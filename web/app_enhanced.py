#!/usr/bin/env python3
"""
Socratic Dialogue Web Demo v3 - Enhanced Edition
Now with argument analysis, adaptive difficulty, debate mode, and threat interrogation.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify, session
from core.socrates import SocraticDialogue, list_topics, list_security_topics, list_modes
from core.argument_analyzer import ArgumentAnalyzer
from core.adaptive_difficulty import AdaptiveSocraticDialogue
from core.threat_interrogator import ThreatInterrogator
from core.debate_mode import DebateModerator
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

dialogues = {}
analyzers = {}
threat_interrogators = {}
debate_moderators = {}


def get_dialogue():
    session_id = session.get('id')
    if not session_id:
        session_id = secrets.token_hex(8)
        session['id'] = session_id

    if session_id not in dialogues:
        base_dialogue = SocraticDialogue()
        dialogues[session_id] = AdaptiveSocraticDialogue(base_dialogue)
        analyzers[session_id] = ArgumentAnalyzer()

    return dialogues[session_id]


def get_analyzer():
    session_id = session.get('id')
    if session_id not in analyzers:
        analyzers[session_id] = ArgumentAnalyzer()
    return analyzers[session_id]


def get_threat_interrogator():
    session_id = session.get('id')
    if session_id not in threat_interrogators:
        threat_interrogators[session_id] = ThreatInterrogator()
    return threat_interrogators[session_id]


def get_debate_moderator():
    session_id = session.get('id')
    if session_id not in debate_moderators:
        debate_moderators[session_id] = DebateModerator()
    return debate_moderators[session_id]


@app.route('/')
def index():
    return render_template('index_enhanced.html',
                         topics=list_topics(),
                         security_topics=list_security_topics(),
                         modes=list_modes())


@app.route('/api/topics')
def api_topics():
    return jsonify({
        "topics": list_topics(),
        "security_topics": list_security_topics(),
        "modes": list_modes()
    })


@app.route('/api/start', methods=['POST'])
def api_start():
    data = request.json
    topic_key = data.get('topic', 'justice')
    custom = data.get('custom')
    mode = data.get('mode', 'socratic')
    security = data.get('security', False)

    dialogue = get_dialogue()
    dialogue.base_dialogue.set_mode(mode)
    dialogue.base_dialogue.set_topic(topic_key, custom, security=security)
    opening = dialogue.base_dialogue.get_opening()

    mode_data = list_modes().get(mode, list_modes()["socratic"])

    return jsonify({
        'topic': dialogue.base_dialogue.topic,
        'mode': mode_data['name'],
        'security': security,
        'message': opening,
        'difficulty': dialogue.get_difficulty_info()
    })


@app.route('/api/respond', methods=['POST'])
def api_respond():
    data = request.json
    user_input = data.get('message', '')

    if not user_input.strip():
        return jsonify({'error': 'Empty message'}), 400

    dialogue = get_dialogue()

    if not dialogue.base_dialogue.topic:
        return jsonify({'error': 'No topic selected'}), 400

    # Get response using adaptive difficulty
    response = dialogue.respond(user_input)

    # Get difficulty info
    difficulty = dialogue.get_difficulty_info()

    return jsonify({
        'message': response,
        'difficulty': difficulty
    })


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """Analyze the current dialogue for argument structure."""
    dialogue = get_dialogue()
    analyzer = get_analyzer()

    if len(dialogue.base_dialogue.history) < 2:
        return jsonify({'error': 'Not enough dialogue to analyze'}), 400

    analysis = analyzer.analyze_dialogue(dialogue.base_dialogue.history)

    # Generate argument graph
    if 'error' not in analysis:
        graph = analyzer.generate_argument_graph(analysis)
        analysis['graph'] = graph

    return jsonify(analysis)


@app.route('/api/threat/analyze', methods=['POST'])
def api_threat_analyze():
    """Analyze a threat model using Socratic questioning."""
    data = request.json
    threat_description = data.get('description', '')

    if not threat_description.strip():
        return jsonify({'error': 'Empty threat description'}), 400

    interrogator = get_threat_interrogator()
    analysis = interrogator.analyze_threat_model(threat_description)

    return jsonify(analysis)


@app.route('/api/threat/control', methods=['POST'])
def api_threat_control():
    """Interrogate a specific security control."""
    data = request.json
    control = data.get('control', '')
    context = data.get('context', '')

    if not control.strip():
        return jsonify({'error': 'Empty control description'}), 400

    interrogator = get_threat_interrogator()
    analysis = interrogator.interrogate_control(control, context)

    return jsonify(analysis)


@app.route('/api/threat/challenge', methods=['POST'])
def api_threat_challenge():
    """Challenge security assumptions."""
    data = request.json
    claim = data.get('claim', '')

    if not claim.strip():
        return jsonify({'error': 'Empty claim'}), 400

    interrogator = get_threat_interrogator()
    questions = interrogator.challenge_assumptions(claim)

    return jsonify({'questions': questions})


@app.route('/api/debate/start', methods=['POST'])
def api_debate_start():
    """Start an AI vs AI debate."""
    data = request.json
    topic = data.get('topic', 'What is justice?')
    mode_a = data.get('mode_a', 'socratic')
    mode_b = data.get('mode_b', 'nietzschean')
    position_a = data.get('position_a', 'Justice is objective')
    position_b = data.get('position_b', 'Justice is power')
    turns = data.get('turns', 6)

    moderator = get_debate_moderator()
    moderator.setup_debate(topic, mode_a, mode_b, position_a, position_b)
    debate_log = moderator.run_debate(turns=turns)
    judgment = moderator.judge_debate()

    return jsonify({
        'debate': debate_log,
        'judgment': judgment,
        'topic': topic
    })


@app.route('/api/export', methods=['POST'])
def api_export():
    """Export dialogue as formatted text."""
    dialogue = get_dialogue()

    if not dialogue.base_dialogue.history:
        return jsonify({'error': 'No dialogue to export'}), 400

    # Format dialogue
    export_text = f"Socratic Dialogue Export\n"
    export_text += f"Topic: {dialogue.base_dialogue.topic}\n"
    export_text += f"Mode: {dialogue.base_dialogue.mode.title()}\n"
    export_text += "=" * 60 + "\n\n"

    for i, msg in enumerate(dialogue.base_dialogue.history, 1):
        speaker = "You" if msg["role"] == "user" else "Philosopher"
        export_text += f"{speaker} (Turn {i}):\n{msg['content']}\n\n"

    export_text += "=" * 60 + "\n"
    export_text += "Generated by Socratic Dialogue v3\n"
    export_text += "github.com/bissembert1618/socratic-dialogue\n"

    return jsonify({
        'text': export_text,
        'filename': f"dialogue_{dialogue.base_dialogue.topic[:20].replace(' ', '_')}.txt"
    })


@app.route('/api/reset', methods=['POST'])
def api_reset():
    dialogue = get_dialogue()
    dialogue.base_dialogue.reset()
    dialogue.current_level = "beginner"
    dialogue.difficulty_score = 30
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    print("\n🏛️  Socratic Dialogue Web Demo v3 - Enhanced Edition")
    print("   Features:")
    print("   ✓ Argument Analysis & Visualization")
    print("   ✓ Adaptive Difficulty")
    print("   ✓ AI vs AI Debates")
    print("   ✓ Socratic Security (Threat Interrogation)")
    print("   ✓ Dialogue Export")
    print("\n   Open http://localhost:5050 in your browser\n")
    app.run(debug=True, port=5050)

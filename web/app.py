#!/usr/bin/env python3
"""
Socratic Dialogue Web Demo v2
Local Flask server — now with philosophical modes and security thinking.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify, session
from core.socrates import SocraticDialogue, list_topics, list_security_topics, list_modes
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

dialogues = {}


def get_dialogue():
    session_id = session.get('id')
    if not session_id:
        session_id = secrets.token_hex(8)
        session['id'] = session_id
    
    if session_id not in dialogues:
        dialogues[session_id] = SocraticDialogue()
    
    return dialogues[session_id]


@app.route('/')
def index():
    return render_template('index.html', 
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
    dialogue.set_mode(mode)
    dialogue.set_topic(topic_key, custom, security=security)
    opening = dialogue.get_opening()
    
    mode_data = list_modes().get(mode, list_modes()["socratic"])
    
    return jsonify({
        'topic': dialogue.topic,
        'mode': mode_data['name'],
        'security': security,
        'message': opening
    })


@app.route('/api/respond', methods=['POST'])
def api_respond():
    data = request.json
    user_input = data.get('message', '')
    
    if not user_input.strip():
        return jsonify({'error': 'Empty message'}), 400
    
    dialogue = get_dialogue()
    
    if not dialogue.topic:
        return jsonify({'error': 'No topic selected'}), 400
    
    response = dialogue.respond(user_input)
    return jsonify({'message': response})


@app.route('/api/reset', methods=['POST'])
def api_reset():
    dialogue = get_dialogue()
    dialogue.reset()
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("⚠️  ANTHROPIC_API_KEY not set.")
        sys.exit(1)
    
    print("\n🏛️  Socratic Dialogue Web Demo v2")
    print("   Open http://localhost:5050 in your browser\n")
    app.run(debug=True, port=5050)

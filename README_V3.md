# Socratic Dialogue v3 - Enhanced Edition

A philosophy game that uses AI to engage in deep philosophical dialogue — now with **argument analysis**, **adaptive difficulty**, **AI vs AI debates**, and **Socratic Security** threat interrogation.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Anthropic Claude](https://img.shields.io/badge/Powered%20by-Claude-orange.svg)](https://www.anthropic.com/)

---

## 🚀 What's New in v3

### 1. **Argument Analysis & Visualization**
- Real-time logical analysis of your arguments
- Automatic detection of claims and contradictions
- Fallacy identification (ad hominem, straw man, etc.)
- Consistency scoring across the conversation
- **Coming soon:** Visual argument graphs showing logical structure

### 2. **Adaptive Difficulty**
- AI adjusts questioning depth based on your sophistication
- Three levels: Beginner → Intermediate → Advanced
- Tracks vocabulary, argumentation quality, and philosophical depth
- Seamlessly scales from simple to complex reasoning

### 3. **AI vs AI Debate Mode**
- Watch two AI philosophers debate each other
- Mix any philosophical traditions (Socratic vs Nietzschean, etc.)
- AI judge analyzes and scores the debate
- Learn by observing different argumentative strategies

### 4. **Socratic Security Suite** 🔒
The world's first philosophical approach to security:

- **Threat Model Interrogator**: Upload threat models, get Socratic questioning
- **Control Challenger**: Distinguish security from security theater
- **Assumption Exposure**: Question unexamined security beliefs
- **Red Team Questions**: Generate adversarial perspectives
- **Compliance vs Security**: Analyze if compliance = actual risk reduction

### 5. **Dialogue Export & Sharing**
- Export conversations as formatted text
- Shareable dialogue summaries
- Track your philosophical journey

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/bissembert1618/socratic-dialogue
cd socratic-dialogue

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# 4. Run enhanced web version
python3 web/app_enhanced.py
# Open http://localhost:5050

# OR run classic CLI version
python3 cli/main.py
```

> **Note:** Get an [Anthropic API key](https://console.anthropic.com/) (free tier available)

---

## Features Deep Dive

### Philosophical Modes

Choose your guide:

| Mode | Style | Best For |
|------|-------|----------|
| **Socratic** | Classical elenchus — expose assumptions through questioning | Beginners, traditional philosophy |
| **Stoic** | Examine what is within your control — Epictetus style | Practical wisdom, emotional clarity |
| **Aristotelian** | Seek the mean, examine virtue as habit | Ethics, character development |
| **Nietzschean** | Challenge values, question will to power | Provocative thinking, value critique |

### Classic Philosophy Topics

- **Justice** — What is justice?
- **Knowledge** — What is knowledge? How do we know?
- **Virtue** — What is virtue? Can it be taught?
- **Beauty** — What is beauty?
- **Truth** — What is truth?
- **Love** — What is love? (Eros, philia, agape)
- **Death** — Should we fear death?
- **Freedom** — Are we truly free?
- **Happiness** — What is the good life?
- **Courage** — What is courage?
- **Piety** — What do we owe the sacred?

### Socratic Security Topics 🔒

Apply philosophical rigor to cybersecurity:

- **Threat Model** — What threats do you actually face?
- **Trust** — What do you trust? Why? Should you?
- **Assumptions** — What assumptions underlie your security posture?
- **Risk** — What is risk? How do we reason about uncertainty?
- **Privacy** — What is privacy? What are we protecting?
- **Access** — Who should have access? On what basis?
- **Failure** — How will your system fail? What then?
- **Adversary** — Who is your adversary? What do they want?

---

## API Endpoints (v3)

### Standard Dialogue
- `POST /api/start` - Start dialogue with mode and topic
- `POST /api/respond` - Send message and get response (with adaptive difficulty)
- `POST /api/reset` - Reset conversation

### New in v3
- `POST /api/analyze` - Get argument analysis of current dialogue
- `POST /api/export` - Export dialogue as text
- `POST /api/threat/analyze` - Analyze threat model
- `POST /api/threat/control` - Interrogate security control
- `POST /api/threat/challenge` - Challenge security assumptions
- `POST /api/debate/start` - Start AI vs AI debate

---

## Architecture

```
socratic-dialogue/
├── core/
│   ├── socrates.py              # Base dialogue engine
│   ├── argument_analyzer.py     # NEW: Logical analysis
│   ├── adaptive_difficulty.py   # NEW: Dynamic difficulty
│   ├── threat_interrogator.py   # NEW: Socratic Security
│   └── debate_mode.py           # NEW: AI vs AI debates
├── cli/
│   └── main.py                  # Terminal interface
├── web/
│   ├── app.py                   # Classic web server
│   ├── app_enhanced.py          # NEW: Enhanced web server (v3)
│   └── templates/
│       ├── index.html           # Classic UI
│       └── index_enhanced.html  # NEW: Enhanced UI (coming)
├── requirements.txt
└── README.md
```

---

## Example Usage

### 1. Standard Dialogue
```python
from core.socrates import SocraticDialogue

dialogue = SocraticDialogue()
dialogue.set_mode("socratic")
dialogue.set_topic("justice")

opening = dialogue.get_opening()
print(opening)
# "What do you believe justice to be? Is it giving each their due?"

response = dialogue.respond("Justice is fairness")
print(response)
# "Fairness to whom? And by what measure? ..."
```

### 2. Argument Analysis
```python
from core.argument_analyzer import ArgumentAnalyzer

analyzer = ArgumentAnalyzer()
analysis = analyzer.analyze_dialogue(dialogue.history)

print(analysis['consistency_score'])  # 0-100
print(analysis['contradictions'])     # List of contradictions
print(analysis['fallacies'])          # Detected fallacies
```

### 3. Adaptive Difficulty
```python
from core.adaptive_difficulty import AdaptiveSocraticDialogue

base = SocraticDialogue()
adaptive = AdaptiveSocraticDialogue(base)

# Automatically adjusts depth based on responses
response = adaptive.respond("Virtue requires wisdom")

difficulty = adaptive.get_difficulty_info()
print(difficulty['level'])  # "beginner", "intermediate", or "advanced"
print(difficulty['score'])  # 0-100
```

### 4. Threat Interrogation
```python
from core.threat_interrogator import ThreatInterrogator

interrogator = ThreatInterrogator()

analysis = interrogator.analyze_threat_model(
    "We encrypt all data at rest using AES-256"
)

print(analysis['assumptions'])
# [{"assumption": "Encryption keys are securely stored",
#   "question": "Who has access to the encryption keys?"}]

print(analysis['questions'])
# ["What happens if the key management system is compromised?",
#  "How do you verify that encryption is actually applied?", ...]
```

### 5. AI vs AI Debate
```python
from core.debate_mode import DebateModerator

moderator = DebateModerator()
moderator.setup_debate(
    topic="Is free will an illusion?",
    mode_a="aristotelian",
    mode_b="stoic",
    position_a="Humans have free will",
    position_b="Free will is limited by nature"
)

debate = moderator.run_debate(turns=8)
judgment = moderator.judge_debate()

print(judgment['winner'])    # Which philosophy won
print(judgment['analysis'])  # Analysis of the debate
```

---

## Use Cases

### For Philosophy Students
- Practice dialectical reasoning
- See how different philosophical traditions approach problems
- Build argumentation skills through analysis feedback
- Explore classic questions with AI guidance

### For Security Professionals
- **Threat Modeling**: Question your threat assumptions
- **Red Teaming**: Generate adversarial perspectives
- **Architecture Review**: Challenge security theater
- **Team Training**: Learn to think critically about security

### For Developers
- **Code Architecture**: Apply Socratic questioning to design decisions
- **Documentation**: See a unique AI/philosophy integration
- **Learning**: Study prompt engineering and multi-agent systems

### For Critical Thinkers
- Sharpen reasoning skills
- Identify logical fallacies in real-time
- Practice defending positions rigorously
- Explore ideas from multiple perspectives

---

## Technical Highlights

**What This Project Demonstrates:**

### AI & Prompt Engineering
- ✅ Multi-mode conversation system with distinct personalities
- ✅ Adaptive system prompts based on user proficiency
- ✅ Multi-agent orchestration (debate mode)
- ✅ Structured output extraction (JSON analysis)
- ✅ Context window management for long conversations

### Software Engineering
- ✅ Clean architecture with separation of concerns
- ✅ Modular design for easy feature addition
- ✅ RESTful API design
- ✅ Session management and state tracking
- ✅ Both CLI and web interfaces

### Domain Expertise
- ✅ Deep knowledge of philosophical traditions
- ✅ Understanding of logical argumentation
- ✅ Application of philosophy to cybersecurity
- ✅ Novel approach to threat modeling

---

## Roadmap

### Phase 1: Visualization (In Progress)
- [ ] D3.js argument graph visualization
- [ ] Interactive contradiction highlighting
- [ ] Real-time argument strength indicators

### Phase 2: Enhanced Debate
- [ ] User can jump into AI debates
- [ ] Tournament mode with bracket system
- [ ] Historical philosopher personas

### Phase 3: Social Features
- [ ] Shareable dialogue links
- [ ] Daily philosophical challenges
- [ ] Leaderboard for argument consistency
- [ ] Community dialogues (multiplayer)

### Phase 4: Security Integration
- [ ] Upload threat model documents
- [ ] Integration with security tools
- [ ] Compliance vs security analyzer
- [ ] Security control database

### Phase 5: Advanced Features
- [ ] Voice mode (speech-to-text/text-to-speech)
- [ ] Historical dialogue database with semantic search
- [ ] Philosophical position mapper
- [ ] Mobile app

---

## Contributing

Contributions welcome! Areas where help is needed:

1. **Frontend**: Build React UI with argument visualization
2. **Analysis**: Improve fallacy detection algorithms
3. **Security**: Expand Socratic Security features
4. **Philosophy**: Add more philosophical modes (Pragmatist, Existentialist, etc.)
5. **Testing**: Unit tests for core modules
6. **Documentation**: Tutorials and guides

---

## Philosophy

> "The unexamined life is not worth living." — Socrates

This project takes that seriously. We use AI not to replace thinking, but to make thinking deeper. The Socratic method — asking questions to expose assumptions — is one of humanity's most powerful intellectual tools. Now it's accessible to anyone.

**Socratic Security** is a novel application: most security thinking is checklist-driven. But real security requires questioning assumptions. "We're PCI compliant" ≠ "We're secure." This tool helps teams think critically about what they're actually protecting, and how.

---

## Credits

**Created by:** Beeri Issembert
**Location:** Tel Aviv, 2026
**Philosophy:** AI-first, philosophically grounded
**License:** MIT

**Powered by:**
- [Anthropic Claude](https://www.anthropic.com/) - AI reasoning
- Flask - Web framework
- Python - Core logic

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## Connect

- **GitHub:** [github.com/bissembert1618/socratic-dialogue](https://github.com/bissembert1618/socratic-dialogue)
- **Email:** beni@focor.io
- **Issues:** [Report bugs or request features](https://github.com/bissembert1618/socratic-dialogue/issues)

---

**Remember:** The goal isn't to win arguments. It's to discover what you actually believe, and why. That's the Socratic way.

🏛️ *Know thyself.*

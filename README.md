# Socratic Dialogue v3 🏛️

A philosophy game that uses AI to engage in deep philosophical dialogue — now with **argument analysis**, **adaptive difficulty**, **AI vs AI debates**, and **Socratic Security** threat interrogation.

> **🚀 NEW IN V3:** Real-time logical analysis, adaptive AI difficulty, debate mode, and security threat interrogation. [See what's new →](README_V3.md)

## Quick Start

```bash
# 1. Clone
git clone https://github.com/bissembert1618/socratic-dialogue
cd socratic-dialogue

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your Anthropic API key (get one at console.anthropic.com)
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# 4. Run (choose one)
python3 cli/main.py            # Terminal version
python3 web/app.py             # Classic web version
python3 web/app_enhanced.py    # NEW: v3 with all features → http://localhost:5050
python3 examples/showcase_v3.py # NEW: Feature demos
```

> **Note:** You need an [Anthropic API key](https://console.anthropic.com/) to run this. The game uses Claude as the AI.

---

## 🚀 What's New in v3

### 1. Argument Analysis & Visualization
- Real-time logical analysis of conversations
- Automatic claim extraction and contradiction detection
- Fallacy identification (ad hominem, straw man, etc.)
- Consistency scoring (0-100)
- Aporia detection (when genuine puzzlement is reached)

### 2. Adaptive Difficulty System
- AI automatically adjusts questioning depth based on your sophistication
- Three levels: Beginner → Intermediate → Advanced
- Tracks: vocabulary, argumentation, self-awareness, depth
- Seamless transitions during conversation

### 3. AI vs AI Debate Mode
- Watch two philosophers debate each other
- Mix any modes (Socratic vs Nietzschean, etc.)
- AI judge scores debates on logic, tradition, engagement
- Learn by observing different argumentative strategies

### 4. Enhanced Socratic Security
- **Threat Model Interrogator**: Upload threat models, get Socratic questioning
- **Control Challenger**: Distinguish security from security theater
- **Assumption Exposure**: Challenge unexamined beliefs
- **Red Team Questions**: Generate adversarial perspectives

### 5. Export & Sharing
- Export dialogues as formatted text
- Shareable summaries
- Track your philosophical journey

[📚 Full v3 Documentation](README_V3.md) | [⚙️ Feature Details](FEATURES_V3.md)

---

## What's New in v2

### Philosophical Modes

Choose your guide:

| Mode | Style |
|------|-------|
| **Socratic** | Classical elenchus — expose assumptions through questioning |
| **Stoic** | Examine what is within your control — Epictetus style |
| **Aristotelian** | Seek the mean, examine virtue as habit and practice |
| **Nietzschean** | Challenge values, question the will to power behind beliefs |

### Socratic Security

Apply philosophical inquiry to cybersecurity and information governance:

- **Threat Model** — What threats do you actually face? How do you know?
- **Trust** — What do you trust? Why? Should you?
- **Assumptions** — What assumptions underlie your security posture?
- **Risk** — What is risk? How do we reason about uncertainty?
- **Privacy** — What is privacy? What are we protecting?
- **Access** — Who should have access? On what basis?
- **Failure** — How will your system fail? What then?
- **Adversary** — Who is your adversary? What do they want?

---

## Philosophy Topics

- **Justice** — What is justice?
- **Knowledge** — What is knowledge? How do we know what we know?
- **Virtue** — What is virtue? Can it be taught?
- **Beauty** — What is beauty?
- **Truth** — What is truth?
- **Love** — What is love?
- **Death** — Should we fear death?
- **Freedom** — What is freedom? Are we truly free?
- **Happiness** — What is the good life?
- **Courage** — What is courage?
- **Piety** — What is piety?

## CLI Commands

- `/topic` — Change topic and mode
- `/mode` — Show current mode
- `/quit` — End dialogue
- `/help` — Show help

## Project Structure

```
socratic-dialogue/
├── core/
│   └── socrates.py      # The dialogue engine (modes + security)
├── cli/
│   └── main.py          # Terminal interface
├── web/
│   ├── app.py           # Flask server
│   └── templates/
│       └── index.html   # Web UI
├── requirements.txt
└── README.md
```

## The Method

> "I know that I know nothing." — Socrates

The Socratic method (elenchus) works by:
1. Taking your initial position
2. Asking for definitions
3. Finding counterexamples
4. Exposing contradictions
5. Reaching aporia (puzzlement)

Aporia isn't failure — it's the beginning of wisdom.

---

Crafted with love in Tel Aviv, 2026. AI-first, philosophically grounded.

[MIT License](LICENSE) · Beeri Issembert

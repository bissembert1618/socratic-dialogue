# Socratic Dialogue

A philosophy game that uses AI to engage in Socratic dialogue — the ancient method of inquiry through questioning.

## The Concept

You take a position on a philosophical topic. Socrates (the AI) doesn't lecture — he asks questions. Probing questions. Questions that expose assumptions, find contradictions, and lead you to examine what you really believe.

The goal isn't to "win." It's to discover what you don't know.

## Topics

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
- Or bring your own question

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"
```

## CLI Version

```bash
python cli/main.py
```

Commands:
- `/topic` — Change topic
- `/quit` — End dialogue
- `/help` — Show help

## Web Version

```bash
python web/app.py
```

Then open http://localhost:5000

## Project Structure

```
socratic-game/
├── core/
│   └── socrates.py      # The dialogue engine
├── cli/
│   └── main.py          # Terminal interface
├── web/
│   ├── app.py           # Flask server
│   └── templates/
│       └── index.html   # Web UI
├── requirements.txt
└── README.md
```

## Philosophy

> "I know that I know nothing." — Socrates

The Socratic method (elenchus) works by:
1. Taking your initial position
2. Asking for definitions
3. Finding counterexamples
4. Exposing contradictions
5. Reaching aporia (puzzlement)

Aporia isn't failure — it's the beginning of wisdom.

---

*The unexamined life is not worth living.*

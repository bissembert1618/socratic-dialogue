# Socratic Dialogue v3 - Feature Documentation

## Complete Feature Overview

---

## 1. Core Dialogue System

### Multiple Philosophical Modes
Four distinct AI personalities, each following authentic philosophical traditions:

**Socratic Mode**
- Classical elenchus (question-and-answer)
- Exposes assumptions through targeted questioning
- Seeks definitions and finds counterexamples
- Leads to aporia (productive puzzlement)
- Never lectures, only questions

**Stoic Mode**
- Focuses on dichotomy of control
- Distinguishes internals (up to us) from externals (not up to us)
- Challenges attachments and judgments
- Direct, almost blunt communication
- Practical wisdom for daily life

**Aristotelian Mode**
- Seeks the mean between extremes
- Examines virtue as habit (hexis)
- Focuses on eudaimonia (flourishing)
- Constructive, builds toward answers
- Uses craft analogies

**Nietzschean Mode**
- Questions the will to power behind beliefs
- Challenges inherited values
- Provocative, uncomfortable
- Uses aphorisms and sharp observations
- Suspects ressentiment hiding behind morality

### Topic Coverage
**Classical Philosophy:**
- Justice, Knowledge, Virtue, Beauty, Truth
- Love, Death, Freedom, Happiness, Courage, Piety

**Socratic Security:**
- Threat modeling, Trust, Assumptions, Risk
- Privacy, Access control, Failure modes, Adversaries

---

## 2. Argument Analysis System

### Real-Time Logical Analysis
The `ArgumentAnalyzer` class provides comprehensive analysis:

**Claim Extraction**
- Identifies explicit claims and assertions
- Distinguishes claims from questions/acknowledgments
- Tracks which turn each claim appears in
- Labels speaker (user vs philosopher)

**Contradiction Detection**
- Compares claims pairwise for logical contradictions
- Classifies severity: direct, implicit, or none
- Explains why claims contradict
- Builds contradiction graph for visualization

**Fallacy Identification**
- Detects common logical fallacies:
  - Ad hominem (attacking character)
  - Straw man (misrepresenting argument)
  - Appeal to authority
  - False dichotomy
  - Slippery slope
- Explains why reasoning is fallacious
- Suggests how to strengthen argument

**Consistency Scoring**
- Rates overall logical consistency (0-100)
- Tracks whether user maintains coherent position
- Identifies when aporia (genuine puzzlement) is reached

**Argument Quality Metrics**
- Argument strength: weak, moderate, strong
- Key insights extracted from dialogue
- Most important moments highlighted

### API Usage
```python
from core.argument_analyzer import ArgumentAnalyzer

analyzer = ArgumentAnalyzer()
analysis = analyzer.analyze_dialogue(history)

# Returns:
{
    "claims": [...],
    "contradictions": [...],
    "fallacies": [...],
    "consistency_score": 85,
    "aporia_reached": false,
    "argument_strength": "strong",
    "key_insights": [...]
}
```

---

## 3. Adaptive Difficulty System

### Dynamic Sophistication Assessment
The system continuously evaluates user sophistication across four dimensions:

**Vocabulary (0-100)**
- Use of philosophical terminology
- Precision of language
- Technical vs colloquial expression

**Argumentation (0-100)**
- Logical structure of responses
- Use of examples and analogies
- Coherence and flow

**Self-Awareness (0-100)**
- Recognition of own assumptions
- Willingness to question beliefs
- Meta-cognitive reflection

**Depth (0-100)**
- Going beyond surface-level
- Considering implications
- Exploring nuance

### Three Difficulty Levels

**Beginner (0-40)**
- Simple, everyday language
- Defines philosophical terms
- Gives concrete examples
- One clear question at a time
- Encouraging and patient
- Connects to familiar experiences

**Intermediate (41-70)**
- Some philosophical terminology with context
- More complex counterexamples
- Occasional compound questions
- Introduces historical positions
- Pushes harder on contradictions
- Expects more rigorous reasoning

**Advanced (71-100)**
- Uses philosophical terminology freely
- Sophisticated counterexamples
- Multi-layered questions
- References historical arguments
- Demands logical precision
- Challenges implicit assumptions aggressively

### Adaptation Strategy
- Initial assessment after 2-3 turns
- Re-assessment every 6 turns
- Smooth transitions between levels
- User never explicitly told their level (maintains flow)
- System prompt dynamically adjusted

### API Usage
```python
from core.adaptive_difficulty import AdaptiveSocraticDialogue

base = SocraticDialogue()
adaptive = AdaptiveSocraticDialogue(base)

response = adaptive.respond("Your message here")
difficulty = adaptive.get_difficulty_info()

# Returns:
{
    "level": "intermediate",
    "score": 65,
    "label": "Intermediate (65/100)"
}
```

---

## 4. AI vs AI Debate Mode

### Philosophical Debates
Watch two AI philosophers debate each other with different modes and positions.

**Features:**
- Choose any two philosophical modes
- Set specific positions for each debater
- Configurable number of turns (2-20)
- AI judge analyzes and scores debate
- Structured debate format

**Debate Structure:**
1. Opening statement (Philosopher A)
2. Response and counter (Philosopher B)
3. Alternating turns
4. Each philosopher defends their position using their tradition
5. Final judgment with scores

**Judging Criteria:**
- Logical consistency (0-10)
- Effective use of tradition (0-10)
- Engagement with opponent (0-10)
- Strength of reasoning (0-10)

**Judge Output:**
- Winner declaration
- Detailed scoring breakdown
- Analysis of debate quality
- Best moment/quote from debate
- One-sentence verdict

### Example Debates
```python
from core.debate_mode import quick_debate

result = quick_debate(
    topic="Is free will an illusion?",
    mode_a="aristotelian",
    mode_b="stoic",
    position_a="Humans have free will",
    position_b="Free will is limited by nature",
    turns=6
)

# Returns debate log + judgment
```

**Suggested Debate Topics:**
- Justice: objective vs subjective
- Knowledge: rationalism vs empiricism
- Ethics: virtue vs consequences
- Truth: absolute vs relative
- Free will vs determinism

---

## 5. Socratic Security Suite

The first philosophical approach to cybersecurity and threat modeling.

### Threat Model Interrogator
Upload or describe a threat model, get Socratic questioning:

**Analysis Provided:**
- **Assumptions identified**: What you're taking for granted
- **Gaps discovered**: What you haven't considered
- **Probing questions**: Deep questions to expose weaknesses
- **Alternative perspectives**: Different ways to view the threat
- **Severity assessment**: How critical are the gaps?

**Example:**
```python
from core.threat_interrogator import ThreatInterrogator

interrogator = ThreatInterrogator()
analysis = interrogator.analyze_threat_model(
    "Our primary threat is external attackers. We use MFA and encryption."
)

# Returns:
{
    "assumptions": [
        {
            "assumption": "MFA prevents all unauthorized access",
            "question": "What if an attacker compromises MFA seed?"
        }
    ],
    "gaps": [...],
    "questions": [...],
    "alternative_perspectives": [...]
}
```

### Security Control Challenger
Distinguish security from security theater:

**Analysis:**
- Effectiveness rating (low/medium/high)
- Security theater risk score (0-100)
- Key assumptions in the control
- Bypass scenarios with likelihood
- Probing questions about implementation
- Verdict and recommendations

**Questions Asked:**
- "Does this control actually reduce risk or just appearance?"
- "What assumptions underlie this control?"
- "How could an attacker bypass this?"
- "What are we NOT protecting by focusing here?"
- "Is this compliance-driven or risk-driven?"

### Assumption Challenger
Give a security claim, get 5 penetrating questions:

**Example:**
Claim: "We're secure because we're SOC 2 compliant"

Questions:
1. "What specific risks does SOC 2 address, and which does it not?"
2. "How do you verify compliance between audits?"
3. "Can you be compliant and still be breached?"
4. "What security gaps exist despite compliance?"
5. "Who decided SOC 2 is the right framework for your actual threats?"

### Red Team Question Generator
Generate both philosophical and tactical red team questions:

**Philosophical Questions:**
- Expose assumptions about trust
- Challenge risk prioritization
- Question adversary models

**Red Team Questions:**
- Specific attack vectors
- System weaknesses
- Exploitation strategies

**Output:**
- Philosophical probing questions
- Tactical attacker questions
- Identified blind spots
- Testing recommendations

### Compliance vs Security Analyzer
Analyze if compliance requirements actually improve security:

**Analysis:**
- Security improvement level (none/minimal/moderate/significant)
- Compliance pass/fail assessment
- Gap analysis (what's missing despite compliance)
- Security theater elements identified
- Actual risk reduction description
- Verdict on compliance value

**Example:**
```python
analysis = interrogator.compliance_vs_security(
    requirement="Annual penetration testing (SOC 2)",
    implementation="We do pentest once per year"
)

# Probes: Is annual frequency enough?
# What happens the other 364 days?
# Do you address findings immediately?
```

---

## 6. Export & Sharing

### Dialogue Export
Export conversations as formatted text files:

**Format:**
```
Socratic Dialogue Export
Topic: [Topic Name]
Mode: [Philosophical Mode]
========================================

You (Turn 1):
[Your message]

Philosopher (Turn 2):
[AI response]

...

========================================
Generated by Socratic Dialogue v3
```

**Features:**
- Clean, readable formatting
- Topic and mode metadata
- Turn numbering
- Speaker labels
- Timestamp (optional)
- Shareable text file

### Future: Shareable Links
(Planned for Phase 3)
- Generate unique URL for dialogue
- Replay conversation for others
- Social media cards
- "I just discovered I'm a Stoic!" sharing

---

## 7. Web Interface Features

### Enhanced UI (v3)
New features in `app_enhanced.py`:

**Dashboard:**
- Mode selector with descriptions
- Topic browser (Philosophy & Security tabs)
- Difficulty level indicator
- Analysis panel

**Dialogue View:**
- Clean message display
- Real-time difficulty updates
- Analysis on demand
- Export button

**Analysis Panel:**
- Claims extracted
- Contradictions highlighted
- Consistency score
- Fallacies detected
- Argument strength

**Security Panel:**
- Threat model input
- Control interrogation
- Question generation
- Red team mode

**Debate Panel:**
- Mode selection (A vs B)
- Position setting
- Turn count configuration
- Live debate display
- Judge verdict with scores

### API Endpoints Summary

**Standard:**
- `POST /api/start` - Start dialogue
- `POST /api/respond` - Continue dialogue
- `POST /api/reset` - Clear conversation

**Analysis:**
- `POST /api/analyze` - Get argument analysis
- `POST /api/export` - Export dialogue

**Security:**
- `POST /api/threat/analyze` - Analyze threat model
- `POST /api/threat/control` - Interrogate control
- `POST /api/threat/challenge` - Challenge assumptions

**Debate:**
- `POST /api/debate/start` - Start AI debate

---

## 8. CLI Interface

### Commands
- `/topic` - Change topic and mode
- `/mode` - Show current mode
- `/quit` - End dialogue
- `/help` - Show help

### Features
- Color-coded output
- Philosophical quotes
- Mode indicators
- Topic display
- Clean formatting

---

## Technical Architecture

### Module Structure

**core/socrates.py**
- Base dialogue engine
- Mode definitions
- Topic management
- Conversation state

**core/argument_analyzer.py**
- Claim extraction
- Contradiction detection
- Fallacy identification
- Graph generation

**core/adaptive_difficulty.py**
- User profiling
- Sophistication assessment
- Dynamic prompt adjustment
- Level transitions

**core/threat_interrogator.py**
- Threat analysis
- Control interrogation
- Assumption challenging
- Red team questions
- Compliance analysis

**core/debate_mode.py**
- Debate orchestration
- Multi-agent management
- Judge system
- Turn management

### Design Patterns

**Strategy Pattern**: Different philosophical modes
**Observer Pattern**: Difficulty adapts to user responses
**Factory Pattern**: Creating analyzers and interrogators
**Template Method**: Debate structure with customizable steps

### State Management
- Session-based storage (web)
- In-memory conversation history
- Difficulty tracking per session
- Analysis caching

---

## Performance Considerations

### API Usage
- ~150-400 tokens per response
- Adaptive difficulty adds ~50 tokens every 6 turns
- Analysis: ~500-1000 tokens per request
- Debates: ~300-500 tokens per turn
- Total cost: ~$0.003-0.015 per conversation (Claude Sonnet)

### Optimization Tips
- Cache analysis results
- Batch analyze at end instead of per-turn
- Use Claude Haiku for less critical features
- Implement conversation length limits
- Add rate limiting for public deployment

---

## Future Enhancements

See `README_V3.md` for complete roadmap.

**Immediate (Phase 1):**
- Argument graph visualization
- Enhanced UI with React
- Historical dialogue search

**Near-term (Phase 2-3):**
- Voice mode
- Social features
- Mobile app
- Gamification

**Long-term (Phase 4-5):**
- Historical philosopher database
- Philosophical position mapper
- Community features
- Security tool integrations

---

## Credits

**Author:** Beeri Issembert
**Email:** beni@focor.io
**License:** MIT
**Powered by:** Anthropic Claude

---

**"The unexamined code is not worth running."** — Socrates (probably)

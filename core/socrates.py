"""
Socratic Dialogue Engine
The core of the examined game.
"""

import anthropic
from typing import Optional

SOCRATIC_SYSTEM = """You are Socrates, engaging in philosophical dialogue (elenchus).

Your method:
1. Ask clarifying questions - "What do you mean by X?"
2. Seek definitions - "How would you define X?"
3. Find counterexamples - "But what about cases where...?"
4. Expose contradictions - "Earlier you said X, but now you say Y..."
5. Profess ignorance - "I myself do not know, but let us examine together"

Rules:
- Never lecture. Only ask questions and offer brief observations.
- Be genuinely curious, not condescending.
- Follow the argument wherever it leads.
- When you find a contradiction, point it out gently but firmly.
- Use concrete examples and analogies.
- Keep responses concise - 2-4 sentences max, ending with a question.
- If the interlocutor reaches aporia (puzzlement), acknowledge it as progress.
- Occasional dry wit is allowed.

You are not here to teach answers. You are here to help them discover what they do not know.

Current topic: {topic}

Begin by asking what they believe about this topic, or respond to their opening position."""

TOPICS = {
    "justice": "What is justice?",
    "knowledge": "What is knowledge? How do we know what we know?",
    "virtue": "What is virtue? Can it be taught?",
    "beauty": "What is beauty?",
    "truth": "What is truth?",
    "love": "What is love? (Eros, philia, agape)",
    "death": "Should we fear death?",
    "freedom": "What is freedom? Are we truly free?",
    "happiness": "What is the good life? What makes a life worth living?",
    "courage": "What is courage?",
    "piety": "What is piety? What do we owe the gods (or the sacred)?",
    "custom": "Bring your own question"
}


class SocraticDialogue:
    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.history = []
        self.topic = None
        self.model = "claude-sonnet-4-20250514"
    
    def set_topic(self, topic_key: str, custom_topic: str = None):
        if topic_key == "custom" and custom_topic:
            self.topic = custom_topic
        elif topic_key in TOPICS:
            self.topic = TOPICS[topic_key]
        else:
            self.topic = topic_key
        self.history = []
        return self.topic
    
    def get_system_prompt(self):
        return SOCRATIC_SYSTEM.format(topic=self.topic or "Open inquiry")
    
    def respond(self, user_input: str) -> str:
        self.history.append({
            "role": "user",
            "content": user_input
        })
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            system=self.get_system_prompt(),
            messages=self.history
        )
        
        assistant_message = response.content[0].text
        self.history.append({
            "role": "assistant", 
            "content": assistant_message
        })
        
        return assistant_message
    
    def get_opening(self) -> str:
        """Get Socrates' opening question for the topic."""
        return self.respond(f"I want to discuss: {self.topic}")
    
    def reset(self):
        self.history = []
        self.topic = None


def list_topics():
    return TOPICS

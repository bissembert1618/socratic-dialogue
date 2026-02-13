"""
Adaptive Difficulty System
Adjusts philosopher's questioning depth based on user sophistication.
"""

import anthropic
from typing import List, Dict, Optional
import re


class UserProfiler:
    """Profiles user sophistication based on their responses."""

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"

    def assess_sophistication(self, history: List[Dict[str, str]]) -> Dict:
        """
        Assess user's philosophical sophistication based on dialogue history.
        Returns level (beginner/intermediate/advanced) and indicators.
        """
        if len(history) < 2:
            return {"level": "beginner", "score": 30, "indicators": []}

        # Get only user messages
        user_messages = [msg["content"] for msg in history if msg["role"] == "user"]

        if len(user_messages) < 2:
            return {"level": "beginner", "score": 30, "indicators": []}

        combined_text = " ".join(user_messages[-5:])  # Last 5 messages

        assessment_prompt = f"""Assess the philosophical sophistication of this speaker based on their responses.

Speaker's responses:
{combined_text}

Rate on these dimensions (0-100 each):
1. **Vocabulary**: Use of philosophical terms, precision of language
2. **Argumentation**: Logical structure, use of examples, coherence
3. **Self-awareness**: Recognition of own assumptions, willingness to question beliefs
4. **Depth**: Going beyond surface-level, considering implications

Respond in JSON:
{{
    "vocabulary": 0-100,
    "argumentation": 0-100,
    "self_awareness": 0-100,
    "depth": 0-100,
    "overall_score": 0-100,
    "level": "beginner|intermediate|advanced",
    "indicators": ["what suggests this level"],
    "recommendations": ["how to adjust dialogue"]
}}

Be fair but accurate. Most people start as beginners."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=800,
                messages=[{"role": "user", "content": assessment_prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                import json
                assessment = json.loads(json_match.group())
                return assessment
            else:
                return {"level": "intermediate", "score": 50, "indicators": []}

        except Exception as e:
            return {"level": "intermediate", "score": 50, "indicators": [], "error": str(e)}


class AdaptiveSocraticDialogue:
    """Enhanced dialogue system with adaptive difficulty."""

    def __init__(self, base_dialogue, api_key: Optional[str] = None):
        self.base_dialogue = base_dialogue
        self.profiler = UserProfiler(api_key=api_key)
        self.current_level = "beginner"
        self.difficulty_score = 30

    def update_difficulty(self):
        """Update difficulty based on conversation history."""
        if len(self.base_dialogue.history) >= 4:
            assessment = self.profiler.assess_sophistication(self.base_dialogue.history)
            self.current_level = assessment.get("level", "intermediate")
            self.difficulty_score = assessment.get("overall_score", 50)
            return assessment
        return None

    def get_adapted_system_prompt(self) -> str:
        """Get system prompt adjusted for current difficulty level."""
        base_prompt = self.base_dialogue.get_system_prompt()

        level_adjustments = {
            "beginner": """
DIFFICULTY: BEGINNER
- Use simple, everyday language
- Define philosophical terms when first used
- Give concrete examples for abstract concepts
- Ask one clear question at a time
- Be encouraging and patient
- Connect to familiar experiences""",

            "intermediate": """
DIFFICULTY: INTERMEDIATE
- Use some philosophical terminology with light context
- Present more complex counterexamples
- Ask compound questions occasionally
- Introduce historical philosophical positions
- Push harder on contradictions
- Expect more rigorous reasoning""",

            "advanced": """
DIFFICULTY: ADVANCED
- Use philosophical terminology freely
- Present sophisticated counterexamples
- Reference historical arguments and positions
- Ask multi-layered questions
- Demand logical precision
- Challenge implicit assumptions aggressively
- Expect familiarity with philosophical concepts"""
        }

        adjustment = level_adjustments.get(self.current_level, level_adjustments["intermediate"])
        return base_prompt + "\n\n" + adjustment

    def respond(self, user_input: str) -> str:
        """Respond with adaptive difficulty."""
        # Every 3 turns, reassess difficulty
        if len(self.base_dialogue.history) % 6 == 0 and len(self.base_dialogue.history) > 0:
            self.update_difficulty()

        # Temporarily override system prompt
        original_get_prompt = self.base_dialogue.get_system_prompt
        self.base_dialogue.get_system_prompt = self.get_adapted_system_prompt

        # Get response using base dialogue
        response = self.base_dialogue.respond(user_input)

        # Restore original method
        self.base_dialogue.get_system_prompt = original_get_prompt

        return response

    def get_difficulty_info(self) -> Dict:
        """Get current difficulty information for UI display."""
        return {
            "level": self.current_level,
            "score": self.difficulty_score,
            "label": f"{self.current_level.title()} ({self.difficulty_score}/100)"
        }

"""
Debate Mode - AI vs AI Philosophical Debate
Watch two AI philosophers debate each other on a topic.
"""

import anthropic
from typing import Optional, List, Dict
from .socrates import MODES


class DebateModerator:
    """Orchestrate debates between two AI philosophers."""

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"
        self.debate_history = []

    def setup_debate(self, topic: str, mode_a: str, mode_b: str, position_a: str, position_b: str):
        """
        Set up a debate between two philosophical modes.

        Args:
            topic: The question or topic to debate
            mode_a: First philosopher's mode (e.g., 'socratic')
            mode_b: Second philosopher's mode (e.g., 'nietzschean')
            position_a: Position A takes
            position_b: Position B takes
        """
        self.topic = topic
        self.mode_a = mode_a
        self.mode_b = mode_b
        self.position_a = position_a
        self.position_b = position_b
        self.debate_history = []

    def _get_philosopher_prompt(self, mode: str, position: str, is_first: bool) -> str:
        """Generate system prompt for a debating philosopher."""
        mode_data = MODES.get(mode, MODES["socratic"])
        base_style = mode_data["prompt"]

        debate_rules = f"""
DEBATE MODE ACTIVE

Your position: {position}
Topic: {self.topic}

Rules:
1. Defend your position using your philosophical tradition
2. Address your opponent's arguments directly
3. Use your characteristic style (questions, assertions, provocations)
4. Be rigorous but respectful
5. Keep responses concise (3-5 sentences)
6. End with either a question or a strong assertion
{'7. You speak first - open by stating your position clearly' if is_first else '7. Respond to your opponent then advance your position'}

Remember: You're not seeking truth together - you're defending a position.
Be intellectually honest but argue forcefully."""

        return base_style + "\n\n" + debate_rules

    def run_debate(self, turns: int = 6) -> List[Dict]:
        """
        Run a debate for specified number of turns.

        Returns:
            List of debate exchanges with analysis
        """
        debate_log = []

        # Philosopher A opens
        opening = self._get_response(
            self.mode_a,
            self.position_a,
            f"Open the debate. State your position on: {self.topic}",
            [],
            is_first=True
        )

        debate_log.append({
            "turn": 1,
            "speaker": f"{MODES[self.mode_a]['name']} (Position: {self.position_a})",
            "mode": self.mode_a,
            "message": opening
        })

        self.debate_history.append({
            "speaker": self.mode_a,
            "message": opening
        })

        # Alternate turns
        for turn in range(2, turns + 1):
            # Determine who speaks
            current_mode = self.mode_b if turn % 2 == 0 else self.mode_a
            current_position = self.position_b if turn % 2 == 0 else self.position_a
            opponent_mode = self.mode_a if turn % 2 == 0 else self.mode_b

            # Get previous message from opponent
            previous_message = self.debate_history[-1]["message"]

            # Generate response
            response = self._get_response(
                current_mode,
                current_position,
                f"Respond to your opponent: '{previous_message[:200]}...'",
                self.debate_history[-3:],  # Last few exchanges for context
                is_first=False
            )

            mode_name = MODES[current_mode]['name']
            position_label = current_position

            debate_log.append({
                "turn": turn,
                "speaker": f"{mode_name} (Position: {position_label})",
                "mode": current_mode,
                "message": response
            })

            self.debate_history.append({
                "speaker": current_mode,
                "message": response
            })

        return debate_log

    def _get_response(self, mode: str, position: str, prompt: str, history: List[Dict], is_first: bool) -> str:
        """Get response from a philosopher in debate mode."""
        system_prompt = self._get_philosopher_prompt(mode, position, is_first)

        # Build messages from history
        messages = []
        for entry in history:
            messages.append({
                "role": "assistant" if entry["speaker"] == mode else "user",
                "content": entry["message"]
            })

        # Add current prompt
        messages.append({
            "role": "user",
            "content": prompt
        })

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=400,
                system=system_prompt,
                messages=messages
            )

            return response.content[0].text

        except Exception as e:
            return f"[Error generating response: {e}]"

    def judge_debate(self) -> Dict:
        """
        Have an AI judge analyze the debate and declare a winner.
        """
        if len(self.debate_history) < 2:
            return {"error": "Not enough debate history"}

        # Format debate for judging
        debate_text = self._format_debate()

        judge_prompt = f"""You are judging a philosophical debate.

Topic: {self.topic}

Debaters:
- {MODES[self.mode_a]['name']}: Position "{self.position_a}"
- {MODES[self.mode_b]['name']}: Position "{self.position_b}"

Debate:
{debate_text}

Judge based on:
1. Logical consistency
2. Effective use of philosophical tradition
3. Addressing opponent's arguments
4. Strength of reasoning

Respond in JSON:
{{
    "winner": "{self.mode_a}|{self.mode_b}|draw",
    "scores": {{
        "{self.mode_a}": {{"logic": 0-10, "tradition": 0-10, "engagement": 0-10, "reasoning": 0-10}},
        "{self.mode_b}": {{"logic": 0-10, "tradition": 0-10, "engagement": 0-10, "reasoning": 0-10}}
    }},
    "analysis": "Brief analysis of debate",
    "best_moment": "Quote the best argument from the debate",
    "verdict": "One-sentence verdict"
}}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1200,
                messages=[{"role": "user", "content": judge_prompt}]
            )

            import re, json
            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse judgment"}

        except Exception as e:
            return {"error": str(e)}

    def _format_debate(self) -> str:
        """Format debate history for analysis."""
        lines = []
        for i, entry in enumerate(self.debate_history, 1):
            speaker = MODES[entry["speaker"]]['name']
            lines.append(f"Turn {i} - {speaker}:")
            lines.append(entry["message"])
            lines.append("")
        return "\n".join(lines)


def quick_debate(topic: str, mode_a: str = "socratic", mode_b: str = "nietzschean",
                 position_a: str = "Yes", position_b: str = "No",
                 turns: int = 6, api_key: Optional[str] = None) -> Dict:
    """Run a quick debate and return results."""
    moderator = DebateModerator(api_key=api_key)
    moderator.setup_debate(topic, mode_a, mode_b, position_a, position_b)
    debate_log = moderator.run_debate(turns=turns)
    judgment = moderator.judge_debate()

    return {
        "topic": topic,
        "debate": debate_log,
        "judgment": judgment
    }

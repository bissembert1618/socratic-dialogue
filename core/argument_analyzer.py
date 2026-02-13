"""
Argument Analyzer - Logical structure and argumentation analysis
Analyzes dialogues for claims, contradictions, fallacies, and argument structure.
"""

import anthropic
from typing import List, Dict, Optional, Tuple
import json
import re


class ArgumentAnalyzer:
    """Analyzes philosophical dialogues for logical structure and quality."""

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"

    def analyze_dialogue(self, history: List[Dict[str, str]]) -> Dict:
        """
        Comprehensive analysis of the dialogue structure.
        Returns claims, contradictions, fallacies, and argument quality metrics.
        """
        if len(history) < 2:
            return {"error": "Not enough dialogue history to analyze"}

        # Extract just user messages for claim analysis
        user_messages = [msg for msg in history if msg["role"] == "user"]

        if len(user_messages) < 2:
            return {"claims": [], "contradictions": [], "fallacies": [], "quality": "insufficient"}

        # Build analysis prompt
        dialogue_text = self._format_dialogue(history)

        analysis_prompt = f"""Analyze this philosophical dialogue for logical structure.

Dialogue:
{dialogue_text}

Provide analysis in JSON format:
{{
    "claims": [
        {{"id": 1, "text": "brief claim", "speaker": "user", "turn": 1}}
    ],
    "contradictions": [
        {{"claim_1_id": 1, "claim_2_id": 3, "explanation": "why they contradict"}}
    ],
    "fallacies": [
        {{"turn": 2, "type": "ad hominem", "explanation": "attacks character not argument"}}
    ],
    "argument_strength": "weak|moderate|strong",
    "consistency_score": 0-100,
    "aporia_reached": true|false,
    "key_insights": ["insight 1", "insight 2"]
}}

Focus on the user's claims and reasoning. Be precise and fair."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": analysis_prompt}]
            )

            # Extract JSON from response
            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                analysis = json.loads(json_match.group())
                return analysis
            else:
                return {"error": "Could not parse analysis", "raw": content}

        except Exception as e:
            return {"error": str(e)}

    def detect_contradiction(self, claim1: str, claim2: str) -> Dict:
        """Check if two claims contradict each other."""
        prompt = f"""Do these two claims contradict each other? Respond in JSON.

Claim 1: {claim1}
Claim 2: {claim2}

Format:
{{
    "contradicts": true|false,
    "explanation": "brief explanation",
    "severity": "direct|implicit|none"
}}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"contradicts": False, "explanation": "Could not analyze", "severity": "none"}

        except Exception as e:
            return {"error": str(e)}

    def extract_claims(self, text: str) -> List[str]:
        """Extract explicit claims from a piece of text."""
        prompt = f"""Extract the explicit claims or assertions from this text.
Return as a JSON array of strings.

Text: {text}

Format: ["claim 1", "claim 2", ...]

Only include factual or normative claims, not questions or acknowledgments."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\[[\s\S]*\]', content)

            if json_match:
                return json.loads(json_match.group())
            return []

        except Exception as e:
            return []

    def generate_argument_graph(self, analysis: Dict) -> Dict:
        """
        Generate data structure for argument graph visualization.
        Returns nodes and edges for D3.js or similar.
        """
        nodes = []
        edges = []

        # Create nodes from claims
        for claim in analysis.get("claims", []):
            nodes.append({
                "id": f"claim_{claim['id']}",
                "label": claim["text"][:50] + ("..." if len(claim["text"]) > 50 else ""),
                "type": "claim",
                "speaker": claim["speaker"],
                "turn": claim["turn"]
            })

        # Create edges from contradictions
        for contradiction in analysis.get("contradictions", []):
            edges.append({
                "source": f"claim_{contradiction['claim_1_id']}",
                "target": f"claim_{contradiction['claim_2_id']}",
                "type": "contradiction",
                "label": "contradicts"
            })

        return {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "total_claims": len(nodes),
                "contradictions": len(edges),
                "consistency": analysis.get("consistency_score", 0)
            }
        }

    def _format_dialogue(self, history: List[Dict[str, str]]) -> str:
        """Format dialogue history for analysis."""
        lines = []
        for i, msg in enumerate(history, 1):
            speaker = "User" if msg["role"] == "user" else "Philosopher"
            lines.append(f"Turn {i} ({speaker}): {msg['content']}")
        return "\n\n".join(lines)


def quick_analyze(history: List[Dict[str, str]], api_key: Optional[str] = None) -> Dict:
    """Quick analysis function for easy import."""
    analyzer = ArgumentAnalyzer(api_key=api_key)
    return analyzer.analyze_dialogue(history)

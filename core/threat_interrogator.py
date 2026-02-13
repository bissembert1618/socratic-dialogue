"""
Threat Model Interrogator - Socratic Security
Apply philosophical questioning to security architecture and threat modeling.
"""

import anthropic
from typing import Optional, Dict, List
import re
import json


class ThreatInterrogator:
    """Apply Socratic method to threat modeling and security architecture."""

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"
        self.conversation_history = []

    def analyze_threat_model(self, threat_description: str) -> Dict:
        """
        Analyze a threat model or security control using Socratic questioning.
        Returns probing questions and identified assumptions.
        """
        analysis_prompt = f"""You are a security philosopher applying the Socratic method to threat modeling.

A security professional describes their threat model:
"{threat_description}"

Apply philosophical rigor to expose assumptions, gaps, and unexplored scenarios.

Generate your analysis in JSON format:
{{
    "assumptions": [
        {{"assumption": "what they're assuming", "question": "probing question"}}
    ],
    "gaps": [
        {{"gap": "what's missing", "risk": "potential impact"}}
    ],
    "questions": [
        "Deep question 1",
        "Deep question 2",
        "Deep question 3"
    ],
    "alternative_perspectives": [
        {{"perspective": "different view", "implication": "what it means"}}
    ],
    "severity": "low|medium|high|critical"
}}

Be incisive but not dismissive. Find what they haven't considered."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": analysis_prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse analysis"}

        except Exception as e:
            return {"error": str(e)}

    def interrogate_control(self, control_description: str, context: str = "") -> Dict:
        """
        Question a specific security control.
        Are they solving the right problem? Is it security or theater?
        """
        prompt = f"""A security control is described: "{control_description}"

Context: {context if context else "General enterprise security"}

Apply the Socratic method to determine:
1. Does this control actually reduce risk, or just give the appearance of security?
2. What assumptions underlie this control?
3. How could an attacker bypass or abuse this control?
4. What are we NOT protecting by focusing here?
5. Is this compliance-driven or risk-driven?

Respond in JSON:
{{
    "effectiveness": "low|medium|high",
    "security_theater_risk": 0-100,
    "key_assumptions": ["assumption 1", "assumption 2"],
    "bypass_scenarios": [
        {{"scenario": "how to bypass", "likelihood": "low|medium|high"}}
    ],
    "probing_questions": [
        "Question 1",
        "Question 2",
        "Question 3"
    ],
    "verdict": "This control...",
    "recommendations": ["rec 1", "rec 2"]
}}

Be rigorous. Security theater is dangerous."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse analysis"}

        except Exception as e:
            return {"error": str(e)}

    def challenge_assumptions(self, security_claim: str) -> List[str]:
        """
        Given a security claim, generate Socratic questions to challenge assumptions.
        """
        prompt = f"""Security claim: "{security_claim}"

Generate 5 penetrating Socratic questions that challenge the assumptions in this claim.

Format as JSON array:
["Question 1?", "Question 2?", "Question 3?", "Question 4?", "Question 5?"]

Make questions progressively deeper. Start with obvious, end with subtle."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=800,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\[[\s\S]*\]', content)

            if json_match:
                return json.loads(json_match.group())
            return []

        except Exception as e:
            return []

    def red_team_questions(self, system_description: str) -> Dict:
        """
        Generate red team questions for a system description.
        What would an attacker ask?
        """
        prompt = f"""System description: {system_description}

You are both a philosopher and a red team attacker. Generate questions from both perspectives:

1. **Philosophical questions**: Expose assumptions about trust, risk, and adversaries
2. **Red team questions**: How would you actually attack this?

Respond in JSON:
{{
    "philosophical": [
        {{"question": "philosophical question", "targets": "what assumption"}}
    ],
    "red_team": [
        {{"question": "attacker question", "attack_vector": "brief description"}}
    ],
    "blind_spots": ["potential blind spot 1", "potential blind spot 2"],
    "recommendations": ["what to explore", "what to test"]
}}

Be adversarial but constructive."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse analysis"}

        except Exception as e:
            return {"error": str(e)}

    def compliance_vs_security(self, requirement: str, implementation: str) -> Dict:
        """
        Analyze if a compliance requirement actually improves security.
        """
        prompt = f"""Compliance requirement: {requirement}
Implementation: {implementation}

Analyze: Does this implementation actually improve security, or just check a compliance box?

Respond in JSON:
{{
    "security_improvement": "none|minimal|moderate|significant",
    "compliance_score": "passes|fails",
    "gap_analysis": "What security gaps remain despite compliance?",
    "security_theater_elements": ["element 1", "element 2"],
    "actual_risk_reduction": "Describe real risk reduction",
    "questions_to_ask": [
        "Question 1",
        "Question 2",
        "Question 3"
    ],
    "verdict": "One-line summary"
}}

Distinguish compliance from security."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.content[0].text
            json_match = re.search(r'\{[\s\S]*\}', content)

            if json_match:
                return json.loads(json_match.group())
            return {"error": "Could not parse analysis"}

        except Exception as e:
            return {"error": str(e)}


def quick_threat_analysis(threat_model: str, api_key: Optional[str] = None) -> Dict:
    """Quick analysis function for easy import."""
    interrogator = ThreatInterrogator(api_key=api_key)
    return interrogator.analyze_threat_model(threat_model)

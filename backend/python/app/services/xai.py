import datetime
from typing import Dict, List

class ExplainableAIEngine:
    """Provides transparent reasoning for AI security decisions."""

    def __init__(self):
        self.feature_weights = {
            "UNUSUAL_PORT": 0.45,
            "GLOBAL_CAMPAIGN_MATCH": 0.85,
            "CREDENTIAL_ANOMALY": 0.70,
            "LATERAL_MOVEMENT_PATTERN": 0.90
        }

    def generate_reasoning_report(self, threat_id: str, findings: List[str]) -> Dict:
        """Generates a human-readable explanation of why a threat was flagged."""
        print(f"[XAI] Generating reasoning for Threat: {threat_id}...")

        evidence = []
        total_certainty = 0.0

        for finding in findings:
            weight = self.feature_weights.get(finding, 0.2)
            evidence.append({
                "factor": finding,
                "contribution": f"{weight*100}%",
                "description": f"Internal telemetry for {finding} correlates with high-risk TTPs."
            })
            total_certainty = max(total_certainty, weight)

        return {
            "threat_id": threat_id,
            "decision": "FLAGGED_CRITICAL",
            "confidence": f"{total_certainty*100}%",
            "evidence_breakdown": evidence,
            "ai_logic_path": "Correlation -> Behavioral Analysis -> XAI Mapping",
            "timestamp": datetime.datetime.now().isoformat()
        }

xai_engine = ExplainableAIEngine()

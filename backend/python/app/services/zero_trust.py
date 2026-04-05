import datetime
from typing import Dict, List, Optional

class ZeroTrustPolicyEngine:
    def __init__(self):
        self.trust_scores = {} # device_id -> score (0.0 to 1.0)

    def evaluate_access_request(self, device_id: str, user_id: str, context: Dict) -> Dict:
        """Implements 'Never Trust, Always Verify' logic for access control."""
        print(f"[ZERO-TRUST] Evaluating request for Device: {device_id}, User: {user_id}")

        # Factors: Location, Time, Device Health, Past Behavior
        risk_factors = []
        trust_score = 1.0

        if context.get("location") == "UNUSUAL":
            trust_score -= 0.4
            risk_factors.append("UNUSUAL_LOCATION")

        if context.get("mfa_status") != "VERIFIED":
            trust_score -= 0.6
            risk_factors.append("MFA_NOT_VERIFIED")

        if context.get("device_compliance") == "NON_COMPLIANT":
            trust_score -= 0.5
            risk_factors.append("DEVICE_OUT_OF_COMPLIANCE")

        is_authorized = trust_score > 0.5

        return {
            "authorized": is_authorized,
            "final_trust_score": max(0.0, round(trust_score, 2)),
            "risk_factors": risk_factors,
            "policy_applied": "DEFAULT_STRICT_ACCESS",
            "timestamp": datetime.datetime.now().isoformat()
        }

zero_trust_engine = ZeroTrustPolicyEngine()

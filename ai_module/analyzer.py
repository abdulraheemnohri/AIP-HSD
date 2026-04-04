import datetime
import random
from typing import List, Dict, Optional

class SecurityAnalyzer:
    def __init__(self, model_name: str = "AIP-GPT-2"):
        self.model_name = model_name
        self.version = "1.0.0"

    def normalize_log(self, raw_log: Dict) -> Dict:
        """Converts raw logs into a unified schema for analysis."""
        return {
            "timestamp": raw_log.get("timestamp", datetime.datetime.now().isoformat()),
            "source": raw_log.get("source_ip", "0.0.0.0"),
            "event_type": raw_log.get("type", "unknown"),
            "raw_message": raw_log.get("msg", ""),
            "normalized": True
        }

    def calculate_risk_score(self, threats: List[Dict], internal_anomalies: List[Dict]) -> float:
        """Calculates a composite risk score (0-100)."""
        base_threat = sum(t.get("severity", 0) for t in threats)
        internal_factor = len(internal_anomalies) * 1.5
        score = min(100.0, base_threat + internal_factor)
        return round(score, 2)

    def generate_summary(self, alerts: List[Dict]) -> str:
        """Simulates natural language summarization for the dashboard."""
        if not alerts:
            return "All systems stable. No significant threats detected in the last 24 hours."

        count = len(alerts)
        return f"AI Analysis: {count} active alerts. Most critical issue is {alerts[0].get('title', 'N/A')}. Increasing firewall vigilance in EMEA region recommended."

    def query_response(self, query: str) -> Dict:
        """Simulates responding to user queries via LLM."""
        return {
            "query": query,
            "response": f"Analyzing '{query}' across internal logs and OSINT feeds. Results show matching patterns in ransomware-alpha variants targeting regional servers.",
            "sources": ["CERTVN", "Internal Firewall Logs", "Global Threat DB"],
            "model": self.model_name
        }

    # ADVANCED AI COMPONENTS
    def autonomous_threat_hunter(self, internal_telemetry: List[Dict], osint_data: List[Dict]) -> List[Dict]:
        """AI Threat Hunter correlating internal anomalies with global OSINT events."""
        print("AI Threat Hunter: Commencing correlation analysis...")
        hunted_threats = []
        for telemetry in internal_telemetry:
            for intel in osint_data:
                if any(keyword in intel['title'].lower() for keyword in ["ransomware", "botnet", "exploit"]):
                    if "port" in telemetry.get("msg", "").lower():
                        hunted_threats.append({
                            "type": "CORRELATED_THREAT",
                            "severity": "HIGH",
                            "correlation_score": 0.89,
                            "reason": f"Global activity for '{intel['title']}' matches internal port anomaly.",
                            "timestamp": datetime.datetime.now().isoformat()
                        })
        return hunted_threats

    def analyze_malware_sample(self, file_hash: str, sandbox_output: str) -> Dict:
        """Generates AI analysis report from malware sandbox execution."""
        risk_score = random.uniform(70, 99)
        return {
            "file_hash": file_hash,
            "ai_risk_score": round(risk_score, 2),
            "threat_classification": "Trojan.Downloader",
            "capabilities": ["Network Communication", "Registry Modification", "Anti-Debugging"],
            "recommendation": "Isolate affected hosts immediately and rotate credentials for service-account-01.",
            "report_id": f"MAL-REP-{random.randint(1000, 9999)}"
        }

if __name__ == "__main__":
    analyzer = SecurityAnalyzer()
    print("--- Basic Summary ---")
    print(analyzer.generate_summary([{"title": "Unauthorized Access Attempt"}]))

    print("\n--- Threat Hunter ---")
    internal = [{"msg": "High traffic on port 4444"}]
    osint = [{"title": "Botnet-Alpha active on port 4444"}]
    print(analyzer.autonomous_threat_hunter(internal, osint))

    print("\n--- Malware Analysis ---")
    print(analyzer.analyze_malware_sample("a1b2c3d4", "Connection to 103.22.XX.YY detected."))

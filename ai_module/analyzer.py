import datetime
import random
import re
from typing import List, Dict, Optional, Any

class SecurityAnalyzer:
    THREAT_TACTICS = {
        "ransomware": {
            "tactics": ["Data Encryption", "Exfiltration", "Inhibition of Recovery"],
            "actions": [
                {"priority": "HIGH", "task": "Isolate affected clusters", "action": "ISOLATE"},
                {"priority": "HIGH", "task": "Disable VSS deletion scripts", "action": "BLOCK"}
            ],
            "default_severity": "CRITICAL"
        },
        "botnet": {
            "tactics": ["Command and Control", "Resource Hijacking"],
            "actions": [
                {"priority": "MEDIUM", "task": "Block C2 IP at firewall", "action": "FW_BLOCK"},
                {"priority": "LOW", "task": "Identify infected endpoints", "action": "SCAN"}
            ],
            "default_severity": "HIGH"
        },
        "phishing": {
            "tactics": ["Credential Access", "Initial Access"],
            "actions": [
                {"priority": "HIGH", "task": "Reset credentials for affected users", "action": "RESET_PW"},
                {"priority": "MEDIUM", "task": "Purge email from inboxes", "action": "PURGE_MAIL"}
            ],
            "default_severity": "MEDIUM"
        },
        "exploit": {
            "tactics": ["Execution", "Privilege Escalation"],
            "actions": [
                {"priority": "HIGH", "task": "Apply emergency patches", "action": "PATCH"},
                {"priority": "MEDIUM", "task": "Restrict access to vulnerable service", "action": "RESTRICT"}
            ],
            "default_severity": "HIGH"
        }
    }

    def __init__(self, model_name: str = "AIP-GPT-2"):
        self.model_name = model_name
        self.version = "1.1.0"

    def normalize_log(self, raw_log: Dict) -> Dict:
        """Converts raw logs into a unified schema for analysis."""
        return {
            "timestamp": raw_log.get("timestamp", datetime.datetime.now().isoformat()),
            "source": raw_log.get("source_ip", raw_log.get("ip", "0.0.0.0")),
            "event_type": raw_log.get("type", "unknown"),
            "raw_message": raw_log.get("msg", ""),
            "normalized": True
        }

    def calculate_risk_score(self, threats: List[Dict], internal_anomalies: List[Dict]) -> float:
        """Calculates a composite risk score (0-100)."""
        base_threat = sum(t.get("severity_score", 0) for t in threats)
        internal_factor = len(internal_anomalies) * 2.5
        score = min(100.0, base_threat + internal_factor)
        return round(score, 2)

    def generate_summary(self, alerts: List[Dict]) -> str:
        """Simulates natural language summarization for the dashboard."""
        if not alerts:
            return "All systems stable. No significant threats detected in the last 24 hours."

        count = len(alerts)
        critical = [a for a in alerts if a.get('severity', '').lower() in ['high', 'critical']]
        summary = f"AI Analysis: {count} active alerts detected. "
        if critical:
            summary += f"Critical focus on {critical[0].get('title')}. "
        summary += "Automated correlation indicates regional shift in attack patterns."
        return summary

    def autonomous_threat_hunter(self, internal_telemetry: List[Dict], osint_data: List[Dict]) -> List[Dict]:
        """Advanced AI Threat Hunter correlating telemetry with OSINT using IOC matching."""
        print("AI Threat Hunter: Commencing deep correlation...")
        correlated = []

        # Simple IOC extraction (IPs/Ports) from OSINT
        for intel in osint_data:
            intel_title = intel.get('title', '').lower()
            intel_body = intel.get('body', '').lower()

            # Find tactic category
            category = next((cat for cat in self.THREAT_TACTICS if cat in intel_title), None)

            for telemetry in internal_telemetry:
                tele_msg = telemetry.get('msg', '').lower()
                confidence = 0.0
                reasons = []

                # Port Correlation
                ports = re.findall(r'port\s+(\d+)', tele_msg + " " + intel_title + " " + intel_body)
                if len(ports) > 1 and ports[0] == ports[1]:
                    confidence += 0.6
                    reasons.append(f"Matching port activity ({ports[0]})")

                # Keyword Correlation
                if category and category in tele_msg:
                    confidence += 0.4
                    reasons.append(f"Matched threat category: {category}")

                if confidence >= 0.5:
                    tactic_info = self.THREAT_TACTICS.get(category, {})
                    correlated.append({
                        "type": "CORRELATED_THREAT",
                        "category": category or "unknown",
                        "severity": tactic_info.get("default_severity", "MEDIUM"),
                        "confidence_score": round(min(0.99, confidence), 2),
                        "reason": "; ".join(reasons),
                        "actions": tactic_info.get("actions", []),
                        "timestamp": datetime.datetime.now().isoformat()
                    })

        return correlated

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

    def query_response(self, query: str) -> Dict:
        """Detailed AI query response structure based on 'AI Query Results' design."""
        # Simulate query parsing
        threat_types = ["Data Exfiltration", "System Infiltration", "Lateral Movement", "Resource Hijacking"]
        confidence_scores = {tt: round(random.uniform(10, 95), 1) for tt in threat_types}

        # Sort by confidence
        sorted_scores = sorted(confidence_scores.items(), key=lambda x: x[1], reverse=True)

        return {
            "query": query,
            "status": "Complete",
            "runtime": "1.2s",
            "summary": f"My analysis of '{query}' identifies a high-confidence correlation between global ransomware trends and recent internal credential anomalies.",
            "threat_matrix": [{"type": t, "confidence": c} for t, c in sorted_scores],
            "source_attribution": [
                {"name": "Global OSINT Feed", "type": "External", "relevance": "High"},
                {"name": "Intranet Log Analyzer", "type": "Internal", "relevance": "High"},
                {"name": "User Behavior AI", "type": "AI Module", "relevance": "Medium"}
            ],
            "action_items": [
                {"priority": "HIGH", "task": "Isolate Cluster Alpha in Segment 4", "action": "ISOLATE"},
                {"priority": "MEDIUM", "task": "Reset credentials for user 'svc_backup_01'", "action": "RESET"},
                {"priority": "LOW", "task": "Enable enhanced logging for Port 8443", "action": "LOG_UP"}
            ],
            "timestamp": datetime.datetime.now().isoformat(),
            "model": self.model_name
        }

if __name__ == "__main__":
    analyzer = SecurityAnalyzer()
    print("--- Advanced Threat Hunter Test ---")
    tel = [{"msg": "High traffic on port 4444. Ransomware patterns detected."}]
    osint = [{"title": "Ransomware-Alpha active on port 4444", "body": "Targeting port 4444 specifically."}]
    results = analyzer.autonomous_threat_hunter(tel, osint)
    import json
    print(json.dumps(results, indent=2))

    print("\n--- Detailed Query Response Test ---")
    query_res = analyzer.query_response("Anomalous traffic in Sector 7")
    print(json.dumps(query_res, indent=2))

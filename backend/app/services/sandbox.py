import datetime
import random
from typing import Dict, List, Optional

class MalwareSandboxService:
    def __init__(self):
        self.common_behaviors = [
            {"type": "NETWORK", "action": "Connection to C2 server at 103.22.45.11 on Port 4444", "risk": 0.9},
            {"type": "REGISTRY", "action": "Created persistence key: HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\svchost_update", "risk": 0.8},
            {"type": "FILESYSTEM", "action": "Dropped encrypted payload in C:\\Windows\\Temp\\payload.bin", "risk": 0.7},
            {"type": "PROCESS", "action": "Injected shellcode into explorer.exe", "risk": 0.95},
            {"type": "ANTI_DEBUG", "action": "Detected IsDebuggerPresent check", "risk": 0.5}
        ]

    def analyze_sample(self, file_name: str, file_hash: str) -> Dict:
        """Simulates a full behavioral analysis in a sandbox environment."""
        print(f"[SANDBOX] Analyzing sample: {file_name} ({file_hash})...")

        # Randomly select behaviors to simulate different malware types
        num_behaviors = random.randint(2, 4)
        detected_behaviors = random.sample(self.common_behaviors, num_behaviors)

        # Calculate risk score based on behaviors
        raw_score = sum(b["risk"] for b in detected_behaviors) / num_behaviors * 100
        risk_score = round(min(99.0, raw_score + random.uniform(-5, 5)), 1)

        return {
            "analysis_id": f"MAL-{random.randint(1000, 9999)}",
            "file_metadata": {
                "name": file_name,
                "hash": file_hash,
                "timestamp": datetime.datetime.now().isoformat()
            },
            "risk_assessment": {
                "score": risk_score,
                "level": "CRITICAL" if risk_score > 80 else ("HIGH" if risk_score > 60 else "MEDIUM"),
                "classification": "Trojan.Agent.AIP" if risk_score > 70 else "Spyware.Generic"
            },
            "behaviors": detected_behaviors,
            "mitre_att&ck_mappings": [
                {"tactic": "Persistence", "technique": "T1547.001"},
                {"tactic": "Command and Control", "technique": "T1071.001"}
            ],
            "recommendations": [
                "Isolate all endpoints that have executed this file.",
                "Block C2 IP at the firewall.",
                "Rotate administrative credentials."
            ]
        }

sandbox_service = MalwareSandboxService()

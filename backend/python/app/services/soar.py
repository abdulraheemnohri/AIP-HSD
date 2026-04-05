import datetime
import json
from typing import List, Dict

class SOARPlaybookEngine:
    def __init__(self):
        self.playbooks = {
            "RANSOMWARE_CONTAINMENT": [
                {"step": 1, "action": "ISOLATE_ENDPOINT", "target": "internal_telemetry.source_ip"},
                {"step": 2, "action": "REVOKE_CLOUD_TOKENS", "target": "affected_user_id"},
                {"step": 3, "action": "SNAPSHOT_SYSTEM", "target": "internal_telemetry.source_ip"}
            ],
            "PHISHING_RESPONSE": [
                {"step": 1, "action": "BLOCK_SENDER_DOMAIN", "target": "osint.sender_domain"},
                {"step": 2, "action": "PURGE_MAIL_INBOXES", "target": "all_users"},
                {"step": 3, "action": "RESET_PASSWORD", "target": "affected_user_id"}
            ]
        }

    def execute_playbook(self, playbook_id: str, context: Dict) -> List[Dict]:
        """Simulates the execution of a SOAR playbook."""
        print(f"[SOAR] Executing Playbook: {playbook_id}...")
        steps = self.playbooks.get(playbook_id, [])
        execution_log = []

        for step in steps:
            print(f"[SOAR] Step {step['step']}: {step['action']} on {step['target']}")
            execution_log.append({
                "step": step['step'],
                "action": step['action'],
                "status": "COMPLETED",
                "timestamp": datetime.datetime.now().isoformat()
            })

        return execution_log

soar_engine = SOARPlaybookEngine()

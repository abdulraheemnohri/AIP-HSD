import datetime
import random
from typing import List, Dict

class DynamicDeceptionService:
    def __init__(self):
        self.active_decoys = [
            {"id": "decoy-srv-01", "name": "srv-prod-db-backup", "type": "DATABASE", "ip": "10.0.5.50"},
            {"id": "decoy-usr-01", "name": "admin_vault_credentials", "type": "CREDENTIAL_FILE", "path": "/etc/vault/keys.txt"}
        ]

    def deploy_new_decoy(self, type: str) -> Dict:
        """Simulates deploying a new virtual decoy to the internal network."""
        new_id = f"decoy-{random.randint(100, 999)}"
        decoy = {"id": new_id, "type": type, "status": "ACTIVE", "deployed_at": datetime.datetime.now().isoformat()}
        self.active_decoys.append(decoy)
        return decoy

    def check_decoy_alerts(self) -> List[Dict]:
        """Simulates checking if any decoys have been interacted with."""
        if random.random() > 0.8:
            return [{
                "decoy_id": "decoy-srv-01",
                "alert_type": "HONEYPOT_INTERACTION",
                "source_ip": "192.168.1.15",
                "severity": "CRITICAL",
                "timestamp": datetime.datetime.now().isoformat(),
                "details": "Unauthorized connection attempt to dummy database service."
            }]
        return []

deception_service = DynamicDeceptionService()

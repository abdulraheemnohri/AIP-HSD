import random
import time
import datetime
from typing import List, Dict

class SecuritySimulator:
    def __init__(self):
        self.threat_names = ["Ransomware-Alpha", "Botnet-Delta", "Phish-Gamma", "Exploit-Zeta", "ZeroDay-Omicron"]
        self.device_names = ["srv-web-01", "srv-db-02", "ws-admin-10", "gateway-01", "srv-app-03"]
        self.severity_levels = ["low", "medium", "high", "critical"]

    def generate_random_alert(self) -> Dict:
        """Generates a mock security alert."""
        device = random.choice(self.device_names)
        severity = random.choice(self.severity_levels)
        threat = random.choice(self.threat_names)

        return {
            "id": random.randint(100, 999),
            "title": f"Suspicious Activity: {threat}",
            "severity": severity,
            "message": f"Detected {threat} pattern on {device}. Possible lateral movement attempt.",
            "device_id": random.randint(1, 10),
            "timestamp": datetime.datetime.now()
        }

    def generate_random_threat(self) -> Dict:
        """Generates a mock global threat."""
        name = random.choice(self.threat_names)
        location = random.choice(["USA", "China", "Russia", "Germany", "Brazil", "France"])

        return {
            "id": random.randint(100, 999),
            "name": name,
            "type": random.choice(["malware", "phishing", "ransomware", "ddos", "exploit"]),
            "source": "OSINT-Simulator",
            "risk_score": round(random.uniform(20.0, 98.0), 2),
            "location": location,
            "description": f"New variant of {name} detected in {location} region.",
            "timestamp": datetime.datetime.now()
        }

    def generate_summary(self, alert_count: int) -> Dict:
        """Generates a mock dashboard summary."""
        return {
            "global_threat_level": round(random.uniform(0.6, 0.95), 2),
            "internal_threat_level": round(random.uniform(0.1, 0.4), 2),
            "network_health": round(random.uniform(0.95, 1.0), 4),
            "active_alerts": alert_count
        }

if __name__ == "__main__":
    simulator = SecuritySimulator()
    print("--- Simulating Alert ---")
    print(simulator.generate_random_alert())
    print("\n--- Simulating Global Threat ---")
    print(simulator.generate_random_threat())

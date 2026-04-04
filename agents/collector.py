import os
import platform
import socket
import json
import datetime
import requests
import time

class SystemCollector:
    def __init__(self, server_url: str = "http://localhost:8000/api"):
        self.server_url = server_url
        self.os = platform.system()
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)

    def get_system_info(self):
        """Collects basic system telemetry."""
        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "os": f"{self.os} {platform.release()}",
            "role": "Endpoint",
            "last_scan": datetime.datetime.now().isoformat(),
            "status": "online"
        }

    def collect_logs(self):
        """Simulates log collection from system files."""
        return [
            {"timestamp": datetime.datetime.now().isoformat(), "type": "auth", "msg": "Failed login attempt from 10.0.0.5"},
            {"timestamp": datetime.datetime.now().isoformat(), "type": "network", "msg": "Unusual outbound connection detected on port 4444"}
        ]

    def send_to_backend(self, endpoint: str, data: dict):
        """Sends collected telemetry to the backend API."""
        try:
            url = f"{self.server_url}/{endpoint}"
            response = requests.post(url, json=data, timeout=5)
            return response.status_code == 200
        except Exception as e:
            print(f"Failed to send data: {e}")
            return False

    def run_cycle(self):
        """Executes a single collection and reporting cycle."""
        info = self.get_system_info()
        logs = self.collect_logs()
        payload = {"system_info": info, "logs": logs}
        return payload

if __name__ == "__main__":
    collector = SystemCollector()
    data = collector.run_cycle()
    print(json.dumps(data, indent=2))

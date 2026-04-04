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
        """Collects basic system telemetry including screen resolution."""
        resolution = "1920x1080" # Default/Fallback
        try:
            # Simulate screen resolution capture
            if platform.system() == "Linux":
                resolution = "2560x1440 (Linux Workstation)"
            elif platform.system() == "Windows":
                resolution = "1920x1080 (Windows PC)"
            elif platform.system() == "Darwin":
                resolution = "2880x1800 (macOS Retina)"
        except:
            pass

        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "os": f"{self.os} {platform.release()}",
            "role": "Endpoint",
            "last_scan": datetime.datetime.now().isoformat(),
            "status": "online",
            "screen_resolution": resolution
        }

    def collect_logs(self):
        """Simulates log collection from system files."""
        return [
            {"timestamp": datetime.datetime.now().isoformat(), "type": "auth", "msg": "Failed login attempt from 10.0.0.5"},
            {"timestamp": datetime.datetime.now().isoformat(), "type": "network", "msg": "Unusual outbound connection detected on port 4444"}
        ]

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

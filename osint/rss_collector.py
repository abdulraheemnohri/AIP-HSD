import time
import datetime
from typing import List, Dict

class RSSCollector:
    def __init__(self, feeds: List[str] = None):
        self.feeds = feeds or [
            "https://www.us-cert.gov/ncas/alerts.xml",
            "https://krebsonsecurity.com/feed/",
            "https://threatpost.com/feed/"
        ]

    def fetch_latest(self) -> List[Dict]:
        """Simulates fetching latest security alerts from RSS feeds."""
        print(f"Fetching from {len(self.feeds)} RSS feeds...")
        # Mock data
        return [
            {
                "title": "New Ransomware Variant 'Delta' Targeting Critical Infrastructure",
                "link": "https://example.com/alert/delta",
                "source": "US-CERT",
                "published": datetime.datetime.now().isoformat()
            },
            {
                "title": "Zero-day vulnerability in popular web server discovered",
                "link": "https://example.com/blog/zero-day",
                "source": "KrebsonSecurity",
                "published": datetime.datetime.now().isoformat()
            }
        ]

if __name__ == "__main__":
    collector = RSSCollector()
    alerts = collector.fetch_latest()
    for alert in alerts:
        print(f"[{alert['source']}] {alert['title']}")

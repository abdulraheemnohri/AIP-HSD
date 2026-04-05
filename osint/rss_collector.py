import time
import datetime
from typing import List, Dict

class RSSCollector:
    def __init__(self, feeds: List[str] = None):
        self.feeds = feeds or [
            "https://www.us-cert.gov/ncas/alerts.xml",
            "https://krebsonsecurity.com/feed/"
        ]

    def fetch_latest(self, keywords: List[str] = None) -> List[Dict]:
        """Fetches latest alerts, optionally filtering by keywords."""
        print(f"RSS: Fetching intelligence (Keywords: {keywords or 'All'})...")
        mock_data = [
            {"title": "New Ransomware Variant 'Delta'", "source": "US-CERT", "published": datetime.datetime.now().isoformat()},
            {"title": "Zero-day vulnerability in web server", "source": "KrebsonSecurity", "published": datetime.datetime.now().isoformat()}
        ]

        if not keywords:
            return mock_data

        return [item for item in mock_data if any(kw.lower() in item['title'].lower() for kw in keywords)]

if __name__ == "__main__":
    collector = RSSCollector()
    print(collector.fetch_latest(["Ransomware"]))

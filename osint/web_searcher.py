from typing import List, Dict

class WebSearcher:
    def __init__(self, engine: str = "duckduckgo"):
        self.engine = engine

    def search_threat(self, query: str, limit: int = 5) -> List[Dict]:
        """Simulates searching the web for specific threat intelligence with limits."""
        print(f"Search: Querying '{query}' via {self.engine} (Limit: {limit})...")
        return [
            {"title": f"Intelligence for {query} - Result {i+1}", "url": f"https://example.com/{query}/{i+1}"}
            for i in range(limit)
        ]

if __name__ == "__main__":
    searcher = WebSearcher()
    print(searcher.search_threat("Exploit-Zeta", 2))

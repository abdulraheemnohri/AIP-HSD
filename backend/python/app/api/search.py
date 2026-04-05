from fastapi import APIRouter, Depends
from typing import Dict, List
from datetime import datetime
from .auth import get_current_user, User
from osint.web_searcher import WebSearcher

router = APIRouter()
web_searcher = WebSearcher()

@router.get("/")
def global_search(query: str, current_user: User = Depends(get_current_user)):
    """Aggregates results from OSINT and Internal sources."""
    print(f"[SEARCH] [{current_user.tenant_id}] Searching for: {query}")

    # 1. External OSINT Search
    osint_results = web_searcher.search_threat(query, limit=3)

    # 2. Internal Context (Simulated)
    internal_hits = [
        {"source": "Internal Logs", "match": f"Telemetry entry matching '{query}' found in srv-web-01."},
        {"source": "Alerts", "match": f"Resolved alert for {query} on {datetime.now().date()}"}
    ]

    return {
        "query": query,
        "tenant_id": current_user.tenant_id,
        "external_intel": osint_results,
        "internal_context": internal_hits,
        "timestamp": datetime.now()
    }

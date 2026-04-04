from fastapi import APIRouter
from typing import List, Dict
from datetime import datetime

router = APIRouter()

@router.get("/data")
def get_attack_map_data():
    """Fetch live cyber attack data for the map."""
    return {
        "timestamp": datetime.now(),
        "attacks": [
            {"source": "CN", "target": "US", "type": "DDOS", "severity": "HIGH", "lat": 35.86, "lon": 104.19},
            {"source": "RU", "target": "DE", "type": "EXPLOIT", "severity": "MEDIUM", "lat": 61.52, "lon": 105.31},
            {"source": "BR", "target": "FR", "type": "PHISHING", "severity": "LOW", "lat": -14.23, "lon": -51.92}
        ]
    }

@router.get("/countries")
def get_country_summaries():
    """Fetch risk level summary per country."""
    return [
        {"country": "USA", "risk_level": "MEDIUM", "score": 45},
        {"country": "CHN", "risk_level": "HIGH", "score": 82},
        {"country": "RUS", "risk_level": "HIGH", "score": 78},
        {"country": "DEU", "risk_level": "LOW", "score": 15}
    ]

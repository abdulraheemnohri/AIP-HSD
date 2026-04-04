from fastapi import APIRouter
from typing import List
from datetime import datetime
from ..schemas.schemas import Threat, ThreatType
from ..core.simulator import SecuritySimulator

router = APIRouter()
simulator = SecuritySimulator()

@router.get("/", response_model=List[Threat])
def get_threats():
    """Fetch global threats from simulated OSINT/Intelligence feeds."""
    threats = []
    for _ in range(5):
        t = simulator.generate_random_threat()
        threats.append(Threat(
            id=t["id"],
            name=t["name"],
            type=t["type"],
            source=t["source"],
            risk_score=t["risk_score"],
            location=t["location"],
            description=t["description"],
            timestamp=t["timestamp"]
        ))
    return threats

@router.get("/{threat_id}", response_model=Threat)
def get_threat(threat_id: int):
    t = simulator.generate_random_threat()
    return Threat(**t, id=threat_id)

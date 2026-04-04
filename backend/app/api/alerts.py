from fastapi import APIRouter
from typing import List
from datetime import datetime
from ..schemas.schemas import Alert, Severity
from ..core.simulator import SecuritySimulator

router = APIRouter()
simulator = SecuritySimulator()

@router.get("/", response_model=List[Alert])
def get_alerts():
    """Fetch recent live alerts from simulated internal monitoring."""
    alerts = []
    for _ in range(10):
        a = simulator.generate_random_alert()
        alerts.append(Alert(
            id=a["id"],
            title=a["title"],
            severity=a["severity"],
            message=a["message"],
            device_id=a["device_id"],
            timestamp=a["timestamp"]
        ))
    return alerts

@router.post("/")
def create_alert(alert: Alert):
    return {"status": "success", "alert_id": alert.id}

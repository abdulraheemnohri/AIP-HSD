from fastapi import APIRouter, Depends
from typing import Dict, List
from datetime import datetime
from .auth import get_current_user, User

router = APIRouter()

@router.get("/status", response_model=Dict)
def get_compliance_status(current_user: User = Depends(get_current_user)):
    """Fetch simulated compliance status for major security standards."""
    return {
        "timestamp": datetime.now(),
        "standards": [
            {"name": "ISO 27001", "status": "COMPLIANT", "score": 98.5, "last_audit": "2024-03-15"},
            {"name": "PCI-DSS v4.0", "status": "VULNERABLE", "score": 72.0, "last_audit": "2024-04-01", "remediation": "Update encryption for Segment 4"},
            {"name": "SOC2 Type II", "status": "COMPLIANT", "score": 100.0, "last_audit": "2024-01-10"},
            {"name": "GDPR", "status": "IN_REVIEW", "score": 85.0, "last_audit": "2024-04-04"}
        ]
    }

@router.get("/reports")
def get_compliance_reports(current_user: User = Depends(get_current_user)):
    return [
        {"id": "ISO-2024-Q1", "date": "2024-03-20", "type": "INTERNAL_AUDIT", "summary": "Full compliance across all domains."},
        {"id": "PCI-2024-04", "date": "2024-04-02", "type": "VULNERABILITY_SCAN", "summary": "Detected non-compliant encryption in Segment 4."}
    ]

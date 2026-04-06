from fastapi import APIRouter, Depends
from typing import List, Dict
from .auth import get_current_user, User
from ..services.reporting import report_generator

router = APIRouter()

@router.post("/generate/pdf")
def create_pdf_report(findings: List[Dict], current_user: User = Depends(get_current_user)):
    return report_generator.generate_pdf_summary(current_user.tenant_id, findings)

@router.get("/list")
def list_reports(current_user: User = Depends(get_current_user)):
    return [
        {"id": "REP-PDF-001", "date": "2024-04-01", "type": "MONTHLY_SUMMARY"},
        {"id": "REP-CSV-002", "date": "2024-04-03", "type": "INCIDENT_EXPORT"}
    ]

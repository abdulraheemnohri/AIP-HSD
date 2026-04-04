from fastapi import APIRouter, Depends
from typing import Dict
from .auth import get_current_user, User
from ..services.updater import updater_service

router = APIRouter()

@router.get("/status", response_model=Dict)
def get_update_status(current_user: User = Depends(get_current_user)):
    """Fetch current version and check for GitHub releases."""
    return updater_service.check_for_updates()

@router.post("/apply")
def apply_update(current_user: User = Depends(get_current_user)):
    """Manually trigger the GitHub update and restart process."""
    if current_user.role != "admin":
        return {"error": "Admin role required for automatic updates."}
    return updater_service.perform_automatic_update()

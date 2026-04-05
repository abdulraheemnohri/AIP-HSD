from fastapi import APIRouter
from .threats import router as threats_router
from .devices import router as devices_router
from .alerts import router as alerts_router
from .query import router as query_router
from .threat_hunter import router as threat_hunter_router
from .attack_map import router as attack_map_router
from .malware_sandbox import router as malware_sandbox_router
from .auth import router as auth_router
from .compliance import router as compliance_router
from .updater import router as updater_router
from .cti import router as cti_router
from .search import router as search_router
from .settings import router as settings_router
from .reports import router as reports_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(threats_router, prefix="/threats", tags=["Threats"])
router.include_router(devices_router, prefix="/devices", tags=["Devices"])
router.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
router.include_router(query_router, prefix="/query", tags=["AI Query"])
router.include_router(threat_hunter_router, prefix="/threat-hunter", tags=["AI Threat Hunter"])
router.include_router(attack_map_router, prefix="/attack-map", tags=["Real-time Attack Map"])
router.include_router(malware_sandbox_router, prefix="/malware-sandbox", tags=["AI Malware Sandbox"])
router.include_router(compliance_router, prefix="/compliance", tags=["Compliance Monitoring"])
router.include_router(updater_router, prefix="/updater", tags=["Auto-Updater"])
router.include_router(cti_router, prefix="/cti", tags=["Threat Intelligence Sharing"])
router.include_router(search_router, prefix="/search", tags=["Global Search"])
router.include_router(settings_router, prefix="/settings", tags=["Platform Settings"])
router.include_router(reports_router, prefix="/reports", tags=["Security Reporting"])

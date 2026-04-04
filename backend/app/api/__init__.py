from fastapi import APIRouter
from .threats import router as threats_router
from .devices import router as devices_router
from .alerts import router as alerts_router
from .query import router as query_router
from .threat_hunter import router as threat_hunter_router
from .attack_map import router as attack_map_router
from .malware_sandbox import router as malware_sandbox_router

router = APIRouter()
router.include_router(threats_router, prefix="/threats", tags=["Threats"])
router.include_router(devices_router, prefix="/devices", tags=["Devices"])
router.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
router.include_router(query_router, prefix="/query", tags=["AI Query"])
router.include_router(threat_hunter_router, prefix="/threat-hunter", tags=["AI Threat Hunter"])
router.include_router(attack_map_router, prefix="/attack-map", tags=["Real-time Attack Map"])
router.include_router(malware_sandbox_router, prefix="/malware-sandbox", tags=["AI Malware Sandbox"])

from fastapi import APIRouter
from typing import List
from datetime import datetime
from ..schemas.schemas import Device, DeviceStatus

router = APIRouter()

@router.get("/", response_model=List[Device])
def get_devices():
    """Fetch simulated internal device statuses."""
    return [
        Device(id=1, ip_address="192.168.1.10", os="Ubuntu 22.04", hostname="srv-web-01", role="Web Server", status=DeviceStatus.ONLINE, risk_score=5.0, last_scan=datetime.now()),
        Device(id=2, ip_address="192.168.1.25", os="Windows Server 2022", hostname="dc-main-01", role="Domain Controller", status=DeviceStatus.VULNERABLE, risk_score=45.2, last_scan=datetime.now()),
        Device(id=3, ip_address="192.168.1.50", os="Ubuntu 20.04", hostname="srv-db-02", role="Database Server", status=DeviceStatus.ONLINE, risk_score=10.0, last_scan=datetime.now()),
        Device(id=4, ip_address="192.168.2.100", os="CentOS 7", hostname="gateway-01", role="Network Gateway", status=DeviceStatus.ONLINE, risk_score=2.0, last_scan=datetime.now()),
        Device(id=5, ip_address="192.168.1.75", os="Windows 11", hostname="ws-admin-10", role="Admin Workstation", status=DeviceStatus.ONLINE, risk_score=8.5, last_scan=datetime.now())
    ]

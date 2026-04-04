from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime
from enum import Enum

class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ThreatType(str, Enum):
    MALWARE = "malware"
    PHISHING = "phishing"
    RANSOMWARE = "ransomware"
    DDOS = "ddos"
    EXPLOIT = "exploit"
    OTHER = "other"

class DeviceStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    VULNERABLE = "vulnerable"
    COMPROMISED = "compromised"

# Threat Schemas
class ThreatBase(BaseModel):
    name: str
    type: str # More flexible
    source: str
    risk_score: float = Field(..., ge=0, le=100)
    location: Optional[str] = None
    description: Optional[str] = None

class ThreatCreate(ThreatBase):
    pass

class Threat(ThreatBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Device Schemas
class DeviceBase(BaseModel):
    ip_address: str
    os: str
    hostname: str
    role: Optional[str] = None
    status: DeviceStatus = DeviceStatus.ONLINE
    risk_score: float = Field(default=0.0, ge=0, le=100)

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    last_scan: Optional[datetime] = None

    class Config:
        from_attributes = True

# Alert Schemas
class AlertBase(BaseModel):
    title: str
    severity: str # More flexible for simulator
    message: str
    device_id: Optional[int] = None
    threat_id: Optional[int] = None

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# AI Query Schemas
class AIQueryRequest(BaseModel):
    query_text: str

class AIQueryResponse(BaseModel):
    id: int
    query_text: str
    ai_response: str
    sources: List[Any] = []
    timestamp: datetime

    class Config:
        from_attributes = True

# Dashboard Summary Schema
class DashboardSummary(BaseModel):
    global_threat_level: float
    internal_threat_level: float
    network_health: float
    error_count: int
    active_alerts: int

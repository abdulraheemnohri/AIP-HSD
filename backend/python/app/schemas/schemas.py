from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime
from enum import Enum

class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class DeviceStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    VULNERABLE = "vulnerable"
    COMPROMISED = "compromised"

# Multi-Tenant Base Schema
class TenantModel(BaseModel):
    tenant_id: str = Field(..., description="Unique identifier for the organization/tenant")

# Device Schemas
class DeviceBase(BaseModel):
    ip_address: str
    os: str
    hostname: str
    role: Optional[str] = None
    status: DeviceStatus = DeviceStatus.ONLINE
    risk_score: float = Field(default=0.0, ge=0, le=100)
    screen_resolution: Optional[str] = None

class Device(DeviceBase, TenantModel):
    id: int
    last_scan: Optional[datetime] = None

    class Config:
        from_attributes = True

# Threat Schemas
class ThreatBase(BaseModel):
    name: str
    type: str
    source: str
    risk_score: float = Field(..., ge=0, le=100)
    location: Optional[str] = None
    description: Optional[str] = None

class Threat(ThreatBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Alert Schemas
class AlertBase(BaseModel):
    title: str
    severity: str
    message: str
    device_id: Optional[int] = None

class Alert(AlertBase, TenantModel):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# AI Query Schemas
class AIQueryRequest(BaseModel):
    query_text: str

class AIQueryResponse(BaseModel, TenantModel):
    id: int
    query_text: str
    ai_response: str
    sources: List[Any] = []
    timestamp: datetime

    class Config:
        from_attributes = True

# Dashboard Summary Schema
class DashboardSummary(BaseModel, TenantModel):
    global_threat_level: float
    internal_threat_level: float
    network_health: float
    active_alerts: int

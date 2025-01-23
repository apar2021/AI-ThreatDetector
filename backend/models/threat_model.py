# backend/models/threat_model.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime

class ThreatSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ThreatType(str, Enum):
    NETWORK_SCAN = "network_scan"
    DDOS = "ddos"
    MALWARE = "malware"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    ANOMALOUS_TRAFFIC = "anomalous_traffic"

class ThreatDetection(BaseModel):
    """
    Detailed threat detection model
    """
    threat_id: str = Field(..., description="Unique threat identifier")
    type: ThreatType
    severity: ThreatSeverity
    timestamp: datetime
    source_ip: str
    destination_ip: str
    description: str
    
    class Config:
        schema_extra = {
            "example": {
                "threat_id": "THREAT-2024-001",
                "type": "network_scan",
                "severity": "high",
                "timestamp": "2024-01-23T10:45:00",
                "source_ip": "185.143.223.42",
                "destination_ip": "192.168.1.100",
                "description": "Potential port scanning detected from suspicious IP"
            }
        }

class ThreatSummary(BaseModel):
    """
    Aggregated threat summary
    """
    total_threats: int
    threats_by_severity: Dict[ThreatSeverity, int]
    top_threats: List[ThreatDetection]
    overall_risk_score: float = Field(
        ..., 
        ge=0, 
        le=1, 
        description="Normalized risk score between 0 and 1"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "total_threats": 5,
                "threats_by_severity": {
                    "low": 2,
                    "medium": 1,
                    "high": 2,
                    "critical": 0
                },
                "overall_risk_score": 0.65
            }
        }
# backend/models/packet_model.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class PacketInfo(BaseModel):
    """
    Detailed packet information model
    """
    timestamp: datetime
    protocol: str
    source_ip: str
    destination_ip: str
    packet_length: int
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2024-01-23T10:30:00",
                "protocol": "TCP",
                "source_ip": "192.168.1.100",
                "destination_ip": "8.8.8.8",
                "packet_length": 1024
            }
        }

class PcapAnalysisResponse(BaseModel):
    """
    Comprehensive PCAP analysis response model
    """
    total_packets: int = Field(..., description="Total number of packets processed")
    unique_protocols: List[str] = Field(default_factory=list)
    traffic_data: List[PacketInfo] = Field(default_factory=list)
    protocol_distribution: Dict[str, int] = Field(default_factory=dict)
    anomaly_score: Optional[float] = Field(None, description="Overall network anomaly score")
    
    class Config:
        schema_extra = {
            "example": {
                "total_packets": 5000,
                "unique_protocols": ["TCP", "UDP", "ICMP"],
                "protocol_distribution": {
                    "TCP": 3000,
                    "UDP": 1500,
                    "ICMP": 500
                },
                "anomaly_score": 0.75
            }
        }
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Packet data table
class Packet(Base):
    __tablename__ = 'packets'
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    src_ip = Column(String)
    dst_ip = Column(String)
    protocol = Column(String)
    length = Column(Integer)
    is_anomalous = Column(Integer, default=0)  # 0 = normal, 1 = anomalous

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./pcap_traffic.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables (if not exists)
Base.metadata.create_all(bind=engine)

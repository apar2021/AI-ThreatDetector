# backend/config.py
from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    """
    Application configuration management
    """
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI Cybersecurity Threat Detector"
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    
    # Machine Learning Model Paths
    RL_MODEL_PATH: str = "ml_models/rl_cybersecurity_model.pkl"
    
    # Threat Detection Configurations
    THREAT_THRESHOLD: int = 1000
    PROTOCOL_RISK_LEVELS: dict = {
        'TCP': 'high',
        'UDP': 'medium',
        'ICMP': 'low'
    }
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    
    # Performance Limits
    MAX_UPLOAD_SIZE: int = 100 * 1024 * 1024  # 100 MB
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create settings instance
settings = Settings()
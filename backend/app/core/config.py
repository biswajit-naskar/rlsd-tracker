from pydantic_settings import BaseSettings 
from typing import List 
 
class Settings(BaseSettings): 
    APP_NAME: str = "RLSD-Tracker" 
    APP_VERSION: str = "1.0.0" 
    ENVIRONMENT: str = "development" 
    DEBUG: bool = True 
    SECRET_KEY: str 
    HOST: str = "0.0.0.0" 
    PORT: int = 8000 
    RELOAD: bool = True 
    DATABASE_URL: str 
    JWT_SECRET_KEY: str 
    JWT_ALGORITHM: str = "HS256" 
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"] 
    CORS_ALLOW_CREDENTIALS: bool = True 
    MAX_UPLOAD_SIZE: int = 10485760 
    UPLOAD_DIR: str = "./uploads" 
    LOG_LEVEL: str = "INFO" 
 
    class Config: 
        env_file = ".env" 
        env_file_encoding = "utf-8" 
        extra = "ignore" 
 
settings = Settings() 

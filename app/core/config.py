from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "assessiq"
    
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000", 
        "http://127.0.0.1:3000",
    ]

    class Config:
        env_file = ".env"


settings = Settings()
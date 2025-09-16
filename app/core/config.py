from pydantic import BaseSettings
from pydantic import Field
from typing import List
from typing import Optional


class Settings(BaseSettings):
    """Centralized app settings loaded from environment variables (.env)."""
    #model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    APP_NAME: str = Field(default="Professor Project API")
    APP_ENV: str = Field(default="dev")
    APP_VERSION: str = Field(default="0.1.0")
    API_PREFIX: str = Field(default="/api")

    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    CORS_ORIGINS: List[str] = Field(default=["http://localhost:5173", "http://localhost:3000"])

    API_KEY: str = Field(default="dev-secret-key-change-me")

    DATABASE_URL: Optional[str] = None
    REDIS_URL: Optional[str] = None

settings = Settings()

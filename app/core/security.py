from fastapi import Header, HTTPException, status, Security
from typing import Optional
from app.core.config import settings

def get_api_key(x_api_key: Optional[str] = Header(default=None)):
    """Simple header-based API key auth."""
    if settings.API_KEY and x_api_key == settings.API_KEY:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing X-API-Key",
    )

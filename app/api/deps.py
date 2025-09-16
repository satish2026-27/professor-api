from fastapi import Depends
from app.core.config import settings
from app.core.security import get_api_key

def auth_guard(_: bool = Depends(get_api_key)):
    return True

def get_settings():
    return settings

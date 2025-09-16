from fastapi import APIRouter, Depends
from app.api.deps import get_settings

router = APIRouter(tags=["meta"])

@router.get("/health")
def healthcheck():
    return {"status": "healthy"}

@router.get("/version")
def version(settings = Depends(get_settings)):
    return {"app": settings.APP_NAME, "version": settings.APP_VERSION, "env": settings.APP_ENV}

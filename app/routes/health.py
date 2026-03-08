from fastapi import APIRouter
from datetime import datetime
from app.config import settings

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.APP_ENV,
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
from .healthz import router as healthz_router
from app.session.endpoint import router as session_router

from fastapi import APIRouter


router = APIRouter()
router.include_router(healthz_router, prefix="/healthz", tags=["Healthz"])
router.include_router(session_router, prefix="/session", tags=["Session"])

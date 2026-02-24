from fastapi import APIRouter
from app.session import service
from livekit import api
from core.livekit_service import get_livekit_client
from fastapi import Depends

router = APIRouter()


@router.get("")
async def get_session(client: api.LiveKitAPI = Depends(get_livekit_client)):
    return await service.get_session(client)

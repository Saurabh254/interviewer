from fastapi import APIRouter, Depends, HTTPException, Query
from livekit import api

from app.session import service
from core.livekit_service import get_livekit_client
from core.exceptions import LivekitException

router = APIRouter()


@router.post("")
async def create_session(
    participant_name: str = Query(default="Candidate", description="Name of the participant"),
    client: api.LiveKitAPI = Depends(get_livekit_client),
):
    """Create a new interview session and return connection details."""
    try:
        return await service.create_interview_session(client, participant_name)
    except LivekitException as e:
        raise HTTPException(status_code=503, detail=f"LiveKit service error: {e.message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create interview session")

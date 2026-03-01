from core.livekit_service import create_room, generate_access_token
from config import settings
from livekit import api


async def create_interview_session(client: api.LiveKitAPI, participant_name: str = "Candidate"):
    """Create a new interview session with room and access token."""
    room = await create_room(client)

    # Generate access token for the participant
    access_token = generate_access_token(
        room_name=room.name,
        participant_name=participant_name,
    )

    return {
        "session_id": room.sid,
        "room_name": room.name,
        "access_token": access_token,
        "livekit_url": settings.LIVEKIT_URL,
        "status": "active",
    }

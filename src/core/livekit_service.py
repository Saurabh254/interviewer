import uuid
from livekit import api
from livekit.api import CreateRoomRequest, AccessToken, VideoGrants
from config import settings


async def get_livekit_client():
    async with api.LiveKitAPI(
        url=settings.LIVEKIT_URL,
        api_key=settings.LIVEKIT_API_KEY,
        api_secret=settings.LIVEKIT_API_SECRET,
    ) as lkapi:
        yield lkapi


def generate_room_name() -> str:
    """Generate a unique room name for each interview session."""
    return f"interview-{uuid.uuid4().hex[:12]}"


async def create_room(lkapi: api.LiveKitAPI, room_name: str | None = None):
    """Create a new LiveKit room for an interview session."""
    if room_name is None:
        room_name = generate_room_name()

    room = await lkapi.room.create_room(
        CreateRoomRequest(
            name=room_name,
            empty_timeout=10 * 60,  # 10 minutes
            max_participants=2,  # interviewer AI + candidate
        )
    )
    return room


def generate_access_token(
    room_name: str,
    participant_name: str,
    participant_identity: str | None = None,
) -> str:
    """Generate an access token for a participant to join a room."""
    if participant_identity is None:
        participant_identity = f"user-{uuid.uuid4().hex[:8]}"

    token = AccessToken(
        api_key=settings.LIVEKIT_API_KEY,
        api_secret=settings.LIVEKIT_API_SECRET,
    )
    token.with_identity(participant_identity)
    token.with_name(participant_name)
    token.with_grants(
        VideoGrants(
            room_join=True,
            room=room_name,
        )
    )

    return token.to_jwt()

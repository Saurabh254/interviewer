from core.livekit_service import create_room
from livekit import api


async def get_session(client: api.LiveKitAPI):
    room = await create_room(client, "djosjdf")

    return {
        "session_id": room.sid,
        "room_name": room.name,
        "status": "active",
    }

from livekit import api
from livekit.api import CreateRoomRequest
from config import settings


async def get_livekit_client():
    async with api.LiveKitAPI(
        url=settings.LIVEKIT_URL,
        api_key=settings.LIVEKIT_API_KEY,
        api_secret=settings.LIVEKIT_API_SECRET,
    ) as lkapi:
        yield lkapi


async def create_room(lkapi: api.LiveKitAPI, room_name: str):
    room = await lkapi.room.create_room(
        CreateRoomRequest(
            name=room_name,
            empty_timeout=10 * 60,
            max_participants=1,
        )
    )
    return room


async def get_session():
    async for client in get_livekit_client():
        print(client)
        room = await create_room(client, "djosjdf")

        return {
            "session_id": room.sid,
            "room_name": room.name,
            "status": "active",
        }

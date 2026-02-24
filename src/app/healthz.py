from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def healthz(): 
  return {"status": "ok"}
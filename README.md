# Interviewer

AI-powered interview platform using FastAPI and LiveKit for real-time audio/video sessions.

## Features

- Real-time interview sessions via LiveKit
- Automatic room creation with unique identifiers
- Access token generation for secure participant access
- Structured logging with correlation IDs

## Project Structure

| Path | Description |
| --- | --- |
| `src/main.py` | FastAPI application entry point |
| `src/config.py` | Environment configuration (pydantic-settings) |
| `src/app/session/` | Session creation endpoints and services |
| `src/app/common/` | Shared utilities (logging, etc.) |
| `src/core/` | Core services (LiveKit integration) |

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Configure environment variables in `.env`:
```
LIVEKIT_URL=wss://your-livekit-server
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret
ENV=dev
```

3. Run the server:
```bash
uv run uvicorn src.main:app --reload
```

## API Endpoints

- `POST /api/session?participant_name=Name` - Create a new interview session
- `GET /api/healthz` - Health check

## Response Example

```json
{
  "session_id": "RM_xxxxx",
  "room_name": "interview-a1b2c3d4e5f6",
  "access_token": "eyJ...",
  "livekit_url": "interview-a1b2c3d4e5f6",
  "status": "active"
}
```

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.common.logging import configure
from app.exception_handler import add_exception_handler
from app.middleware import add_http_log_middleware
from app.api import router as api_router
import structlog


logger = structlog.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure()
    logger.info("Starting up the AI Interview API...")
    yield
    logger.info("Shutting down the AI Interview API...")


app = FastAPI(
    title="AI Interview API",
    description="An API for conducting AI interviews, allowing users to ask questions and receive responses from an AI model.",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(api_router, prefix="/api")
add_http_log_middleware(app)
add_exception_handler(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

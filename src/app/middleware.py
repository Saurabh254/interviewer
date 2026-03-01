import time
from starlette.middleware.base import BaseHTTPMiddleware
import structlog

from app.common.logging import generate_correlation_id

logger = structlog.getLogger(__name__)


def add_http_log_middleware(app):

    class HTTPLogMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            correlation_id = (
                request.headers.get("x-correlation-id") or generate_correlation_id()
            )
            logger.info(f"Incoming request: {request.method} {request.url}", extra={"correlation_id": correlation_id})

            structlog.contextvars.bind_contextvars(
                correlation_id=correlation_id,
                method=request.method,
                path=request.url.path,
            )

            start_time = time.time()
            try:
                response = await call_next(request)
            except Exception as exc:
                duration_ms = round((time.time() - start_time) * 1000, 2)

                logger.exception(
                    "http_request_failed", duration_ms=duration_ms, exc_info=exc, extra={"correlation_id": correlation_id}
                )

                structlog.contextvars.clear_contextvars()
                raise

            duration_ms = round((time.time() - start_time) * 1000, 2)

            logger.info(
                "http_request_completed",
                status_code=response.status_code,
                duration_ms=duration_ms,
                correlation_id=correlation_id,
            )
            response.headers["x-correlation-id"] = correlation_id
            response.headers["X-Process-Time"] = str(duration_ms)
            structlog.contextvars.clear_contextvars()
            return response

    app.add_middleware(HTTPLogMiddleware)

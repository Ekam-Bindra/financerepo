from collections.abc import Awaitable, Callable
from uuid import UUID, uuid4

from fastapi import Request, Response

from equity_research_api.logging import request_id_context

RequestHandler = Callable[[Request], Awaitable[Response]]


def _request_id(value: str | None) -> str:
    if value is None:
        return str(uuid4())
    try:
        return str(UUID(value))
    except ValueError:
        return str(uuid4())


async def correlation_id_middleware(
    request: Request,
    call_next: RequestHandler,
) -> Response:
    request_id = _request_id(request.headers.get("X-Request-ID"))
    token = request_id_context.set(request_id)
    request.state.request_id = request_id
    try:
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
    finally:
        request_id_context.reset(token)

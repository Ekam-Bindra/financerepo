import asyncio
from collections.abc import Awaitable, Callable
from time import perf_counter
from typing import Any

import asyncpg
import redis.asyncio as redis

from equity_research_api.models import DependencyHealth
from equity_research_api.settings import Settings

DependencyProbe = Callable[[], Awaitable[None]]


async def _measure(
    probe: DependencyProbe,
    timeout_seconds: float,
) -> DependencyHealth:
    started = perf_counter()
    try:
        await asyncio.wait_for(probe(), timeout=timeout_seconds)
    except (TimeoutError, OSError, asyncpg.PostgresError, redis.RedisError):
        return DependencyHealth(status="unavailable", error="dependency unavailable")
    return DependencyHealth(
        status="ok",
        latency_ms=round((perf_counter() - started) * 1000, 2),
    )


async def check_dependencies(
    settings: Settings,
) -> dict[str, DependencyHealth]:
    async def check_postgres() -> None:
        connection = await asyncpg.connect(
            settings.database_url,
            timeout=settings.dependency_timeout_seconds,
        )
        try:
            await connection.execute("SELECT 1")
        finally:
            await connection.close()

    async def check_redis() -> None:
        client: Any = redis.from_url(  # type: ignore[no-untyped-call]
            settings.redis_url,
        )
        try:
            await client.ping()
        finally:
            await client.aclose()

    postgres, redis_result = await asyncio.gather(
        _measure(check_postgres, settings.dependency_timeout_seconds),
        _measure(check_redis, settings.dependency_timeout_seconds),
    )
    return {"postgres": postgres, "redis": redis_result}

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class DependencyHealth(BaseModel):
    status: Literal["ok", "unavailable"]
    latency_ms: float | None = None
    error: str | None = None


class HealthResponse(BaseModel):
    service: Literal["api"] = "api"
    status: Literal["ok", "degraded"]
    version: str
    timestamp: datetime


class ReadinessResponse(HealthResponse):
    dependencies: dict[str, DependencyHealth]

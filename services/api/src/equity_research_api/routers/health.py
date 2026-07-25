from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from equity_research_api.dependencies import check_dependencies
from equity_research_api.models import HealthResponse, ReadinessResponse
from equity_research_api.settings import Settings, get_settings

router = APIRouter(prefix="/health", tags=["health"])
SettingsDependency = Annotated[Settings, Depends(get_settings)]


@router.get(
    "/live",
    response_model=HealthResponse,
    summary="Confirm the API process is alive",
)
async def live(settings: SettingsDependency) -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=settings.app_version,
        timestamp=datetime.now(UTC),
    )


@router.get(
    "/ready",
    response_model=ReadinessResponse,
    summary="Confirm required dependencies are available",
    responses={status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ReadinessResponse}},
)
async def ready(
    settings: SettingsDependency,
    response: Response,
) -> ReadinessResponse:
    dependencies = await check_dependencies(settings)
    is_ready = all(item.status == "ok" for item in dependencies.values())
    if not is_ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return ReadinessResponse(
        status="ok" if is_ready else "degraded",
        version=settings.app_version,
        timestamp=datetime.now(UTC),
        dependencies=dependencies,
    )

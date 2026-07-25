import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from equity_research_api.logging import configure_logging
from equity_research_api.middleware import correlation_id_middleware
from equity_research_api.routers.health import router as health_router
from equity_research_api.settings import get_settings

settings = get_settings()
configure_logging(settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.info("api_starting")
    yield
    logger.info("api_stopping")


def create_app() -> FastAPI:
    application = FastAPI(
        title="AI-Powered Equity Research Assistant API",
        description="Versioned API foundation for source-grounded equity research.",
        version=settings.app_version,
        docs_url="/api/docs" if settings.app_env != "production" else None,
        openapi_url="/api/openapi.json" if settings.app_env != "production" else None,
        redoc_url=None,
        lifespan=lifespan,
    )
    application.middleware("http")(correlation_id_middleware)
    application.include_router(health_router, prefix="/api/v1")
    return application


app = create_app()

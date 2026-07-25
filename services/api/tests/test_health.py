from collections.abc import Generator
from typing import Any

import pytest
from fastapi.testclient import TestClient

from equity_research_api.main import app
from equity_research_api.models import DependencyHealth
from equity_research_api.routers import health


@pytest.fixture
def client() -> Generator[TestClient, Any, None]:
    with TestClient(app) as test_client:
        yield test_client


def test_liveness_returns_version_and_request_id(client: TestClient) -> None:
    response = client.get(
        "/api/v1/health/live",
        headers={"X-Request-ID": "c9d93169-c50b-46a4-96b4-5fcf89c20ed2"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "api"
    assert response.headers["X-Request-ID"] == ("c9d93169-c50b-46a4-96b4-5fcf89c20ed2")


def test_invalid_request_id_is_replaced(client: TestClient) -> None:
    response = client.get(
        "/api/v1/health/live",
        headers={"X-Request-ID": "not-a-valid-correlation-id"},
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] != "not-a-valid-correlation-id"


def test_readiness_reports_healthy_dependencies(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def healthy_dependencies(_: Any) -> dict[str, DependencyHealth]:
        return {
            "postgres": DependencyHealth(status="ok", latency_ms=1.1),
            "redis": DependencyHealth(status="ok", latency_ms=0.8),
        }

    monkeypatch.setattr(health, "check_dependencies", healthy_dependencies)
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["dependencies"]["postgres"]["status"] == "ok"


def test_readiness_returns_503_when_a_dependency_is_unavailable(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def degraded_dependencies(_: Any) -> dict[str, DependencyHealth]:
        return {
            "postgres": DependencyHealth(
                status="unavailable",
                error="dependency unavailable",
            ),
            "redis": DependencyHealth(status="ok", latency_ms=0.8),
        }

    monkeypatch.setattr(health, "check_dependencies", degraded_dependencies)
    response = client.get("/api/v1/health/ready")

    assert response.status_code == 503
    assert response.json()["status"] == "degraded"
    assert response.json()["dependencies"]["postgres"]["error"] == (
        "dependency unavailable"
    )

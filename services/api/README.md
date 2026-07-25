# Equity Research API

FastAPI foundation for the AI-Powered Equity Research Assistant.

## Endpoints

- `GET /api/v1/health/live` confirms the API process is running.
- `GET /api/v1/health/ready` verifies PostgreSQL and Redis connectivity.

The readiness endpoint returns HTTP `503` when either required dependency is
unavailable. Dependency error details are intentionally normalized so internal
connection information is not exposed.

## Local command

From the repository root:

```bash
make setup
make dev-api
```


# AI-Powered Equity Research Assistant

Enterprise-grade AI research platform for collecting, organizing, analyzing, and comparing public-company disclosures and generating source-grounded equity research outputs.

## Program

- Planned duration: 48 weeks
- Delivery cadence: 24 two-week sprints
- Target: enterprise-ready v1.0
- Initial market scope: U.S. public companies and SEC disclosures

## Core Documentation

- [Enterprise Requirements](docs/requirements/ENTERPRISE_REQUIREMENTS.md)
- [Technical Design and 48-Week Implementation Plan](docs/design/TECHNICAL_DESIGN_AND_ROADMAP.md)
- [Verified Project Status](docs/project-management/PROJECT_STATUS.md)
- [Two-Person Collaboration Workflow](docs/project-management/TWO_PERSON_COLLABORATION_WORKFLOW.md)
- [Master Execution Prompt](docs/prompts/MASTER_EXECUTION_PROMPT.md)

## Product Goal

Reduce the amount of repetitive work required during the first stage of equity research by automating document discovery, ingestion, extraction, comparison, retrieval, evidence-grounded question answering, and report generation while preserving source traceability and human oversight.

## Core Principles

1. Evidence before interpretation.
2. Facts and AI analysis remain clearly separated.
3. Every material claim should be traceable to source evidence.
4. Human review remains authoritative for high-impact research conclusions.
5. Financial-period, unit, currency, GAAP/non-GAAP, restatement, and amendment handling are first-class concerns.
6. Security, auditability, testing, observability, accessibility, and compliance are part of the architecture from the beginning.

## Status

Engineering foundation in progress on `feature/PLAT-001-project-foundation`.
SEC ingestion, document processing, financial extraction, and AI functionality
have not begun.

## Foundation architecture

```text
financerepo/
├── apps/
│   └── web/                    # Next.js App Router frontend
├── services/
│   └── api/                    # FastAPI backend
├── packages/
│   └── api-contracts/          # Shared TypeScript contracts
├── database/
│   └── migrations/
├── infrastructure/
│   └── docker/
├── tests/
│   └── integration/
├── .github/workflows/
├── AGENTS.md
├── docker-compose.yml
├── Makefile
└── pnpm-workspace.yaml
```

## Prerequisites

- Node.js 22 or newer.
- pnpm 9.
- Python 3.12.
- A Docker-compatible runtime with Docker Compose v2. Docker Desktop works;
  Colima is the validated free and open-source macOS option.

Free macOS container setup:

```bash
brew install docker docker-compose docker-buildx colima
# Follow Homebrew's caveat if Docker does not discover its Compose/Buildx plugins.
colima start --cpu 2 --memory 4 --disk 20
docker info
docker compose version
```

## Local setup

```bash
cp .env.example .env
make setup
make check
make dev
```

Use `colima stop` when the free macOS runtime is no longer needed.

Local services:

- Web application: `http://localhost:3000`
- Web health: `http://localhost:3000/api/health`
- API documentation: `http://localhost:8000/api/docs`
- API liveness: `http://localhost:8000/api/v1/health/live`
- API readiness: `http://localhost:8000/api/v1/health/ready`

Readiness verifies PostgreSQL and Redis connectivity and returns HTTP `503`
when either dependency is unavailable.

## Development commands

```bash
make install
make dev
make format
make lint
make typecheck
make test
make build
make check
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and pull-request workflow
and [SECURITY.md](SECURITY.md) for vulnerability-reporting guidance.

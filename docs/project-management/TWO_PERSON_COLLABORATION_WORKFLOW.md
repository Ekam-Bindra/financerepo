# Two-Person Collaboration Workflow

This document defines how two developers can work on the AI-Powered Equity Research Assistant at the same time without duplicating work or constantly creating merge conflicts.

## 1. Source of Truth

Use one GitHub repository as the shared source of truth.

Each developer has:
- A full local clone.
- Their own local database and development environment.
- Separate feature branches.
- Assigned issues/tasks.
- Pull requests for integration.

Do not use Dropbox, Google Drive, OneDrive, or a network share as the primary source-code collaboration system.

## 2. Recommended Repository Layout

```text
ai-equity-research-assistant/
├── apps/
│   └── web/
├── services/
│   ├── api/
│   ├── ingestion-worker/
│   ├── document-processor/
│   ├── financial-data/
│   └── ai-orchestrator/
├── packages/
│   ├── api-contracts/
│   ├── shared-types/
│   ├── ui-components/
│   └── financial-models/
├── ai/
│   ├── prompts/
│   ├── evaluations/
│   └── model-configurations/
├── database/
│   ├── migrations/
│   ├── seeds/
│   ├── schemas/
│   └── diagrams/
├── infrastructure/
│   ├── docker/
│   ├── terraform/
│   ├── kubernetes/
│   ├── monitoring/
│   └── environments/
├── docs/
│   ├── requirements/
│   ├── design/
│   ├── architecture/
│   ├── adr/
│   ├── security/
│   ├── api/
│   ├── runbooks/
│   ├── testing/
│   ├── prompts/
│   └── project-management/
├── tests/
│   ├── integration/
│   ├── end-to-end/
│   ├── performance/
│   ├── security/
│   └── ai-evaluation/
├── scripts/
├── sample-data/
├── .github/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── README.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## 3. Recommended Ownership Split

### Developer A — Backend, Data, Platform
Primary ownership:

```text
services/api/
services/ingestion-worker/
services/document-processor/
services/financial-data/
database/
infrastructure/
```

Typical responsibilities:
- Database design.
- APIs.
- SEC ingestion.
- Document processing.
- XBRL extraction.
- Financial calculations.
- Backend authentication/authorization.
- Infrastructure.
- Workflow execution.
- Logging/monitoring.

### Developer B — Frontend, AI Experience, Product Workflow
Primary ownership:

```text
apps/web/
packages/ui-components/
ai/prompts/
ai/evaluations/
tests/end-to-end/
```

Typical responsibilities:
- Web application.
- Dashboard.
- Charts.
- Filing reader.
- Research chat UX.
- Report editor.
- Accessibility.
- End-to-end testing.
- Prompt/evaluation workflows.

### Shared areas

```text
packages/api-contracts/
packages/shared-types/
database/migrations/
.github/
docker-compose.yml
README.md
```

Shared means both developers approve changes; it does not mean both should edit the same file at the same time.

## 4. The Core Rule: Contract First

Before frontend and backend implementation starts, agree on the interface.

Example:

```http
GET /api/v1/companies/search?query=AAPL
```

Example response:

```json
{
  "results": [
    {
      "companyId": "company_123",
      "legalName": "Apple Inc.",
      "ticker": "AAPL",
      "cik": "0000320193",
      "exchange": "NASDAQ"
    }
  ]
}
```

Then:
- Backend owner implements the endpoint.
- Frontend owner implements the UI using a mock response.
- Once the endpoint is merged, the frontend swaps the mock for the real API.

This allows true parallel development.

## 5. Branching Workflow

Protected branch:

```text
main
```

Do not normally commit directly to `main`.

Branch naming examples:

```text
feature/COMP-011-company-search-api
feature/COMP-012-company-search-ui
feature/ING-003-sec-filing-discovery
feature/DOC-009-document-chunking
feature/FIN-015-margin-calculations
feature/RAG-011-citation-mapping
fix/FIN-204-quarter-period-error
docs/ADR-004-search-engine-decision
```

Workflow:

1. Select an assigned issue.
2. Pull latest `main`.
3. Create a feature branch.
4. Commit small logical changes.
5. Push branch.
6. Open pull request.
7. Automated checks run.
8. Other developer reviews.
9. Address review comments.
10. Merge to `main`.
11. Delete branch.

## 6. Recommended Main-Branch Protections

- Require one approval.
- Require automated tests.
- Require linting/type checks.
- Require branch to be current before merge.
- Prevent direct pushes.
- Prevent force pushes.
- Require resolved conversations.
- Require code-owner review for critical shared areas.

## 7. Task Board

Recommended columns:

```text
Backlog
Ready
In Progress
In Review
Blocked
Testing
Done
```

Every task should have exactly one primary owner.

Recommended task fields:

| Field | Example |
|---|---|
| Task ID | FIN-015 |
| Owner | Developer A |
| Reviewer | Developer B |
| Phase | Structured Financial Data |
| Sprint | Sprint 11 |
| Priority | P1 |
| Size | Medium |
| Component | Backend |
| Status | In Progress |
| Dependency | FIN-005 |

## 8. Preventing Overlap

### Rule 1 — One task, one owner
One developer is accountable for completing an issue. The other can review or assist, but should not independently implement the same issue.

### Rule 2 — Declare expected files
Each issue should identify expected files or components before work starts.

Example:

```text
Expected files:
- services/api/app/companies/routes.py
- services/api/app/companies/service.py
- services/api/tests/test_company_search.py
```

### Rule 3 — Keep tasks small
Avoid vague tasks such as:

```text
Build dashboard
```

Prefer:

```text
DASH-001 Create dashboard layout
DASH-002 Create company header
DASH-003 Create financial highlight cards
DASH-004 Create revenue chart
DASH-005 Create filing-status widget
DASH-006 Connect dashboard API
```

### Rule 4 — Announce shared-file changes
Before modifying shared files, notify the other developer.

Example:

```text
I am updating the shared company-search API contract for COMP-011.
Please avoid packages/api-contracts until the PR is merged.
```

### Rule 5 — Keep pull requests focused
Prefer one task per PR. Avoid mixing unrelated frontend, backend, infrastructure, AI, and documentation changes into a single PR.

### Rule 6 — Review each other's work
The backend owner reviews whether frontend assumptions match APIs. The frontend owner reviews whether backend outputs support the intended UX.

## 9. Example Parallel Work

### Developer A
Branch:

```text
feature/COMP-011-company-search-api
```

Works in:

```text
services/api/app/companies/
services/api/tests/companies/
database/migrations/
```

### Developer B
Branch:

```text
feature/COMP-012-company-search-ui
```

Works in:

```text
apps/web/src/features/company-search/
apps/web/src/components/
apps/web/tests/
```

Both can work simultaneously because the API contract was agreed first.

## 10. Weekly Routine

### Start of week
Spend 30–45 minutes deciding:
- What each person owns.
- Blocked tasks.
- Contracts that must be agreed upon.
- Shared files likely to change.
- What should be completed before the next sync.

### During week
Each developer:
- Updates issue status.
- Pushes regularly.
- Opens draft PRs early.
- Reviews the other developer's PRs.
- Raises blockers quickly.

### End of week
Review:
- Completed tasks.
- Delays.
- Bugs.
- Architecture changes.
- Next assignments.

## 11. Example First Four Weeks for Two Developers

### Week 1
Developer A:
- Backend project initialization.
- PostgreSQL setup.
- FastAPI setup.
- Migration framework.
- Docker configuration.

Developer B:
- Next.js initialization.
- UI component system.
- Application layout.
- Login page design.
- Company-search wireframe.

Together:
- API conventions.
- Repository conventions.
- Coding standards.
- PR template.
- Definition of Done.

### Week 2
Developer A:
- Company model.
- Company-search API.
- CIK/ticker model.
- API tests.

Developer B:
- Company-search interface.
- Loading/empty/error states.
- Search-result cards.
- Frontend tests.

### Week 3
Developer A:
- SEC source adapter.
- Filing metadata.
- Filing-download workflow.

Developer B:
- Company workspace page.
- Filing list.
- Processing-status components.

### Week 4
Developer A:
- Document storage.
- Duplicate detection.
- Retry handling.
- Ingestion monitoring.

Developer B:
- Document-reader shell.
- Filing filters.
- Error states.
- End-to-end onboarding test.

## 12. Local Development

Each developer should clone separately and run an independent local environment.

Example:

```bash
git clone https://github.com/Ekam-Bindra/financerepo.git
cd financerepo
cp .env.example .env
docker compose up -d
```

Eventually standardize common commands such as:

```bash
make install
make migrate
make seed
make dev
make test
```

Example local ports:

```text
Frontend            localhost:3000
Backend API         localhost:8000
PostgreSQL          localhost:5432
Redis               localhost:6379
Search engine       localhost:9200
Object storage      localhost:9000
Workflow dashboard  localhost:8233
```

Each developer should use their own local database and local test data.

## 13. Never Commit Secrets

`.gitignore` should exclude:

```text
.env
.env.local
.env.production
*.pem
*.key
credentials.json
secrets/
node_modules/
.venv/
__pycache__/
dist/
build/
coverage/
local-data/
downloads/
filings/
audio/
generated-reports/
database-backups/
```

Commit `.env.example`, but never real credentials.

## 14. Recommended CODEOWNERS Direction

When usernames are finalized, use `.github/CODEOWNERS` to identify primary reviewers for major areas.

Example structure:

```text
/apps/web/                     @frontend-owner
/packages/ui-components/      @frontend-owner
/services/api/                @backend-owner
/services/ingestion-worker/   @backend-owner
/services/document-processor/ @backend-owner
/services/financial-data/     @backend-owner
/database/                    @backend-owner
/infrastructure/              @backend-owner
/packages/api-contracts/      @backend-owner @frontend-owner
/packages/shared-types/       @backend-owner @frontend-owner
/.github/                     @backend-owner @frontend-owner
```

## 15. Simplest Mental Model

For a two-person team:

```text
Developer B builds what users see.
Developer A builds the systems that provide the data.
Both agree on contracts between those systems.
Both review each other's changes.
GitHub integrates the finished work.
```

This division provides enough independent work for both people to remain productive while greatly reducing merge conflicts and duplicated implementation.
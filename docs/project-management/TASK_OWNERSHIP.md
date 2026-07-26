# Remaining Task Ownership — Ekam and Abhinav

Last reconciled: 2026-07-25

This is the authoritative ownership map for parallel work. Codex and both
developers must read this file together with `PROJECT_STATUS.md` before
selecting work.

Abhinav’s GPT/coding-agent handoff prompt is maintained at
`docs/prompts/ABHINAV_EXECUTION_PROMPT.md`.

## Allocation summary

| Backlog state | Count |
| --- | ---: |
| Master tasks | 242 |
| Verified complete and excluded from allocation | 24 |
| Remaining tasks assigned to Ekam | 104 |
| Remaining tasks assigned to Abhinav | 114 |
| Unassigned or duplicate remaining tasks | 0 |

The split favors coherent subsystem ownership over a perfectly equal number of
tasks. A range such as `ING-001–020` is inclusive and applies only to that
prefix.

## Primary work lanes

### Ekam — platform, backend, data, security, and operations

Primary paths:

- `services/api`
- future ingestion and financial-data services
- `database`
- `infrastructure`
- backend portions of `packages/api-contracts`
- security, tenancy, reliability, and production operations

### Abhinav — document intelligence, AI, frontend, and product workflow

Primary paths:

- `apps/web`
- future document-processing and AI-orchestration services
- `ai`
- `tests/end-to-end`
- frontend portions of `packages/api-contracts`
- analyst UX, reports, evaluations, and beta workflow

## Exact remaining-task allocation

| Phase | Ekam | Count | Abhinav | Count |
| --- | --- | ---: | --- | ---: |
| 1 — Program foundation | `PRG-014`, `PRG-017–019` | 4 | `PRG-002`, `PRG-020` | 2 |
| 2 — Platform and developer experience | `PLAT-008–010`, `PLAT-012–013`, `PLAT-015`, `PLAT-018–020` | 9 | `PLAT-006` | 1 |
| 3 — Identity, tenancy, company master | `IAM-001–002`, `IAM-004–010`, `IAM-012`, `IAM-015`, `IAM-017–018` | 13 | `IAM-003`, `IAM-011`, `IAM-013–014`, `IAM-016` | 5 |
| 4 — SEC ingestion | `ING-001–020` | 20 | — | 0 |
| 5 — Document processing and search | — | 0 | `DOC-001–020` | 20 |
| 6 — Structured financial data | `FIN-001–019`, `FIN-021–022` | 21 | `FIN-020` | 1 |
| 7 — Qualitative AI extraction | — | 0 | `AIQ-001–018` | 18 |
| 8 — Comparison and trend detection | — | 0 | `CMP-001–018` | 18 |
| 9 — Research assistant and citations | `RAG-003–008`, `RAG-010–014`, `RAG-018` | 12 | `RAG-001–002`, `RAG-009`, `RAG-015–017`, `RAG-019–020` | 8 |
| 10 — Dashboard and reports | — | 0 | `UX-001–010`, `REP-001–012` | 22 |
| 11 — Enterprise hardening and beta | `ENT-006–007`, `ENT-009–016` | 10 | `ENT-001–005`, `ENT-008`, `ENT-017–020` | 10 |
| 12 — General availability | `GA-004–006`, `GA-008`, `GA-011–017`, `GA-019–022` | 15 | `GA-001–003`, `GA-007`, `GA-009–010`, `GA-018`, `GA-023–024` | 9 |
| **Total remaining** |  | **104** |  | **114** |

Task descriptions and phase dependencies remain authoritative in
`MASTER_TASK_LIST.md`. Completed task IDs remain authoritative in
`PROJECT_STATUS.md`.

## Required handoffs

| Producer | Consumer | Merge gate before consumer starts |
| --- | --- | --- |
| Ekam: platform environments, migrations, secrets, telemetry | Both developers | Environment contracts, setup documentation, and health checks are merged |
| Ekam: IAM/company APIs and permissions | Abhinav: profile, search, workspace, and metadata UI | Versioned API contract, authorization behavior, mocks, and error states are merged |
| Ekam: `ING-001–020` | Abhinav: `DOC-001–020` | Immutable raw-document, source metadata, lineage, status, retry, and object-storage contracts are merged |
| Abhinav: normalized documents, chunks, and source references | Ekam: structured financial pipeline; Abhinav: AI pipeline | Document/chunk schemas, quality status, and citation anchors are merged |
| Ekam: `FIN-001–019`, `FIN-021–022` | Abhinav: `FIN-020`, comparisons, dashboard, and reports | Financial fact/history APIs, units, periods, warnings, and validation status are merged |
| Abhinav: AI extraction schemas and evaluations | Ekam: RAG retrieval/validation services | Versioned insight schemas, confidence/review state, prompt/model lineage, and thresholds are merged |
| Ekam: RAG retrieval, citation, numeric, and injection controls | Abhinav: answer prompts, evidence UI, feedback, and benchmarks | Retrieval/answer contract, citation objects, refusal states, and security behavior are merged |
| Both task owners | Enterprise/GA consumers | Required quality, security, accessibility, performance, recovery, and compliance evidence is merged |

## No-overlap operating rules

1. Before creating a branch, read `PROJECT_STATUS.md`, this file, and the
   dependency tasks in `MASTER_TASK_LIST.md`.
2. Work only on task IDs assigned to the active developer. The current
   repository owner defaults to Ekam unless the user explicitly says the work
   is for Abhinav.
3. Use one task or tightly coupled task group per branch and pull request.
4. Put the task ID and owner in the pull-request description.
5. Do not start a consumer task before its producer handoff in the table above
   is merged.
6. If blocked, select another ready task from the same owner’s lane; do not take
   the other developer’s task.
7. Reallocation requires a dedicated pull request updating this file before
   implementation begins. The pull request must state the old owner, new owner,
   reason, affected dependencies, and active-branch disposition.
8. Never maintain competing migrations, API contracts, or root configuration
   changes. The producing task owner makes the change; the consuming owner
   reviews and updates only after merge.

## Shared-file protocol

The following paths are shared even though tasks have one owner:

- `packages/api-contracts`
- `database/migrations`
- `.github`
- `docker-compose.yml`
- root dependency, build, lint, and formatting configuration
- requirements, design, ADR, status, and ownership documents

For a shared-file change:

1. declare the producing task in the pull request;
2. publish the contract or migration before dependent implementation;
3. have only the producing branch edit the shared file;
4. require the consumer to rebase from merged `main`;
5. resolve ownership changes through this document, not informal parallel
   edits.

## Immediate queues

Ekam’s next ready queue:

1. `PRG-014` — branching and release strategy.
2. `PRG-017` — severity and incident classification.
3. `PRG-018`/`PRG-019` — threat model and data classification.

Abhinav’s next ready queue:

1. `PRG-020` — quality metrics and release gates.
2. `PLAT-006` — runnable integration-test framework.
3. `PRG-002` — stakeholder-workshop evidence when stakeholders are available.

Neither developer should begin SEC ingestion, document processing, financial
extraction, or AI implementation until the applicable program and platform
dependencies are complete and merged.

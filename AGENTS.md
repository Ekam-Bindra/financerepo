# AI-Powered Equity Research Assistant — Codex Instructions

## Authoritative project context

Build the enterprise AI-Powered Equity Research Assistant defined in:

- `docs/requirements/ENTERPRISE_REQUIREMENTS.md`
- `docs/design/TECHNICAL_DESIGN_AND_ROADMAP.md`
- `docs/project-management/MASTER_TASK_LIST.md`
- `docs/project-management/TWO_PERSON_COLLABORATION_WORKFLOW.md`
- `docs/prompts/MASTER_EXECUTION_PROMPT.md`

These documents and the master execution prompt are authoritative unless an
approved architecture decision record changes them. Apply them even when the
user gives a very short follow-up such as "continue".

## Current delivery boundary

The repository is in the engineering-foundation phase. Do not implement SEC
ingestion, document intelligence, financial extraction, or AI functionality
until the foundation is validated and the corresponding task is explicitly in
scope.

## Working rules

- Never implement directly on `main`.
- Work on one declared task or tightly related task group at a time.
- Inspect existing code and documentation before changing architecture.
- Do not silently replace approved architecture or project conventions.
- Prefer deterministic financial processing over LLM reasoning when possible.
- Preserve source lineage for all material financial claims.
- Never invent financial facts, filing content, test results, or implementation
  status.
- Never hard-code secrets or commit `.env` files.
- Add tests with behavioral changes.
- Update documentation when commands, APIs, architecture, or behavior changes.
- Do not introduce a dependency without a concrete operational benefit.
- Keep frontend and backend contracts explicit and versioned.
- Treat security, accessibility, observability, and failure handling as part of
  implementation rather than follow-up work.

## Progress reporting

Use `docs/project-management/PROJECT_STATUS.md` as the verified progress
ledger. At the end of every user-facing response about repository work, report:

- completed master tasks as `X/242 (Y%)`;
- task IDs newly completed in that response, or `none`;
- the next unblocked task IDs and the immediate action;
- any blocker that prevents the next action.

Count a task only when its acceptance criteria and the Definition of Done are
satisfied by repository or external-system evidence. Do not count proposed,
partially implemented, scaffold-only, or unverified work. Update the ledger in
the same change that completes a task. When the user gives a short instruction
such as "continue", select the next unblocked work from the ledger and master
task list while respecting dependencies, branch scope, and pull-request gates.

## Repository structure

- `apps/web`: Next.js App Router frontend.
- `services/api`: FastAPI backend.
- `packages/api-contracts`: shared TypeScript API contracts.
- `database`: migrations and database documentation.
- `infrastructure`: container and future infrastructure definitions.
- `tests`: cross-service integration and end-to-end foundations.
- `docs`: requirements, design, decisions, runbooks, and project management.

## Required commands

```text
make setup       # create local Python environment and install dependencies
make install     # install frontend and backend dependencies
make dev         # run local services through Docker Compose
make test        # run unit tests
make lint        # run Python and TypeScript linting
make typecheck   # run Python and TypeScript type checks
make format      # format supported source files
make check       # lint, typecheck, and test
```

## Git conventions

Branches:

```text
feature/<TASK-ID>-short-description
fix/<TASK-ID>-short-description
docs/<TASK-ID>-short-description
```

Commits:

```text
<type>(<area>): <description>
```

Examples:

```text
feat(platform): establish monorepo foundation
test(api): add readiness endpoint coverage
docs(architecture): record search decision
```

## Definition of Done

A task is complete only when:

- implementation and acceptance criteria are complete;
- formatting, linting, type checking, and relevant tests pass;
- security, data-lineage, privacy, and authorization impacts are addressed;
- error and degraded states are handled;
- relevant observability and accessibility exist;
- documentation and API contracts are current;
- deployment, rollback, and recovery implications are understood;
- no critical unresolved defects remain.

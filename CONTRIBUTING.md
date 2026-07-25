# Contributing

Read `AGENTS.md` and the project documentation before starting work.

## Workflow

1. Select a task with a clear owner, reviewer, dependencies, and acceptance
   criteria.
2. Pull the latest `main`.
3. Create a task branch such as
   `feature/PLAT-001-project-foundation`.
4. Keep the change focused and update relevant tests and documentation.
5. Run `make check`.
6. Push the branch and open a pull request.
7. Resolve automated checks and review comments before merging.

Direct commits to `main` and force pushes are not part of the normal workflow.

## Shared files

Coordinate changes to API contracts, database migrations, root tooling,
Docker Compose, and CI. Shared ownership means both developers review a change;
it does not mean both developers edit the same file simultaneously.

## Pull requests

Each pull request should explain:

- what changed and why;
- the task ID and acceptance criteria;
- architecture, security, data, and operational effects;
- tests and validation performed;
- migration and rollback implications;
- known limitations or follow-up tasks.


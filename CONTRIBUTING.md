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

## Review policy

Pull requests and all required automated checks are mandatory. While the
repository has only one maintainer, an approving review is not required because
GitHub does not permit an author to approve their own pull request. The
maintainer must still merge through a pull request after every required check
passes and every conversation is resolved.

Restore the one-approval branch rule before a second maintainer begins
contributing. See
`docs/adr/0001-solo-maintainer-pull-request-approval.md` for the decision,
trade-offs, and restoration trigger.

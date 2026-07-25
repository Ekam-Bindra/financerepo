# ADR 0001: Solo-maintainer pull-request approval

- Status: Accepted
- Date: 2026-07-25
- Owners: Repository maintainer
- Revisit trigger: A second maintainer receives repository write access

## Context

The target collaboration workflow requires one approving pull-request review.
The repository currently has one collaborator, who is also the author of the
foundation pull request. GitHub does not allow pull-request authors to approve
their own changes, so an approval requirement makes every pull request
impossible to merge.

The project must retain protected-branch enforcement, mandatory pull requests,
strict required checks, resolved conversations, linear history, and protection
from direct, forced, or destructive updates.

## Decision

Set the required approving-review count for `main` to zero while there is only
one repository maintainer. Continue to require:

- all changes to enter `main` through pull requests;
- strict `Web checks`, `API checks`, and `Compose validation` status checks;
- resolved review conversations;
- linear history;
- enforcement for administrators;
- blocked force pushes and branch deletion.

Restore the required approving-review count to one before granting a second
maintainer write access.

## Consequences

The solo maintainer can merge checked pull requests without paying for an
external review service or creating a sham reviewer account. Automated gates
and protected-branch controls remain enforced, but independent human review is
temporarily unavailable. The repository owner is responsible for restoring the
approval gate when collaboration begins.

## Rollback

Set `required_approving_review_count` to `1` in the `main` branch protection
rule. No source-code or data migration is required.

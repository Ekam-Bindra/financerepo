# Architecture Decision Records

Task: `PRG-012`

Architecture Decision Records (ADRs) preserve significant technical and
cross-functional decisions, their context, trade-offs, and consequences.
Merged ADRs are the authoritative decision history alongside the requirements,
technical design, and master execution prompt.

## When an ADR is required

Create an ADR before implementing a decision that materially changes:

- approved architecture, service boundaries, data stores, or protocols;
- security, privacy, tenancy, identity, secrets, or trust boundaries;
- financial-data semantics, lineage, validation, or source-of-truth rules;
- source rights, retention, AI-provider data handling, or compliance controls;
- model/provider selection, AI safety policy, or evaluation gates;
- reliability targets, deployment topology, recovery, or migration strategy;
- a project-wide convention that is expensive to reverse.

Routine implementation detail, a reversible local refactor, and a decision
already fully governed by an accepted ADR do not need a new record.

## Lifecycle

1. Copy `template.md` to the next zero-padded number:
   `NNNN-short-kebab-case-title.md`.
2. Set status to **Proposed**, identify owners and reviewers, and link affected
   requirements, tasks, risks, and prior ADRs.
3. Describe the decision drivers and at least two credible options, including
   “do nothing” when applicable.
4. Record security, data/lineage, compliance, accessibility, reliability, cost,
   migration, rollback, and operational consequences.
5. Open a focused pull request and obtain reviews from the accountable roles.
6. Change the status to **Accepted** only when the authorized decision owner
   approves it and required checks pass.
7. Implement the decision in linked tasks. Acceptance does not imply that
   implementation is complete.
8. If the decision changes, create a new ADR and mark the old record
   **Superseded by ADR NNNN**. Do not rewrite accepted decision history.

## Status values

- **Proposed:** under review; not authoritative.
- **Accepted:** approved and authoritative.
- **Rejected:** considered but not selected.
- **Deprecated:** retained for history but no longer recommended.
- **Superseded by ADR NNNN:** replaced by a newer accepted decision.

## Decision authority

The Principal Software Architect accepts architecture and platform decisions.
Security decisions also require the Application or Cloud Security owner.
Financial semantics require the Financial Data Specialist. Source-rights and
compliance decisions require Legal/Compliance. Product-scope decisions require
the Enterprise Product Manager. Critical cross-functional decisions require
all affected authorities.

When only one maintainer is available, role reviews are recorded as pending
external sign-off where expertise is unavailable; the ADR must not claim legal,
security, or financial approval that did not occur.

## Review rules

- ADRs use the normal protected pull-request workflow.
- Reviewers verify consistency with requirements, risks, and existing ADRs.
- Unresolved material objections block acceptance.
- Accepted ADRs include migration, rollback, observability, and validation
  implications or explicitly state why each is not applicable.
- The Technical Program Manager reviews accepted ADRs at phase gates and when a
  revisit trigger occurs.

## Index

| ADR | Status | Decision |
| --- | --- | --- |
| [0001](0001-solo-maintainer-pull-request-approval.md) | Accepted | Temporary zero-approval policy for a one-maintainer repository |

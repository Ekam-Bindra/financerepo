# Security policy

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability or exposed secret.
Contact the repository owner privately with:

- the affected component;
- reproduction steps;
- likely impact;
- any suggested mitigation.

Do not include production credentials, private customer information, or
regulated data in the report.

## Foundation controls

- Secrets are supplied through environment variables and excluded from Git.
- Production API documentation is disabled by default.
- Correlation identifiers support incident investigation without carrying user
  data.
- Readiness failures expose normalized errors rather than connection details.
- CI runs formatting, linting, types, tests, builds, and Compose validation.

Authentication, authorization, tenant isolation, audit events, rate limiting,
and application threat controls must be implemented before exposing product
workflows.


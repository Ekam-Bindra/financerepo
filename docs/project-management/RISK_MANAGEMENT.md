# Program Risk Management

This document defines the operating process for the product and technical risk
registers:

- `PRODUCT_RISK_REGISTER.md`
- `TECHNICAL_RISK_REGISTER.md`

Ratings are initial planning judgments, not measured production outcomes.
Named people replace role owners when the delivery team is staffed.

## Scoring

Likelihood and impact use a five-point scale.

| Score | Likelihood | Impact |
| --- | --- | --- |
| 1 | Rare; exceptional conditions required | Negligible; no material user, financial, legal, security, or schedule effect |
| 2 | Unlikely; could occur but is not expected | Minor; localized rework or recoverable user inconvenience |
| 3 | Possible; credible during the program | Moderate; milestone, quality target, or user workflow is affected |
| 4 | Likely; expected without active controls | Major; release, trust, compliance, security, or material data quality is affected |
| 5 | Almost certain or already recurring | Severe; unsafe output, material breach, release failure, or sustained loss of service |

`Inherent score = likelihood × impact` before planned controls.

| Score | Rating | Required response |
| --- | --- | --- |
| 1–4 | Low | Owner monitors during the normal monthly review |
| 5–9 | Moderate | Mitigation plan and target residual score are required |
| 10–16 | High | Review at least every two weeks and at each phase gate |
| 17–25 | Critical | Escalate immediately; block affected release or feature until formally reduced or accepted |

## Required register fields

Every active risk records:

- a stable risk ID and concise risk statement;
- cause and potential consequence;
- likelihood, impact, inherent score, and target residual score;
- one accountable role owner;
- preventive controls and concrete mitigation actions;
- an observable trigger or early-warning indicator;
- a contingency response if the risk materializes;
- status and next formal review point.

Role ownership is accountability, not proof that all mitigation work is
complete. Delivery tasks must be created in the master backlog or issue tracker
when a mitigation requires implementation.

## Status workflow

- **Identified:** recorded but mitigation work has not started.
- **Mitigating:** controls or evidence are actively being developed.
- **Monitoring:** planned controls exist and indicators are being watched.
- **Accepted:** authorized owner accepts the residual exposure with rationale
  and review date.
- **Materialized:** the risk occurred and is managed as an issue or incident.
- **Closed:** the threat no longer applies or evidence shows it is adequately
  eliminated.

## Review and escalation

The Technical Program Manager maintains both registers and facilitates:

1. a biweekly review of high and critical risks;
2. a monthly review of all open risks;
3. a review at every phase exit and release-readiness gate;
4. an immediate review after a material incident, source-policy change,
   architecture change, model change, or quality-threshold breach.

The role owner updates indicators, mitigation evidence, residual rating, and
next actions. Product risks are accepted by the Product Manager with
Compliance/Legal approval where applicable. Technical risks are accepted by the
Principal Architect, with Security approval for security risks and the
Financial Data Specialist for financial-correctness risks. Critical residual
risk requires cross-functional release sign-off.

## Initial assumptions

- The first release remains limited to U.S. public companies and supported SEC
  disclosures.
- Recommendation and trade-execution functionality remains excluded or
  disabled by default.
- Human review remains authoritative for formal research output.
- Source rights, quality gates, and threat modeling are separate required tasks;
  a risk-register entry does not satisfy those deliverables.

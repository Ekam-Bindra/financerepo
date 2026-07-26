# Financial Disclaimer Requirements

Task: `PRG-010`

These are product and engineering requirements for counsel-approved
disclosures. They are not final legal language and do not replace a
jurisdiction-, customer-, or workflow-specific legal review.

## Required messages

Counsel-approved language must communicate, in plain language, that:

1. the system is an informational research assistant and does not replace
   professional financial judgment;
2. generated content is not individualized investment, legal, tax, or
   accounting advice and is not an offer, solicitation, or guarantee;
3. AI-generated extraction and analysis can be incomplete, stale, or wrong;
4. users must inspect cited primary sources and independently verify material
   facts, calculations, periods, units, assumptions, and conclusions;
5. historical results and forward-looking statements do not guarantee future
   outcomes;
6. source availability, coverage, timeliness, licensing, and processing status
   can limit an answer or report;
7. the product is not affiliated with or endorsed by the SEC or an issuer merely
   because it displays SEC or issuer materials;
8. formal research publication and any investment conclusion require an
   authorized human reviewer and the customer’s applicable compliance process.

## Placement and interaction requirements

| Surface | Requirement |
| --- | --- |
| Sign-in/onboarding and terms acceptance | Present the general service limitation and record the accepted disclosure version, timestamp, user, tenant, and locale |
| Application shell | Provide a persistent, accessible link to current disclosures and source-use information |
| AI answer | Label AI-generated content, separate fact/analysis/assumption, show evidence and freshness, and display material limitations inline |
| Dashboard/score | Show methodology, inputs, period, missing-data handling, version, and the statement that a score is not an objective recommendation |
| Research report/editor | Include disclosure version, generation timestamp, source cutoff, AI/human edit markers, open validation issues, and approval state |
| Export/share | Embed applicable disclosures and evidence appendix in the artifact; do not rely only on an application footer |
| Incomplete/stale/conflicting data | Show a prominent contextual warning and block finalization where the missing evidence is material |
| Recommendation feature | Remain disabled by default; require separate authorization, methodology, assumptions, opposing evidence, uncertainty, risks, human approval, audit history, and counsel-approved language |

Disclosures must be perceivable by keyboard and assistive technology, readable
at 200% zoom, available before a consequential action, and never hidden behind
color alone, hover interaction, or preselected consent.

## Dynamic financial disclosures

The system must generate contextual warnings when applicable:

- fiscal and calendar periods differ;
- values are quarterly, year-to-date, annual, trailing, instant, or duration;
- currencies, units, scales, or share bases differ;
- GAAP and non-GAAP measures appear together;
- filings are amended, restated, incomplete, or superseded;
- guidance is management-provided rather than an external forecast;
- calculations use assumptions, missing values, or incompatible periods;
- source evidence conflicts or falls below a confidence threshold;
- content is stale or a required ingestion/validation step failed.

## Governance and release controls

- Legal/Compliance owns final language, supported jurisdictions, customer
  variants, translations, and review cadence.
- Disclosures are versioned content with effective dates and immutable acceptance
  records; application code references a disclosure ID rather than hard-coded
  legal prose.
- Material wording changes require Legal/Compliance approval, regression review,
  and renewed user acceptance when counsel determines it is necessary.
- Automated tests verify required placement, version IDs, export inclusion,
  accessibility, and recommendation-feature gating.
- Product analytics may measure display and acknowledgment but must not capture
  sensitive research content.
- No production release may describe output as advice, guaranteed, approved by
  the SEC, error-free, comprehensive, or suitable for a user without human
  review.

## Approval checklist

Before production, Legal/Compliance must sign off on:

- entity/provider identity and regulated-status wording;
- intended users, jurisdictions, customer types, and permitted workflows;
- investment-advice, broker/dealer, research-publication, record-retention, and
  communication requirements that apply;
- recommendation, score, forward-looking statement, and third-party-source
  language;
- terms acceptance, privacy notice, accessibility, export, audit, retention,
  and incident/takedown procedures.

# Source Rights Classification

Task: `PRG-009`

This is an engineering control matrix, not legal advice. Legal/Compliance must
approve every production source and record the evidence reviewed. Public access
alone does not authorize automated collection, AI processing, storage, or
redistribution unless the governing terms permit those uses.

## Rights classes

| Class | Meaning | System behavior |
| --- | --- | --- |
| Approved | Authoritative terms support the defined use and required controls are recorded | Source may be enabled only for the approved use |
| Conditional | Use may be permissible, but source/content-specific terms, contracts, or consent must be reviewed | Disabled by default; allowlist after approval |
| Licensed | A signed agreement grants the defined rights | Disabled until contract metadata and enforcement controls exist |
| Prohibited | Terms or policy disallow the intended use | Block acquisition and processing |
| Unknown | Evidence is missing or ambiguous | Treat as prohibited until classified |

## Initial classification matrix

| Source IDs | Initial class | Approved or proposed use | Required controls / unresolved conditions |
| --- | --- | --- | --- |
| SRC-001–SRC-004 | Approved with conditions | Filing discovery, retrieval, storage, processing, citation, and source-linked display | Identified user agent; maximum 10 requests/second; efficient bulk access; attribution; no SEC seals/logos; no implied SEC affiliation; monitor policy changes |
| SRC-005 | Conditional | Discovery fallback and operational monitoring | Confirm endpoint-specific automation expectations; prefer documented APIs, archives, bulk data, and RSS |
| SRC-006 | Conditional | Supplemental issuer releases and presentations | Review each domain’s terms, robots policy, copyright, retention, redistribution, attribution, and AI-processing rights; domain/content allowlist |
| SRC-007 | Unknown | Speech-to-text and commentary analysis | Written authorization or license must cover access, recording, transcription, storage, AI processing, quotation, and redistribution |
| SRC-008 | Unknown or Licensed | Transcript search, extraction, and analysis | Identify copyright owner; contract must cover storage, derivative processing, quotation, display, export, retention, and model-provider transfer |
| SRC-009–SRC-010 | Licensed | Contract-defined news, price, reference, or estimate workflows | Provider agreement, entitlements, user limits, display/derived-data rights, retention/deletion, audit, and offboarding controls |
| SRC-011 | Conditional | Tenant-private processing of user-provided documents | User attestation/contract authority, malware scanning, tenant isolation, retention/deletion, export, and takedown process |
| SRC-012 | Conditional | Approved AI processing | Provider terms/DPA, no-training setting where required, region, subprocessors, retention, deletion, confidentiality, security, audit, and model/version allowlist |

## SEC decision evidence

The SEC states that government-created sec.gov content and EDGAR public filing
content are free to access and reuse. It also states that sec.gov information
may be copied or redistributed without SEC permission, while restricting SEC
marks and any implication of affiliation. The technical authorization is
therefore conditional on the access-policy controls above rather than on a paid
license.

References:

- [SEC Webmaster FAQ](https://www.sec.gov/about/webmaster-frequently-asked-questions)
- [SEC Website Dissemination policy](https://www.sec.gov/about/privacy-information#dissemination)
- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

## Approval record requirements

Before enabling a source, record:

- source ID, owner, domain/provider, terms URL, contract ID if applicable;
- reviewer and approval date, review expiration, and change-monitoring owner;
- allowed acquisition methods and request limits;
- allowed user groups, territories, display, quotation, export, and
  redistribution;
- storage, retention, deletion, backup, and disaster-recovery treatment;
- derivative-data, machine-learning, model-provider, and human-review rights;
- attribution, branding, audit, reporting, and termination obligations;
- kill-switch identifier and deletion/offboarding procedure.

Any material terms change returns the source to **Unknown**, disables new
acquisition, and triggers Legal/Compliance review. Existing data follows the
recorded retention, deletion, and contract-termination obligations.

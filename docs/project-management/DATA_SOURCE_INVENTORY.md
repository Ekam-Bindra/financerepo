# Data Source Inventory

Task: `PRG-008`

This inventory defines the candidate inputs for the initial U.S. public-company
research release. Inclusion here does not authorize production use; the rights
decision in `SOURCE_RIGHTS_CLASSIFICATION.md` is controlling.

| ID | Source | Content and access | Intended use | Freshness | Release decision | Accountable owner |
| --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | SEC EDGAR Submissions API | Public JSON from `data.sec.gov/submissions`; no API key | Company identity, tickers, exchanges, filing discovery, accession metadata | Updated throughout the day | Initial release | Data Engineering Lead |
| SRC-002 | SEC XBRL Company Facts/Concept APIs | Public JSON from `data.sec.gov/api/xbrl`; no API key | Source-grounded standardized financial facts and validation input | Updated throughout the day | Initial release | Financial Data Specialist |
| SRC-003 | SEC EDGAR filing archives | Public HTML, inline XBRL, XML, text, exhibits, and available PDFs under `sec.gov/Archives` | Immutable original filings, sections, tables, exhibits, and citation anchors | Filing-driven | Initial release for approved forms | Data Engineering Lead |
| SRC-004 | SEC bulk submissions and company-facts archives | Nightly ZIP archives published by the SEC | Efficient backfill, reconciliation, and recovery | Nightly | Initial release where operationally beneficial | Data Engineering Lead |
| SRC-005 | SEC filing search/RSS/latest-filings surfaces | Public SEC search and RSS resources | Discovery fallback and freshness monitoring | Near-real-time but not guaranteed | Conditional fallback; API/archive preferred | Data Engineering Lead |
| SRC-006 | Issuer investor-relations websites | Issuer-hosted HTML, releases, presentations, and reports; access varies by issuer | Supplemental company disclosures not present in the selected EDGAR record | Issuer-driven | Conditional per domain and content class | Compliance and Legal Reviewer |
| SRC-007 | Issuer earnings webcasts and audio | Issuer or vendor-hosted streams/recordings | Authorized speech-to-text and commentary analysis | Event-driven | Excluded until explicit rights approval | Compliance and Legal Reviewer |
| SRC-008 | Earnings-call transcripts | Issuer-authored or third-party licensed text | Management commentary, guidance, Q&A, and period comparison | Event-driven | Excluded until licensed/approved | Compliance and Legal Reviewer |
| SRC-009 | Licensed news | Commercial news APIs/feeds | Approved material-event context | Provider-driven | Future scope; contract required | Enterprise Product Manager |
| SRC-010 | Market prices, reference data, and estimates | Exchange/vendor datasets and APIs | Price context, consensus, valuation, and real-time analytics | Vendor-specific | Future scope; contract required | Enterprise Product Manager |
| SRC-011 | User-uploaded research documents | Authenticated workspace upload | User-authorized private analysis and source comparison | User-driven | Future/conditional; tenant and rights controls required | Enterprise Product Manager |
| SRC-012 | Model-provider inputs/outputs | Data sent to and returned from approved AI providers | Extraction, retrieval synthesis, and report assistance | Request-driven | Conditional on provider terms, privacy, retention, and security approval | MLOps Lead |

## Required metadata

Every acquired source record must retain:

- source ID, canonical URL or provider identifier, and retrieval timestamp;
- publication, filing, acceptance, and reporting-period timestamps when
  available;
- company, CIK, accession number, form/document type, and amendment status;
- MIME type, byte length, cryptographic checksum, and immutable object version;
- rights class and the version/date of the governing rights decision;
- retrieval method, user-agent identity, processing status, and failure reason;
- source and parser versions used by every derived artifact.

## Operational constraints

- Prefer SEC bulk archives for large backfills.
- SEC automated traffic must use an identified user agent and remain at or
  below the SEC’s current maximum of 10 requests per second across the
  application.
- Apply backoff, caching, conditional requests where supported, idempotency,
  checksums, and a kill switch.
- Do not bypass authentication, paywalls, robots controls, access blocks, or
  technical restrictions.
- Do not enable a conditional source until Legal/Compliance records its terms,
  approved uses, retention, redistribution, attribution, AI-processing, and
  termination requirements.

## Authoritative references

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [SEC Webmaster FAQ](https://www.sec.gov/about/webmaster-frequently-asked-questions)
- [SEC Privacy and Security Policy](https://www.sec.gov/about/privacy-information)

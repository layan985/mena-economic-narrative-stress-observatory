# Governance

## Purpose

The MENA Open Data & Evidence Lab maintains public research infrastructure whose credibility depends on traceability, versioning, reproducibility, and meaningful separation between production and verification.

The Lab is an institution with founder leadership; it is not a label for founder-produced work. Institutional claims must be supported by attributable work from contributors, reviewers, users, or partners other than the founder.

## Roles

- **Research Director / release maintainer:** coordinates scope, release timing, documentation, partnerships, and repository administration.
- **Dataset lead:** owns a defined dataset or module and is accountable for source coverage, schema compliance, and release readiness.
- **Data contributors:** collect, transcribe, normalize, and document eligible primary-source observations.
- **Method contributors:** propose and document measurement, comparability, annotation, and validation rules.
- **Independent reproducibility reviewers:** rerun or independently audit data, code, or a defined module before a release can claim independent reproduction.
- **External methodological reviewers:** review design, measurement, assumptions, comparability, or validation logic without being the producing analyst.
- **Release reviewers:** verify that required release gates are satisfied before a stable release is approved.

## Contributor status

Contributor status is earned through validated public work, not appointment, affiliation, or appearance on a website.

The default progression is:

`Applicant -> Participant -> Contributor Candidate -> Validated Contributor -> Maintainer`

A person becomes a **Validated Contributor** only after substantive work is attributable in the public project history and has passed review. Qualifying evidence includes a merged pull request, accepted audit, released dataset contribution, validated methods contribution, or another comparably substantive research artifact.

## Decision record

Material methodological decisions must be documented in GitHub issues, pull requests, audit records, or versioned documentation. Decisions that change released values require a changelog entry and a new release version.

## Separation of duties

- No analyst may approve their own work as independently verified.
- Founder-produced work may be released, but it must be labeled accurately until independently reviewed.
- A stable release may not claim independent reproduction unless a non-producing reviewer has completed the public reproduction protocol.
- The principal producer of a release may not satisfy every release gate alone.
- Where feasible, dataset production, methodological review, reproducibility review, and release approval should be performed by different people.

## Release gates

A stable Lab dataset or research object should pass the following gates before release:

1. **Provenance** — source URLs, retrieval dates, transformation history, and rights status are documented.
2. **Schema** — machine-readable schema or data dictionary exists and validation passes.
3. **Reproducibility** — the documented pipeline runs in a fresh environment or deviations are recorded.
4. **Independent review** — a non-producing person reviews the release, methodology, or defined verification target.
5. **Corrections** — review findings are resolved or explicitly documented as unresolved limitations.
6. **Release record** — version tag, changelog, citation metadata, contributor roles, and archive/DOI status are recorded.

No single person may self-certify all six gates.

## Credit

Contributor credit is tied to accepted, attributable public work such as merged pull requests, documented audits, annotation work, methods contributions, released datasets, or co-produced outputs. Titles alone do not create scholarly credit.

Release records should distinguish roles such as project lead, dataset lead, data contributor, methodological reviewer, reproducibility reviewer, and release reviewer.

## Institutional independence standard

The Lab should be able to demonstrate that credible work continues beyond the founder through external contributors, reviewers, users, partners, and non-founder-led outputs. Progress is tracked in `INSTITUTIONAL_INDEPENDENCE.md`.

## Conflicts and corrections

Potential conflicts of interest should be disclosed when they could reasonably affect source selection, interpretation, review, or verification. Corrections follow `CORRECTIONS.md`.

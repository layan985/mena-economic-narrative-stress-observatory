# Observatory Validation Status

Last updated: 9 August 2026.

This ledger separates checks completed by the producing project from evidence supplied by independent third parties. A status is never promoted merely because infrastructure exists for the check.

| Gate | Status | Evidence |
|---|---|---|
| Founder-produced pilot release | PASS | v0.2 repository contents and documented release contract |
| Automated release validation | PASS | GitHub Actions `Validate release` workflow on `main` |
| Automated tests | PASS | repository test suite executed in CI |
| Row-level provenance fields | PRESENT | v0.2 data plus `PROVENANCE.md` |
| Public correction protocol | PRESENT | `CORRECTIONS.md` |
| Reproduction instructions | READY | `REPRODUCE.md` |
| Independent reproduction | PENDING | MODE-007; requires a non-producer verifier record |
| External provenance review | PENDING | requires a completed `audits/PROVENANCE_REVIEW_TEMPLATE.md` by a non-producer reviewer |
| Public immutable GitHub release/tag | PENDING | no GitHub release currently published |
| Zenodo DOI publication | PENDING | reserved DOI `10.5281/zenodo.21845069`; not yet claimed as published |
| v0.3 expanded dataset | PENDING | begins only after external validation and release gates |
| External research use | PENDING | requires documented non-founder use |

## Current claim boundary

The strongest supported description today is:

> Founder-produced, source-traced v0.2 pilot with automated validation, public correction protocols, documented reproduction procedures, and external validation pending.

Do **not** describe the Observatory as independently reproduced, externally provenance-reviewed, DOI-archived, or externally used until the corresponding public evidence exists.

## Promotion rule

A gate moves from `PENDING` to `PASS` only when a durable public artifact supports it. Examples include a third-party audit file or issue, an immutable GitHub release, a published Zenodo record, or a documented external use case.

## Next sequence

1. Complete MODE-007 with a genuinely independent rerun.
2. Complete an external provenance review using the public template.
3. Resolve substantive findings through the correction protocol.
4. Freeze and publish the audited release.
5. Verify the Zenodo record is public before promoting the DOI.
6. Start v0.3 expansion.
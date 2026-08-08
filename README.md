# MENA Economic Narrative and Market Stress Observatory

[![Validate release](https://github.com/layan985/mena-economic-narrative-stress-observatory/actions/workflows/validate.yml/badge.svg)](https://github.com/layan985/mena-economic-narrative-stress-observatory/actions/workflows/validate.yml)

> **Reserved Zenodo DOI:** `10.5281/zenodo.21845069` — **not yet claimed as published**. The DOI will be promoted to the canonical citation only after the Zenodo record is verifiably published.

The **MENA Economic Narrative and Market Stress Observatory: Pilot Release v0.2** is an auditable, source-traced pilot dataset of official consumer-price observations for selected MENA economies and Palestinian geographies. It is maintained by **Layan Oraidi** and the **MENA Open Data & Evidence Lab**.

## Research question

How can official macroeconomic releases, market conditions, policy events, and Arabic/English economic narratives be assembled into comparable country-period evidence about economic stress without hiding missingness, period mismatch, or conflict-related structural breaks?

The pilot answers only the first, narrower measurement question: can official price observations be released with enough row-level provenance and comparability information to support independent checking? It deliberately does **not** publish a composite stress score.

## Release v0.2

- **8** release/geography rows
- **24** populated numeric observations
- **5** official statistical institutions
- direct primary-source URLs and retrieval dates
- explicit period, missingness, comparability, and structural-break notes
- **0** composite scores

Release date: **7 August 2026**. Status: **founder-produced pilot; not yet independently audited**.

## Canonical files

| File | Purpose |
|---|---|
| [`data/raw/mena-observatory-pilot-2026-08-07.csv`](data/raw/mena-observatory-pilot-2026-08-07.csv) | Immutable v0.2 pilot transcription |
| [`data_dictionary.csv`](data_dictionary.csv) | Machine-readable public-field definitions |
| [`METHODOLOGY.md`](METHODOLOGY.md) | Measurement, comparability, structural-break, and publication rules |
| [`PROVENANCE.md`](PROVENANCE.md) | Source-trace and verification requirements |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Roles, authority, credit, and separation of duties |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Public contribution protocol and Founding Researcher Challenge |
| [`CORRECTIONS.md`](CORRECTIONS.md) | Correction, withdrawal, and retraction policy |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |
| [`CITATION.cff`](CITATION.cff) | Machine-readable citation metadata |
| [`scripts/validate_release.py`](scripts/validate_release.py) | Release validator |
| [`tests/test_release.py`](tests/test_release.py) | Automated release test |
| [`.github/workflows/validate.yml`](.github/workflows/validate.yml) | Continuous validation workflow |

Null fields mean **not observed, unavailable, or outside the current release scope**. They never mean zero.

## Reproduce the release checks

The v0.2 validator uses only the Python standard library.

```bash
python scripts/validate_release.py data/raw/mena-observatory-pilot-2026-08-07.csv
python -m unittest discover -s tests -v
```

The validator checks required schema fields, unique record IDs, source URLs, allowed composite-status values, numeric parseability, the 8-row release contract, and the 24 populated numeric observations.

## Methodological boundary

Jordan's figure is a first-half period average and must not be naively ranked beside monthly annual rates. Palestine is retained as separately published overall, West Bank, Jerusalem J1, and Gaza series. Gaza's annual decline follows unprecedented wartime price levels and is flagged as a structural break, not interpreted as low stress or improved welfare.

## Publication gate

The Observatory ultimately targets four layers: **macro, markets, policy, and bilingual narrative evidence**.

A composite is withheld until required coverage, provenance, licensing, reproducibility, comparability, structural-break treatment, and independent verification gates are satisfied.

> **Missing components are never converted into reassuring zeros.**

## Public roadmap

The research roadmap is now tracked as GitHub issues:

- [MODE-001 — Assess and appoint four founding workers](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/1)
- [MODE-002 — Freeze country-entry and source-eligibility rules](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/2)
- [MODE-003 — Publish Arabic-English annotation guide](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/3)
- [MODE-004 — Audit licensing and redistribution source by source](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/4)
- [MODE-005 — Publish pilot schema and first official-data cut](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/5)
- [MODE-006 — Secure one substantive partner](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/6)
- [MODE-007 — Independent rerun of package v0.2](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/7)
- [MODE-008 — Publish first workshop artifact](https://github.com/layan985/mena-economic-narrative-stress-observatory/issues/8)

## Citation

Until the Zenodo deposit is published, cite the version explicitly:

> Oraidi, L. (2026). *MENA Economic Narrative and Market Stress Observatory: Pilot Release v0.2*. MENA Open Data & Evidence Lab. Version 0.2.

## Corrections and contributions

Suspected errors should be opened as GitHub issues with the affected record ID and primary-source evidence. Published releases are never overwritten silently. Material corrections require a new version and documented review.

Contributor credit begins with accepted, auditable public work—not honorary titles.

## Project links

- **Repository:** https://github.com/layan985/mena-economic-narrative-stress-observatory
- **Lab:** https://mena-open-evidence-lab.r8ms5bfzb6.chatgpt.site/

Founded and directed by **Layan Oraidi**.
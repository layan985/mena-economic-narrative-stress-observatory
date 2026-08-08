# MENA Economic Narrative and Market Stress Observatory

[![Release](https://img.shields.io/badge/release-v0.2-0f766e)](https://github.com/layan985/mena-economic-narrative-stress-observatory/releases/tag/v0.2)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21845069.svg)](https://doi.org/10.5281/zenodo.21845069)
[![Validate release](https://github.com/layan985/mena-economic-narrative-stress-observatory/actions/workflows/validate.yml/badge.svg)](https://github.com/layan985/mena-economic-narrative-stress-observatory/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

> **Zenodo DOI:** [10.5281/zenodo.21845069](https://doi.org/10.5281/zenodo.21845069)

The **MENA Economic Narrative and Market Stress Observatory: Pilot Release v0.2** is an auditable, source-traced pilot dataset of official consumer-price observations for selected MENA economies and Palestinian geographies. It is maintained by [Layan Oraidi](https://orcid.org/0009-0002-1946-3411) and the MENA Open Data & Evidence Lab.

## Research question

How can official macroeconomic releases, market conditions, policy events, and Arabic/English economic narratives be assembled into comparable country-period evidence about economic stress without hiding missingness, period mismatch, or conflict-related structural breaks?

The pilot answers only the first, narrower measurement question: can official price observations be released with enough row-level provenance and comparability information to support independent checking? It deliberately does **not** publish a composite stress score.

## Release v0.2

- 8 release/geography rows;
- 24 populated numeric observations;
- 5 official statistical institutions;
- direct primary-source URLs and retrieval dates;
- explicit period, missingness, comparability, and structural-break notes;
- 0 composite scores.

Release date: **7 August 2026**. Status: **founder-produced pilot; not yet independently audited**.

## Data files

| File | Purpose |
|---|---|
| `data/raw/mena-observatory-pilot-2026-08-07.csv` | Immutable transcription published with the original Lab pilot |
| `data/processed/mena-observatory-pilot-v0.2.csv` | Validated wide release generated from the immutable transcription |
| `data/processed/observations_long.csv` | One row per populated numeric observation (24 rows) |
| `data/processed/sources.csv` | Deduplicated source-institution ledger |
| `data_dictionary.csv` | Machine-readable definitions for public release fields |
| `provenance/release_manifest.json` | Checksums, row counts, observation counts, and build metadata |

Null fields mean **not observed or outside the release scope**. They never mean zero.

## Reproduce the release

The build uses only the Python standard library.

```bash
python scripts/process_data.py
python scripts/validate_release.py
python -m unittest discover -s tests -v
```

`process_data.py` reads the immutable pilot transcription and deterministically rebuilds every file under `data/processed/` plus the provenance manifest. CI runs the same validation on every push and pull request.

## Methodological boundary

Jordan's figure is a first-half period average and is not ranked beside monthly annual rates. Palestine is retained as separately published overall, West Bank, Jerusalem J1, and Gaza series. Gaza's annual decline follows unprecedented wartime price levels and is flagged as a structural break, not interpreted as low stress or improved welfare. See [METHODOLOGY.md](METHODOLOGY.md) and [PROVENANCE.md](PROVENANCE.md).

## Citation

Until the DOI is issued, cite:

> Oraidi, L. (2026). *MENA Economic Narrative and Market Stress Observatory: Pilot Release v0.2*. MENA Open Data & Evidence Lab. Version 0.2.

Machine-readable citation metadata are in [CITATION.cff](CITATION.cff).

## Corrections and contributions

Report suspected errors through a GitHub issue using the `correction` label. Published releases are never overwritten silently; changed cells require a new patch release and a verifier. See [CORRECTIONS.md](CORRECTIONS.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Except where an upstream source states otherwise, the dataset, documentation, and repository materials are licensed under [CC BY 4.0](LICENSE). The license does not replace or alter the terms of the linked primary-source websites.

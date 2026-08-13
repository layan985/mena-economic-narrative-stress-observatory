# MENA economic narrative and market stress: price-data pilot

Official inflation releases can look comparable while referring to different periods, geographies, and populations. Jordan's pilot observation is a first-half period average; several other rows are monthly annual rates; and Gaza's annual price decline follows an exceptional wartime price level. Putting those numbers into one ranking would create a precise-looking but misleading result.

This repository contains a versioned official-price-release panel built around that measurement problem. It does not claim to contain a regional stress index.

## Current status

**v0.3.0-rc1 is a founder-produced release candidate.** Data transcription and automated validation are complete for its fixed January–June 2026 scope. Independent source audit, immutable source archiving/hashing, and DOI publication are still pending. It must not be described as independently reproduced or as a stable DOI release.

The release candidate contains:

- 48 geography-month rows;
- 30 primary institution-month rows plus 18 separately published Palestinian regional rows;
- 195 populated numeric observations;
- sources from 5 official statistical institutions;
- 30 unique official release URLs with retrieval dates, period descriptions, and comparability notes;
- complete headline annual and month-on-month CPI fields for every row;
- no composite score.

The release candidate has automated checks, but no person outside the project has reproduced or source-audited it. There is no published Zenodo record and no documented outside use. [VALIDATION_STATUS.md](VALIDATION_STATUS.md) and [V0_3_RELEASE_GATE.md](V0_3_RELEASE_GATE.md) keep those boundaries explicit.

## Why I did not calculate a stress score

Three issues appeared immediately:

1. Jordan's first-half period average is not the same object as a monthly year-on-year rate.
2. Palestine, the West Bank, Jerusalem J1, and Gaza are published as distinct series and should not be collapsed without an explicit aggregation rule.
3. Gaza's large annual decline reflects wartime base effects and cannot be read mechanically as falling hardship.

The pilot's result is therefore the source table plus those warnings rather than a knowingly misleading ranking. [notes/2026-08-10-why-i-dropped-the-composite.md](notes/2026-08-10-why-i-dropped-the-composite.md) records the decision.

## Files

- [data/raw/mena-observatory-v0.3.0-rc1.csv](data/raw/mena-observatory-v0.3.0-rc1.csv): full 48-row release-candidate transcription.
- [data/processed/headline-monthly-panel-v0.3.0-rc1.csv](data/processed/headline-monthly-panel-v0.3.0-rc1.csv): focused 30-row primary panel.
- [data/processed/observatory-v0.3.0-rc1-summary.json](data/processed/observatory-v0.3.0-rc1-summary.json): machine-generated coverage/status summary.
- [data/provenance/source-manifest-v0.3.0-rc1.csv](data/provenance/source-manifest-v0.3.0-rc1.csv): 30-source provenance ledger with archive/hash status.
- [data/raw/mena-observatory-pilot-2026-08-07.csv](data/raw/mena-observatory-pilot-2026-08-07.csv): frozen v0.2 eight-row pilot.
- [data_dictionary.csv](data_dictionary.csv): field definitions.
- [METHODOLOGY.md](METHODOLOGY.md): source, missingness, and comparability rules.
- [PROVENANCE.md](PROVENANCE.md): how source documents are recorded.
- [RIGHTS_LEDGER.md](RIGHTS_LEDGER.md): source-specific reuse notes.
- [RESULTS.md](RESULTS.md): what can and cannot be concluded from the pilot.
- [PILOT_RELEASE.md](PILOT_RELEASE.md): exact v0.2 completion boundary.

Blank numeric fields mean not observed, unavailable, or outside the source's scope. They do not mean zero.

## Run the checks

The validator uses only the Python standard library.

```bash
python scripts/validate_release.py data/raw/mena-observatory-pilot-2026-08-07.csv
python scripts/validate_v03.py data/raw/mena-observatory-v0.3.0-rc1.csv
python scripts/build_v03_release.py
python -m unittest discover -s tests -v
```

The v0.3 checks enforce all 48 geography-period pairs, the 30/18 primary-regional split, five official institutions, HTTPS sources, required headline fields, structural-break status, and numeric parsing. They do not establish source transcription accuracy, economic comparability, or independent verification.

## Release boundary

No new country, month, market layer, narrative model, or composite enters this release candidate. The next work is source audit, source archiving/hashing where rights permit, correction of discrepancies, a clean-room reproduction, and DOI publication of the resulting stable release.

Corrections should identify the affected `record_id` and link the primary source. Existing releases are not silently overwritten.

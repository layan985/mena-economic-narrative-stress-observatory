# MENA economic narrative and market stress: price-data pilot

Official inflation releases can look comparable while referring to different periods, geographies, and populations. Jordan's pilot observation is a first-half period average; several other rows are monthly annual rates; and Gaza's annual price decline follows an exceptional wartime price level. Putting those numbers into one ranking would create a precise-looking but misleading result.

This repository contains the dataset I used to work through that measurement problem. It does not claim to contain a regional stress index.

## Current status

**v0.2 is a completed founder-produced pilot research object.** Its release boundary is frozen in [PILOT_RELEASE.md](PILOT_RELEASE.md) and on the `release/v0.2-pilot` branch. External reproduction, provenance review, DOI archiving, and a larger v0.3 dataset are separate maturity gates rather than unfinished components of the v0.2 pilot itself.

The completed pilot contains:

- 8 release/geography rows;
- 24 populated numeric observations;
- sources from 5 official statistical institutions;
- source URLs, retrieval dates, period descriptions, and comparability notes;
- no composite score.

The pilot has automated checks, but no person outside the project has reproduced or reviewed it. There is no published Zenodo record and no documented outside use. [VALIDATION_STATUS.md](VALIDATION_STATUS.md) keeps that status explicit.

## Why I did not calculate a stress score

Three issues appeared immediately:

1. Jordan's first-half period average is not the same object as a monthly year-on-year rate.
2. Palestine, the West Bank, Jerusalem J1, and Gaza are published as distinct series and should not be collapsed without an explicit aggregation rule.
3. Gaza's large annual decline reflects wartime base effects and cannot be read mechanically as falling hardship.

The pilot's result is therefore the source table plus those warnings rather than a knowingly misleading ranking. [notes/2026-08-10-why-i-dropped-the-composite.md](notes/2026-08-10-why-i-dropped-the-composite.md) records the decision.

## Files

- [data/raw/mena-observatory-pilot-2026-08-07.csv](data/raw/mena-observatory-pilot-2026-08-07.csv): the eight-row transcription.
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
python -m unittest discover -s tests -v
```

The tests check the schema, unique record IDs, numeric parsing, source URLs, the eight-row count, and the 24 populated numeric observations. They do not establish that the rows are economically comparable or independently verified.

## Next research version

A future v0.3 should choose a narrower construct, collect consistent time periods, encode conflict-specific interpretation rules, materially expand source coverage, and add non-founder checking. Those are expansion goals, not conditions for calling the existing v0.2 pilot complete.

Corrections should identify the affected `record_id` and link the primary source. Existing releases are not silently overwritten.

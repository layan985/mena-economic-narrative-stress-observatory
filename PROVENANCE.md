# Provenance Policy

Every public observation must be traceable to a source that an independent reviewer can identify and inspect.

## Required fields

For each released row, record at minimum:

- stable `record_id`;
- geography and reference period;
- source institution;
- direct source URL;
- retrieval date;
- measurement type;
- comparability note when the row is non-standard, structurally affected, or otherwise unsafe to compare naively.

## Source rules

Primary official sources are preferred. Secondary summaries may be used for discovery but must not silently replace an available primary release.

A source change, rebasing, methodological revision, boundary change, or conflict-related disruption must be documented before the affected observations are used in comparative inference.

## Transformation rules

Raw transcriptions are preserved. Transformations into processed or long-form data must be deterministic and code-generated where practical. Manual edits to derived files are prohibited.

## Verification

No producer should be the sole verifier of their own release. Independent checking should reproduce the relevant source trace, transformation, and validation results and record discrepancies publicly.

## Uncertainty

When provenance is incomplete, the observation may be retained for investigation but must not be promoted into a published composite merely to improve coverage.

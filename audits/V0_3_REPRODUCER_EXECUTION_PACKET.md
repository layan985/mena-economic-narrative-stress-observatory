# v0.3 Independent Reproducer Execution Packet

## Purpose

Attempt to regenerate the v0.3 release-candidate outputs from the repository's documented starting materials without relying on unpublished author state.

This is separate from source review. A successful clean run can support `INDEPENDENT REPRODUCTION` only after a non-author completes and signs the reproduction record.

## Fixed object

Version: `v0.3.0-rc1`

Expected public outputs:
- `data/processed/headline-monthly-panel-v0.3.0-rc1.csv`
- `data/processed/observatory-v0.3.0-rc1-summary.json`
- `data/provenance/source-manifest-v0.3.0-rc1.csv`

## Starting rule

The reproducer should begin from a fresh checkout at the exact commit being tested and document:

- operating system
- Python version
- dependency installation method
- repository commit
- commands executed
- start and finish time
- any undocumented manual intervention

Do not use author-generated local files outside the repository.

## Procedure

1. Clone or download the repository at the tested commit.
2. Create a clean Python environment.
3. Install only the dependencies documented by the repository.
4. Run the repository's validation procedure.
5. Run the v0.3 release build procedure.
6. Compare regenerated outputs to the committed candidate outputs.
7. Record exact differences, including ordering-only differences.
8. Record any missing dependency, platform assumption, hidden input, manual step, or network dependency.
9. Complete `audits/V0_3_INDEPENDENT_REPRODUCTION_RECORD.md`.

## Success criterion

`success_exact`:
- documented commands execute in a clean environment
- required outputs regenerate
- regenerated substantive values equal the committed candidate values
- any byte-level differences are explained and non-substantive
- no undocumented source data or author-only state is required

`success_with_documented_difference`:
- outputs regenerate with a known non-substantive difference such as ordering or environment-specific metadata
- difference is documented and does not alter the research object

`failure`:
- required outputs do not regenerate, an undocumented input is required, or substantive values differ without resolution

## Deliverables

Return:

1. completed `audits/V0_3_INDEPENDENT_REPRODUCTION_RECORD.md`
2. command transcript or concise command log
3. checksums of regenerated outputs when feasible
4. any discrepancy files needed to explain differences

## Interpretation boundary

A successful reproduction shows that the documented computational transformation can be rerun. It does not independently verify whether the official source values were transcribed correctly. Source correctness is the job of the external source audit.

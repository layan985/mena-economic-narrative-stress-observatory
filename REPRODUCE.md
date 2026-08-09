# Reproduce Observatory v0.2

This guide is designed for an independent verifier who did not produce the pilot release. The goal is to make the reproduction procedure explicit enough that the verifier should not need private instructions from the producing analyst.

## 1. Obtain the repository

```bash
git clone https://github.com/layan985/mena-economic-narrative-stress-observatory.git
cd mena-economic-narrative-stress-observatory
```

Before running anything, record the exact research object:

```bash
git rev-parse HEAD
```

Copy that commit SHA into `audits/INDEPENDENT_REPRODUCTION_TEMPLATE.md` together with the operating system and Python version.

> Until a GitHub/Zenodo release is formally published, the verifier must report the exact commit SHA rather than treating `main` as an immutable release.

## 2. Environment

The v0.2 release validator and tests use only the Python standard library. No project-specific Python dependencies are required for the core reproduction checks.

Record:

```bash
python --version
```

## 3. Run the release validator

```bash
python scripts/validate_release.py data/raw/mena-observatory-pilot-2026-08-07.csv
```

The validator checks the release contract, including required schema fields, unique record IDs, source URLs, allowed composite-status values, numeric parseability, the expected 8 release/geography rows, and 24 populated numeric observations.

## 4. Run the automated tests

```bash
python -m unittest discover -s tests -v
```

Record the full result as PASS or FAIL. Do not edit the dataset to make a failing check pass.

## 5. Independently spot-check official sources

Select at least three records spanning more than one source institution where possible. For each sampled record:

1. Open the primary official source recorded by the project.
2. Confirm the institution and release are identifiable.
3. Confirm the published value and period definition.
4. Compare the official value with the value transcribed in the Observatory.
5. Record any unit, period, geography, or comparability discrepancy.

Use `audits/INDEPENDENT_REPRODUCTION_TEMPLATE.md` for the result.

## 6. Report discrepancies publicly

Every substantive discrepancy should become a GitHub issue containing:

- affected `record_id`;
- observed value or metadata;
- expected value or metadata;
- primary-source evidence;
- whether the discrepancy changes the released data or only documentation.

Do not silently repair the audited object.

## 7. Reproduction verdict

The independent verifier should choose exactly one verdict:

- Reproduced without substantive discrepancy
- Reproduced with documented non-substantive discrepancies
- Did not reproduce

The producing analyst may respond to issues and make later corrections, but must not rewrite the verifier's observed result.

## 8. Submit the audit record

Preferred public routes:

1. Open a pull request adding a completed file under `audits/`, for example `audits/independent-reproduction-001.md`; or
2. Attach the completed record to MODE-007 and link any discrepancy issues.

A reproduction does not count as independent if the producing analyst ran the checks on the verifier's behalf or supplied undocumented private fixes.
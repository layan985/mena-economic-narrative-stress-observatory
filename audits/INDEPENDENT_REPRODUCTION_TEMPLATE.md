# Independent Reproduction Record

Use this template for MODE-007. The verifier must not be the producing analyst.

## Verifier

- Name:
- Affiliation (if any):
- GitHub/ORCID:
- Date:
- Relationship to project:

## Exact research object

- Repository:
- Release/tag:
- Commit SHA:
- Dataset file and checksum:

## Environment

- Operating system:
- Python version:
- Installation commands:

## Commands run

```bash
python scripts/validate_release.py data/raw/mena-observatory-pilot-2026-08-07.csv
python -m unittest discover -s tests -v
```

Additional commands:

```text

```

## Automated result

- Validator: PASS / FAIL
- Tests: PASS / FAIL
- Unexpected warnings/errors:

## Primary-source spot checks

| record_id | official source checked | released value | independently observed value | period definition matches? | result |
|---|---|---:|---:|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

## Reproduction verdict

Choose one:

- [ ] Reproduced without substantive discrepancy
- [ ] Reproduced with documented non-substantive discrepancies
- [ ] Did not reproduce

## Discrepancies

For every discrepancy, link a GitHub issue rather than silently correcting the release.

- Issue(s):
- Description:

## Verifier statement

I independently ran the commands and checks recorded above against the stated commit/release. This record reflects what I observed and has not been written or approved as a result claim by the producing analyst.

Name/date:

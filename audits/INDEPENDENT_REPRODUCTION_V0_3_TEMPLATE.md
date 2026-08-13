# Independent Reproduction Record — v0.3

The verifier must not be the producing analyst.

## Verifier and independence

- Name:
- Affiliation, if any:
- GitHub/ORCID:
- Contact:
- Audit dates:
- Relationship to the project or founder:
- Compensation or other conflict disclosure:

## Exact object

- Repository URL:
- Commit SHA:
- Release/tag, if any:
- Raw file SHA-256:
- Focused-panel SHA-256:

## Environment and commands

- Operating system:
- Python version:
- Fresh clone used: yes / no

```bash
python scripts/validate_v03.py data/raw/mena-observatory-v0.3.0-rc1.csv
python scripts/build_v03_release.py
python -m unittest discover -s tests -v
```

- Validator result: PASS / FAIL
- Tests result: PASS / FAIL
- Regenerated focused panel matches committed file: yes / no
- Regenerated summary matches committed file: yes / no
- Regenerated source manifest matches committed file: yes / no

## Independent official-source checks

Check at least one row from every institution, at least three reference months, and one conflict-affected Palestine/Gaza row with its matching West Bank or Jerusalem J1 row.

| record_id | official source | released annual rate | observed annual rate | released monthly rate | observed monthly rate | period/geography match | result |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Discrepancies

List every discrepancy before any repair. Link issues or pull requests and preserve the original observation after a fix.

## Scope boundary

This audit does not by itself establish cross-country comparability, welfare interpretation, causal inference, or a valid regional composite. State any additional boundary discovered during review.

## Verdict

- [ ] Reproduced without substantive discrepancy
- [ ] Reproduced with documented non-substantive discrepancies
- [ ] Did not reproduce
- [ ] Incomplete audit; no reproduction conclusion

## Verifier statement

I independently ran the recorded checks against the stated commit, reviewed the listed official sources, disclosed relevant relationships, and did not silently remove discrepancies.

- Name/date:
- Verifiable public report or signature, if used:

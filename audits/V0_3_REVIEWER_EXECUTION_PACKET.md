# v0.3 Reviewer Execution Packet

## Object under review

Release candidate: `v0.3.0-rc1`

Fixed scope:
- January–June 2026
- five official statistical institutions
- 30 primary institution-month rows
- 18 separately published Palestinian regional rows
- 48 complete headline annual and month-on-month observations
- no composite, country ranking, welfare interpretation, or stress index

The purpose of this review is narrow: verify that the release candidate faithfully represents the cited official source material and that the published provenance is sufficient for another researcher to trace each checked observation.

## Reviewer independence rule

The reviewer must not be the release author and must not rely on the author's transcription as the sole source of truth.

A completed review can support the label `EXTERNAL REVIEW` only when the review record identifies the reviewer, date, scope, version reviewed, sample examined, method, findings, Lab response, and attribution permission.

## Minimum source-audit sample

Review at least one primary release from each institution:

1. Department of Statistics (Jordan)
2. General Authority for Statistics (Saudi Arabia)
3. Haut-Commissariat au Plan (Morocco)
4. National Institute of Statistics (Tunisia)
5. Palestinian Central Bureau of Statistics

For the Palestinian Central Bureau of Statistics, inspect at least one month where regional observations are present and verify the relationship between the primary release and the separately recorded regional rows.

Recommended minimum: 10 source rows, including at least one January and one June observation and at least one source delivered as PDF.

## What to verify for each sampled source

Record each check in `audits/v0.3-source-audit.csv`.

- source URL resolves or failure is documented
- source institution is correct
- reference period is correct
- headline annual rate matches the official source
- headline month-on-month rate matches the official source
- regional role, where present, is represented correctly
- units and sign are correct
- nulls are source-defined rather than silently imputed
- source locator is precise enough for another reader to find the value
- rights/archive treatment is appropriate for the source
- any discrepancy is classified and described

## Discrepancy classes

Use exactly one primary class per issue:

- `none`
- `transcription_error`
- `source_locator_weak`
- `period_mismatch`
- `unit_or_sign_error`
- `regional_role_error`
- `rights_or_archive_issue`
- `source_unavailable`
- `methodology_ambiguity`
- `other`

Severity:

- `minor`: does not alter a reported numeric value or interpretation
- `material`: alters a value, period, unit, role, provenance claim, or reproducibility claim
- `blocking`: prevents a stable release from satisfying the published release gate

## Reviewer deliverables

Return:

1. completed `audits/v0.3-source-audit.csv`
2. completed `audits/V0_3_EXTERNAL_REVIEW_RECORD.md`
3. any annotated source notes necessary to explain discrepancies
4. an explicit recommendation: `release`, `release_after_corrections`, or `do_not_release`

## Lab response rule

Every material or blocking issue must receive one of:

- corrected in the candidate and linked to a commit
- retained as a documented limitation with rationale
- release blocked pending resolution

The reviewer does not need to approve the Lab response. The record should distinguish what the reviewer found from what the Lab decided.

## What this review does not establish

This review does not establish causal validity, institutional independence, statistical-agency quality, or regional representativeness beyond the fixed object. It also does not count as independent reproduction unless the reviewer separately runs the reproduction procedure from the documented starting materials.

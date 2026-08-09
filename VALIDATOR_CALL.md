# Call for Independent Validators — Observatory v0.2

The MENA Economic Narrative and Market Stress Observatory is seeking **two independent external validators** for its pilot release v0.2.

The current object is intentionally small: **8 release/geography rows, 24 populated numeric observations, and 5 official statistical institutions**. The goal is not to endorse the project. The goal is to determine, publicly and independently, whether the released object can be reproduced and whether sampled source traces are correct.

## Track A — Independent reproduction (MODE-007)

A verifier who did not produce the pilot release should:

1. clone the public repository;
2. record the exact commit SHA and environment;
3. run the documented validator and tests in `REPRODUCE.md`;
4. independently spot-check at least three primary-source records;
5. record discrepancies without silently fixing the audited object; and
6. submit a completed `audits/INDEPENDENT_REPRODUCTION_TEMPLATE.md` through a pull request or linked public issue record.

The producing analyst will not run the checks on the verifier's behalf and will not determine the verdict.

## Track B — External provenance review (MODE-009)

A separate reviewer should independently inspect a sample of at least five records where feasible and verify:

- source institution;
- primary-source URL/document;
- geography;
- reference period;
- reported value;
- unit/definition;
- transcription;
- transformation documentation; and
- comparability or structural-break notes where applicable.

Use `audits/PROVENANCE_REVIEW_TEMPLATE.md`. Each sampled record should receive one of four outcomes: `PASS`, `MINOR`, `MAJOR`, or `UNVERIFIABLE`.

## Independence standard

A validator must not be the producing analyst and should disclose any relationship to the project. A reviewer does **not** need to agree with the project's methodology or conclusions. Critical findings are useful and will be preserved in the public audit record.

## What counts as completion

A validation only counts when the evidence is durable and public:

- exact commit/release identified;
- commands/checks documented;
- findings recorded;
- discrepancies linked to public issues where substantive; and
- reviewer identity and date included.

Private messages saying “looks good” do not count.

## Credit

Completed substantive validation work will be acknowledged in the relevant public audit record and project contributor history. Credit reflects the work actually performed and does not imply authorship of the underlying dataset.

## How to volunteer

Comment on:

- **MODE-007** for independent reproduction; or
- **MODE-009** for provenance review.

Please state which track you want to take, your affiliation or research background (if any), and whether you have any prior involvement with the project.

Repository: https://github.com/layan985/mena-economic-narrative-stress-observatory

The Observatory will continue to describe v0.2 as **founder-produced and not independently audited** until the corresponding external evidence is actually completed and public.
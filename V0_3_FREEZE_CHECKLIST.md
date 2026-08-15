# v0.3 Stable Freeze Checklist

This checklist controls promotion of `v0.3.0-rc1` to a stable v0.3 release. It records evidence required for promotion; it does not itself satisfy any gate.

## A. Fixed object

- [x] Scope frozen at January–June 2026.
- [x] Five official statistical institutions.
- [x] 30 primary institution-month rows.
- [x] 18 separately published Palestinian regional rows.
- [x] No composite, ranking, welfare interpretation, or regional stress index.

## B. Computational package

- [x] Raw release-candidate table committed.
- [x] Processed headline panel committed.
- [x] Release summary committed.
- [x] Machine-readable source manifest committed.
- [x] Build script committed.
- [x] Automated validation available.
- [x] Reproduction instructions available.
- [ ] Non-author clean-environment reproduction completed and recorded.

Evidence when complete: `audits/V0_3_INDEPENDENT_REPRODUCTION_RECORD.md` with a successful result tied to an exact commit.

## C. Source and rights package

- [x] Each source has institution, period, URL, and retrieval date.
- [ ] Each source has final archive treatment.
- [ ] Each redistributable archived source object has SHA-256.
- [ ] Each link-only source has final source-specific rights rationale.
- [ ] External source audit covers every institution and the required regional-role check.

Evidence when complete:
- `data/provenance/source-manifest-v0.3.0-rc1.csv`
- `audits/v0.3-source-audit.csv`
- `audits/V0_3_EXTERNAL_REVIEW_RECORD.md`

## D. Discrepancy closure

- [ ] Every material or blocking review discrepancy is corrected, retained as an explicit limitation, or blocks release.
- [ ] Any substantive correction receives second-person verification before the stable release claims independent checking.
- [ ] Correction commits are linked from the review record where applicable.

## E. Stable archive

- [ ] Final candidate commit is identified after review and reproduction.
- [ ] Stable GitHub release freezes that exact commit.
- [ ] Stable release files have a checksum manifest.
- [ ] DOI archive resolves to the exact stable release.
- [ ] Citation metadata points to the stable version and DOI.
- [ ] Public Lab release registry is updated only after the stable object exists.

## Promotion rule

Promotion is blocked while any unchecked item in B–E remains required by the published release gate. A release manager must not convert an absence of findings, an internal rerun, or an invitation sent to a reviewer into evidence that the gate is complete.

## Stable-label rule

Before promotion, permitted labels remain:

- `v0.3.0-rc1`
- `founder-produced release candidate`
- `automated validation passing`
- `independent audit pending`
- `DOI pending`

`EXTERNAL REVIEW` and `INDEPENDENT REPRODUCTION` may be added only after their corresponding completed records exist. `stable release` and `stable DOI release` may be used only after section E is complete.

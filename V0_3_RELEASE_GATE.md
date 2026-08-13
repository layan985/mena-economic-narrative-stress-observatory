# v0.3 Stable Release Gate

## Current status

**v0.3.0-rc1 — founder-produced release candidate.**  
Data transcription and automated validation are complete for the fixed scope. Independent source audit, source-byte archiving/hashing, and DOI publication are pending.

## Fixed research object

- January–June 2026 only
- five official statistical institutions
- 30 primary institution-month rows
- 18 separately published Palestinian regional rows
- 48 complete headline annual and month-on-month observations
- no composite, market score, country ranking, or welfare interpretation

No new geography, month, or evidence layer enters v0.3 before the existing object passes review.

## Gate status

### Coverage and schema

- [x] All 48 fixed geography-month rows exist.
- [x] All 48 headline annual rates are populated.
- [x] All 48 month-on-month rates are populated.
- [x] All 30 primary and 18 regional roles are machine-enforced.
- [x] Source-defined optional components remain null rather than being imputed.

### Provenance and rights

- [x] All rows identify the official institution, source URL, and retrieval date.
- [x] The 30 unique official releases have a machine-readable provenance ledger.
- [ ] Permitted source bytes are archived and SHA-256 hashed.
- [ ] Link-only or non-redistributable sources have final source-specific rights notes.
- [ ] An outside reviewer checks at least one row from every institution.

### Reproducibility and correction

- [x] Version-specific validation passes.
- [x] The focused panel, summary, and source manifest regenerate from code.
- [ ] A non-author completes the public v0.3 reproduction template.
- [ ] Discrepancies are logged and resolved or retained as limitations.
- [ ] A second person verifies any substantive correction before a stable release claims independent checking.

### Citation and archive

- [x] Release-candidate citation metadata exists.
- [ ] A stable GitHub release freezes the reviewed commit.
- [ ] A DOI archive resolves to that exact release.
- [ ] The public site links the stable data, methodology, audit, and DOI.

## Permitted labels

Before all gates close, use:

- **v0.3.0-rc1**
- **founder-produced release candidate**
- **automated validation passing**
- **independent audit pending**
- **DOI pending**

Do not use **independently reproduced**, **externally validated**, **regional stress index**, or **stable DOI release**.

## Stop rule

The next unit of work is external checking, not a seventh month, sixth institution, new dashboard, or composite. Scope expansion resumes only after the reviewed v0.3 release is archived or the gate is explicitly revised with a public reason.

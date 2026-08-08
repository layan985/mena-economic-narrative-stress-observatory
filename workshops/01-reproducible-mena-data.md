# Workshop 01 — Reproducible MENA Economic Data

**Host:** MENA Open Data & Evidence Lab  
**Instructor:** Layan Oraidi  
**Format:** 75 minutes, live coding + audit exercise  
**Audience:** undergraduate researchers, early-stage RAs, policy-data users  
**Prerequisites:** basic Python or spreadsheet familiarity  

## Learning objectives

By the end of the workshop, participants should be able to:

1. distinguish a source-traced research dataset from a spreadsheet of copied numbers;
2. preserve period definitions, missingness, structural breaks, and provenance;
3. run the Observatory validator and tests;
4. independently recheck a released observation against its official source;
5. create an auditable correction issue instead of silently editing published data;
6. query the Observatory JSON API without discarding comparability metadata.

## Agenda

### 0–10 min — Why reproducibility fails

- copied values without source dates;
- country names that change across files;
- monthly rates mixed with period averages;
- missing values converted to zero;
- wartime structural breaks interpreted mechanically;
- unpublished scripts and undocumented manual edits.

### 10–25 min — Anatomy of an auditable row

Open the pilot CSV and inspect:

- `record_id`
- `geography`
- `reference_period`
- `measure_type`
- outcome fields
- `source_institution`
- `source_url`
- `retrieved_date`
- `comparability_note`
- `composite_status`

Exercise: explain why the Jordan H1 observation should not be ranked directly beside a monthly annual rate.

### 25–40 min — Reproduce the release checks

```bash
python scripts/validate_release.py data/raw/mena-observatory-pilot-2026-08-07.csv
python -m unittest discover -s tests -v
```

Participants record:

- operating system;
- Python version;
- commit SHA;
- commands run;
- pass/fail result.

### 40–55 min — Independent source audit

Each participant selects one row, opens the linked official statistical release, and records:

- value shown by the source;
- period definition;
- publication date if available;
- whether the Observatory transcription matches;
- any caveat omitted from the row.

Discrepancies become GitHub issues with the affected `record_id`.

### 55–65 min — Query the API

Example after deployment:

```text
GET /api?geography=Tunisia
```

Discuss why an API response must retain methodological fields rather than expose only headline numbers.

### 65–75 min — Mini replication handoff

Participants exchange audit records. A second person reruns the check and signs off or opens a discrepancy.

## Evidence required for the workshop milestone

The workshop counts as **taught** only when there is external evidence of delivery, such as:

- event page or registration form;
- dated slide deck or handout;
- attendee list or anonymized attendance count;
- recording or screenshots;
- participant-submitted audit issue/PR;
- short post-event report.

Drafting this curriculum alone does not count as teaching the workshop.

## Suggested public outputs

- workshop slides;
- participant audit template;
- one completed independent source audit;
- event recap with attendance and outcomes;
- Zenodo archive of teaching materials for a DOI-backed object.

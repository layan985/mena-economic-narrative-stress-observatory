#!/usr/bin/env python3
import csv
import json
from collections import Counter
from pathlib import Path

from validate_v03 import validate_v03

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "mena-observatory-v0.3.0-rc1.csv"
PROCESSED = ROOT / "data" / "processed"
PROVENANCE = ROOT / "data" / "provenance"
PRIMARY = PROCESSED / "headline-monthly-panel-v0.3.0-rc1.csv"
SUMMARY = PROCESSED / "observatory-v0.3.0-rc1-summary.json"
SOURCE_MANIFEST = PROVENANCE / "source-manifest-v0.3.0-rc1.csv"


def main():
    failures = validate_v03(RAW)
    if failures:
        raise SystemExit("\n".join(failures))

    with RAW.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    primary_rows = [row for row in rows if row["measure_type"] == "monthly_annual_rate"]
    primary_rows.sort(key=lambda row: (row["geography"], row["reference_period"]))

    PROCESSED.mkdir(parents=True, exist_ok=True)
    primary_fields = [
        "record_id", "geography", "reference_period", "headline_cpi_annual_pct",
        "cpi_month_on_month_pct", "source_institution", "source_url",
        "retrieved_date", "composite_status", "comparability_note",
    ]
    with PRIMARY.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=primary_fields)
        writer.writeheader()
        writer.writerows({field: row[field] for field in primary_fields} for row in primary_rows)

    numeric_fields = [
        "headline_cpi_annual_pct", "cpi_month_on_month_pct", "food_cpi_annual_pct",
        "housing_cpi_annual_pct", "core_cpi_annual_pct", "prior_period_headline_pct",
        "usd_exchange_rate_local_per_usd",
    ]
    summary = {
        "status": "v0.3.0-rc1; founder-produced; independent audit pending",
        "rows": len(rows),
        "primary_institution_month_rows": len(primary_rows),
        "supplemental_palestinian_regional_rows": len(rows) - len(primary_rows),
        "reference_periods": sorted({row["reference_period"] for row in rows}),
        "official_source_institutions": sorted({row["source_institution"] for row in rows}),
        "unique_source_urls": len({row["source_url"] for row in rows}),
        "headline_annual_complete": sum(bool(row["headline_cpi_annual_pct"]) for row in rows),
        "month_on_month_complete": sum(bool(row["cpi_month_on_month_pct"]) for row in rows),
        "populated_numeric_observations": sum(bool(row[field]) for row in rows for field in numeric_fields),
        "composite_status_counts": dict(sorted(Counter(row["composite_status"] for row in rows).items())),
        "composite_published": False,
        "independently_reproduced": False,
        "doi_published": False,
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    source_rows = {}
    for row in rows:
        source_rows[row["source_url"]] = {
            "source_id": f"SRC-{row['record_id'].split('-')[0]}-{row['reference_period']}",
            "source_institution": row["source_institution"],
            "reference_period": row["reference_period"],
            "source_url": row["source_url"],
            "retrieved_date": row["retrieved_date"],
            "access_status": "accessible_at_transcription",
            "content_sha256": "",
            "archive_status": "not_archived_release_candidate",
            "rights_status": "link_only_pending_source_specific_review",
        }
    PROVENANCE.mkdir(parents=True, exist_ok=True)
    source_fields = [
        "source_id", "source_institution", "reference_period", "source_url",
        "retrieved_date", "access_status", "content_sha256", "archive_status", "rights_status",
    ]
    with SOURCE_MANIFEST.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=source_fields)
        writer.writeheader()
        writer.writerows(sorted(source_rows.values(), key=lambda row: (row["source_institution"], row["reference_period"])))

    print(f"wrote {PRIMARY.relative_to(ROOT)} ({len(primary_rows)} rows)")
    print(f"wrote {SUMMARY.relative_to(ROOT)}")
    print(f"wrote {SOURCE_MANIFEST.relative_to(ROOT)} ({len(source_rows)} sources)")


if __name__ == "__main__":
    main()

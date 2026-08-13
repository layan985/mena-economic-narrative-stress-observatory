#!/usr/bin/env python3
import csv
import sys
from collections import Counter
from pathlib import Path

from validate_release import ALLOWED_COMPOSITE, NUMERIC, REQUIRED

PERIODS = {f"2026-{month:02d}" for month in range(1, 7)}
BASE_GEOGRAPHIES = {"Tunisia", "Saudi Arabia", "Morocco", "Jordan", "Palestine overall"}
REGIONAL_GEOGRAPHIES = {"West Bank excluding J1", "Jerusalem J1", "Gaza Strip"}


def validate_v03(path: Path):
    errors = []
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        fields = set(rows[0]) if rows else set()

    missing = REQUIRED - fields
    if missing:
        errors.append(f"missing columns: {sorted(missing)}")
    if len(rows) != 48:
        errors.append(f"v0.3.0-rc1 must contain 48 rows; found {len(rows)}")

    ids = [row.get("record_id", "") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("record_id values must be unique")

    institutions = {row.get("source_institution", "") for row in rows}
    if len(institutions) != 5:
        errors.append(f"expected 5 official source institutions; found {len(institutions)}")

    periods = {row.get("reference_period", "") for row in rows}
    if periods != PERIODS:
        errors.append(f"reference periods must be January-June 2026; found {sorted(periods)}")

    pairs = Counter((row.get("geography"), row.get("reference_period")) for row in rows)
    expected_pairs = {(g, p) for g in BASE_GEOGRAPHIES | REGIONAL_GEOGRAPHIES for p in PERIODS}
    if set(pairs) != expected_pairs:
        missing_pairs = sorted(expected_pairs - set(pairs))
        extra_pairs = sorted(set(pairs) - expected_pairs)
        if missing_pairs:
            errors.append(f"missing geography-period pairs: {missing_pairs}")
        if extra_pairs:
            errors.append(f"unexpected geography-period pairs: {extra_pairs}")
    if any(count != 1 for count in pairs.values()):
        errors.append("every geography-period pair must appear exactly once")

    for i, row in enumerate(rows, start=2):
        if not row.get("source_institution"):
            errors.append(f"row {i}: missing source institution")
        if not row.get("source_url", "").startswith("https://"):
            errors.append(f"row {i}: source_url must use https")
        if row.get("retrieved_date") != "2026-08-13":
            errors.append(f"row {i}: unexpected retrieved_date {row.get('retrieved_date')!r}")
        if row.get("composite_status") not in ALLOWED_COMPOSITE:
            errors.append(f"row {i}: invalid composite_status {row.get('composite_status')!r}")
        if not row.get("headline_cpi_annual_pct", "").strip():
            errors.append(f"row {i}: headline annual CPI is required")
        if not row.get("cpi_month_on_month_pct", "").strip():
            errors.append(f"row {i}: month-on-month CPI is required")
        expected_type = "regional_monthly_annual_rate" if row.get("geography") in REGIONAL_GEOGRAPHIES else "monthly_annual_rate"
        if row.get("measure_type") != expected_type:
            errors.append(f"row {i}: expected measure_type {expected_type!r}")
        if row.get("geography") in {"Palestine overall", "Gaza Strip"} and row.get("composite_status") != "withheld_structural_break":
            errors.append(f"row {i}: conflict-affected aggregate/Gaza row must carry structural-break withholding")
        if row.get("geography") in {"West Bank excluding J1", "Jerusalem J1"} and row.get("composite_status") != "withheld_regional_series":
            errors.append(f"row {i}: separately published regional row must remain a regional series")
        for field in NUMERIC:
            value = row.get(field, "").strip()
            if value:
                try:
                    float(value)
                except ValueError:
                    errors.append(f"row {i}: {field} is not numeric")

    primary = [row for row in rows if row.get("measure_type") == "monthly_annual_rate"]
    regional = [row for row in rows if row.get("measure_type") == "regional_monthly_annual_rate"]
    if len(primary) != 30 or len(regional) != 18:
        errors.append(f"expected 30 primary and 18 regional rows; found {len(primary)} and {len(regional)}")

    return errors


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "data/raw/mena-observatory-v0.3.0-rc1.csv")
    failures = validate_v03(target)
    if failures:
        print("\n".join(f"ERROR: {failure}" for failure in failures))
        raise SystemExit(1)
    print(f"OK: {target} passed v0.3.0-rc1 validation (48 rows; 30 primary + 18 regional)")

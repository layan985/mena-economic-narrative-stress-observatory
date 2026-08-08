#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

REQUIRED = {
    'record_id','geography','reference_period','measure_type','headline_cpi_annual_pct',
    'cpi_month_on_month_pct','food_cpi_annual_pct','housing_cpi_annual_pct',
    'core_cpi_annual_pct','prior_period_headline_pct','usd_exchange_rate_local_per_usd',
    'market_layer','narrative_layer','composite_status','source_institution','source_url',
    'retrieved_date','comparability_note'
}
NUMERIC = {
    'headline_cpi_annual_pct','cpi_month_on_month_pct','food_cpi_annual_pct',
    'housing_cpi_annual_pct','core_cpi_annual_pct','prior_period_headline_pct',
    'usd_exchange_rate_local_per_usd'
}
ALLOWED_COMPOSITE = {'withheld','withheld_structural_break','withheld_regional_series'}


def validate(path: Path):
    errors = []
    with path.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
        fields = set(rows[0].keys()) if rows else set()
    missing = REQUIRED - fields
    if missing:
        errors.append(f'missing columns: {sorted(missing)}')
    ids = [r.get('record_id','') for r in rows]
    if len(ids) != len(set(ids)):
        errors.append('record_id values must be unique')
    if len(rows) != 8:
        errors.append(f'v0.2 must contain 8 rows; found {len(rows)}')
    numeric_count = 0
    for i, row in enumerate(rows, start=2):
        if not row.get('source_institution'):
            errors.append(f'row {i}: missing source institution')
        if not row.get('source_url','').startswith('http'):
            errors.append(f'row {i}: source_url must be http(s)')
        if row.get('composite_status') not in ALLOWED_COMPOSITE:
            errors.append(f"row {i}: invalid composite_status {row.get('composite_status')!r}")
        for field in NUMERIC:
            value = row.get(field,'').strip()
            if value:
                numeric_count += 1
                try:
                    float(value)
                except ValueError:
                    errors.append(f'row {i}: {field} is not numeric')
    if numeric_count != 24:
        errors.append(f'v0.2 must contain 24 populated numeric observations; found {numeric_count}')
    return errors


if __name__ == '__main__':
    target = Path(sys.argv[1] if len(sys.argv) > 1 else 'data/raw/mena-observatory-pilot-2026-08-07.csv')
    failures = validate(target)
    if failures:
        print('\n'.join(f'ERROR: {x}' for x in failures))
        raise SystemExit(1)
    print(f'OK: {target} passed release validation')

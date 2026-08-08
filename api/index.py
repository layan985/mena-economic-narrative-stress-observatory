"""Read-only JSON API for the MENA Economic Narrative and Market Stress Observatory.

The endpoint is intentionally dependency-free so the archived release remains easy to
run and deploy. On Vercel, this file is exposed at ``/api``.
"""

from __future__ import annotations

import csv
import json
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

RELEASE = "v0.2"
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "raw" / "mena-observatory-pilot-2026-08-07.csv"

NUMERIC_FIELDS = {
    "headline_cpi_annual_pct",
    "cpi_month_on_month_pct",
    "food_cpi_annual_pct",
    "housing_cpi_annual_pct",
    "core_cpi_annual_pct",
    "prior_period_headline_pct",
    "usd_exchange_rate_local_per_usd",
}


def _coerce(row: dict[str, str]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in row.items():
        if value == "":
            out[key] = None
        elif key in NUMERIC_FIELDS:
            out[key] = float(value)
        else:
            out[key] = value
    return out


def _records() -> list[dict[str, object]]:
    with DATA_FILE.open("r", encoding="utf-8", newline="") as handle:
        return [_coerce(row) for row in csv.DictReader(handle)]


def _filter(records: list[dict[str, object]], query: dict[str, list[str]]) -> list[dict[str, object]]:
    allowed = {"record_id", "geography", "reference_period", "measure_type", "source_institution", "composite_status"}
    selected = records
    for field in allowed:
        values = query.get(field)
        if not values:
            continue
        wanted = values[-1].casefold()
        selected = [row for row in selected if str(row.get(field, "")).casefold() == wanted]
    return selected


class handler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: object) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "public, max-age=300, s-maxage=3600")
        self.send_header("X-Observatory-Release", RELEASE)
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        if query.get("health", [""])[-1].lower() in {"1", "true", "yes"}:
            self._send_json(200, {"status": "ok", "release": RELEASE})
            return

        try:
            records = _records()
        except (OSError, csv.Error) as exc:
            self._send_json(500, {"error": "release_data_unavailable", "detail": str(exc)})
            return

        filtered = _filter(records, query)
        payload = {
            "api_version": "1",
            "dataset_release": RELEASE,
            "status": "pilot",
            "count": len(filtered),
            "filters": {key: values[-1] for key, values in query.items() if key != "health"},
            "data": filtered,
            "methodological_warning": (
                "Rows are not automatically comparable across measure types. "
                "Structural-break and comparability fields must be retained in analysis."
            ),
            "license_note": "See repository LICENSE and source-specific provenance before redistribution.",
        }
        self._send_json(200, payload)

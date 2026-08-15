#!/usr/bin/env python3
"""Check whether the v0.3 release candidate has evidence required for stable promotion.

Exit 0 means the stable gate is closed completely. Exit 1 means one or more
published requirements remain open. This checker never treats a template,
invitation, or founder-only rerun as external validation.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/provenance/source-manifest-v0.3.0-rc1.csv"
AUDIT = ROOT / "audits/v0.3-source-audit.csv"
REVIEW_RECORD = ROOT / "audits/V0_3_EXTERNAL_REVIEW_RECORD.md"
REPRO_RECORD = ROOT / "audits/V0_3_INDEPENDENT_REPRODUCTION_RECORD.md"

REQUIRED_INSTITUTIONS = {
    "Department of Statistics (Jordan)",
    "General Authority for Statistics (Saudi Arabia)",
    "Haut-Commissariat au Plan (Morocco)",
    "National Institute of Statistics (Tunisia)",
    "Palestinian Central Bureau of Statistics",
}
SUCCESS_REPRO = {"success_exact", "success_with_documented_difference"}
SUCCESS_REVIEW = {"release", "release_after_corrections"}


def read_rows(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def field(text: str, label: str) -> str:
    m = re.search(rf"^- {re.escape(label)}:\s*`?([^`\n]+?)`?\s*$", text, re.M | re.I)
    return m.group(1).strip() if m else ""


def main() -> int:
    failures: list[str] = []

    manifest = read_rows(MANIFEST)
    if len(manifest) != 30:
        failures.append(f"source manifest has {len(manifest)} rows; expected 30")

    for row in manifest:
        sid = row.get("source_id", "<unknown>")
        archive = row.get("archive_status", "").strip()
        rights = row.get("rights_status", "").strip()
        digest = row.get("content_sha256", "").strip()
        if not archive or "pending" in archive or "release_candidate" in archive:
            failures.append(f"{sid}: archive treatment not final")
        if not rights or "pending" in rights:
            failures.append(f"{sid}: rights treatment not final")
        if archive.startswith("archived") and not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            failures.append(f"{sid}: archived source lacks a valid SHA-256")

    audit_rows = [r for r in read_rows(AUDIT) if any((v or "").strip() for v in r.values())]
    checked_institutions = {
        r.get("source_institution", "").strip()
        for r in audit_rows
        if r.get("status", "").strip().lower() in {"complete", "completed", "closed"}
    }
    missing_institutions = REQUIRED_INSTITUTIONS - checked_institutions
    if missing_institutions:
        failures.append("external audit does not yet cover: " + ", ".join(sorted(missing_institutions)))
    if len(audit_rows) < 5:
        failures.append("external audit has fewer than five completed source checks")
    for row in audit_rows:
        if row.get("severity", "").strip().lower() in {"material", "blocking"}:
            response = row.get("lab_response", "").strip()
            status = row.get("status", "").strip().lower()
            if not response or status not in {"closed", "complete", "completed"}:
                failures.append(f"{row.get('source_id','<unknown>')}: material/blocking discrepancy remains open")

    review_text = REVIEW_RECORD.read_text(encoding="utf-8")
    if "Status: **not completed**" in review_text:
        failures.append("external review record is not completed")
    review_recommendation = field(review_text, "Recommendation")
    if review_recommendation and review_recommendation.lower() not in SUCCESS_REVIEW:
        failures.append(f"external review recommendation is not release-permitting: {review_recommendation}")

    repro_text = REPRO_RECORD.read_text(encoding="utf-8")
    if "Status: **not completed**" in repro_text:
        failures.append("independent reproduction record is not completed")
    repro_result = field(repro_text, "Result")
    if repro_result and repro_result.lower() not in SUCCESS_REPRO:
        failures.append(f"independent reproduction result is not successful: {repro_result}")

    if failures:
        print("V0.3 STABLE GATE: OPEN")
        for item in failures:
            print(f"- {item}")
        return 1

    print("V0.3 STABLE GATE: CLOSED")
    print("All machine-checkable review, reproduction, provenance, archive and rights requirements passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

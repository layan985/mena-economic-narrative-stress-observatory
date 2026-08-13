# Methodology

## What v0.3.0-rc1 contains

The release candidate records official monthly CPI releases for January–June 2026 from five statistical institutions. One row represents a published geography and month. The focused primary panel has 30 institution-month rows: Tunisia, Saudi Arabia, Morocco, Jordan, and Palestine overall. Eighteen Palestinian regional rows are a separate supplement, not extra countries.

Primary statistical offices and their direct release pages or PDFs are used when available. Blank numeric fields remain null; they are not replaced with zero.

Every row requires a headline annual rate and month-on-month rate. Food, housing, core, prior-period, and exchange-rate fields remain optional because the official releases do not expose the same secondary measures.

## Comparability

Rows are not treated as interchangeable merely because they contain percentages.

- Monthly annual rates are aligned to the same six reference months, but remain source-defined national measures.
- Jordan uses its published monthly year-on-year rates in v0.3; the first-half period average remains only in the frozen v0.2 pilot.
- Palestine's regional series remain separate from the overall series.
- A change in source method or geography must be recorded with the row.
- Saudi rows carry the documented break that the updated CPI method applies from August 2025.

## Conflict-related breaks

Gaza's annual price decline follows exceptional wartime price levels and base effects. It is marked as a structural break and is not interpreted as lower stress or improved welfare.

## Why there is no composite

The release candidate has matching reference months but does not have a validated construct joining conflict-affected geography, national CPI definitions, a market layer, and narrative evidence. A composite would conceal those gaps. `composite_status` therefore remains withheld.

If a later version introduces an index, it must publish the construct being measured, eligibility rules, missing-data treatment, transformations, and sensitivity to excluding incomparable rows before reporting a headline ranking.

## Corrections

A released file is a snapshot. Corrections produce a new version and changelog entry rather than silently replacing the old file.

## Release-candidate provenance

`data/provenance/source-manifest-v0.3.0-rc1.csv` records one row for each of the 30 unique official releases. URLs and retrieval dates are complete. Source-byte archives and SHA-256 hashes are explicitly pending; the release candidate therefore does not yet pass the stable provenance gate.

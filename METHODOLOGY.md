# Methodology

## What v0.2 contains

The pilot records official price releases. One row represents a published geography and reference period. Subnational Palestinian geographies remain separate when the source publishes them separately.

Primary statistical offices and their direct release pages or PDFs are used when available. Blank numeric fields remain null; they are not replaced with zero.

## Comparability

Rows are not treated as interchangeable merely because they contain percentages.

- Monthly annual rates are compared only when the underlying concept and reference period align.
- Jordan's H1 period-average figure is preserved but excluded from a naive monthly ranking.
- Palestine's regional series remain separate from the overall series.
- A change in source method or geography must be recorded with the row.

## Conflict-related breaks

Gaza's annual price decline follows exceptional wartime price levels and base effects. It is marked as a structural break and is not interpreted as lower stress or improved welfare.

## Why there is no composite

The pilot does not yet have consistent country coverage, matching periods, a defensible rule for conflict breaks, or an independent source review. A composite would conceal those gaps. `composite_status` therefore remains withheld.

If a later version introduces an index, it must publish the construct being measured, eligibility rules, missing-data treatment, transformations, and sensitivity to excluding incomparable rows before reporting a headline ranking.

## Corrections

A released file is a snapshot. Corrections produce a new version and changelog entry rather than silently replacing the old file.

# Methodology

## Scope

Release v0.2 is an official-data pilot for the MENA Economic Narrative and Market Stress Observatory. It tests whether heterogeneous official price releases can be captured with enough provenance and comparability metadata to support later multi-layer research.

It is **not** a completed regional stress index.

## Unit of observation

The public wide file uses one row per published geography and reference period. Subnational Palestinian geographies are retained separately when the source publishes them separately.

## Source hierarchy

1. Primary national statistical offices or equivalent official institutions.
2. Direct official release pages or official PDFs.
3. No secondary aggregator substitutes for a primary source when the primary release is available.

## Missingness

Blank numeric fields are null values. They mean that the measure was not observed, was not available in the source, or is outside the scope of the release. Nulls must never be recoded as zero merely to make a composite computable.

## Comparability

Rows are not treated as exchangeable merely because they contain percentages.

- Monthly annual rates may be compared only when the underlying concepts are materially aligned.
- Jordan's H1 period-average figure is preserved but excluded from naive monthly ranking.
- Regional Palestinian series remain distinct from the overall Palestine series.
- Methodological changes must be documented at the row or source level.

## Conflict-related structural breaks

Conflict can make directionally intuitive interpretation invalid. Gaza's large annual price decline follows exceptional wartime price levels and base effects. It must not be interpreted mechanically as lower economic stress or improved welfare.

Rows affected by such breaks are explicitly flagged and composite publication is withheld.

## Four-layer target architecture

The Observatory ultimately targets four evidence layers:

1. **Macro:** official price, labor, output, and related macro releases.
2. **Markets:** exchange rates, yields, equities, commodities, volatility, or other documented market-pressure variables where licensing permits.
3. **Policy:** timestamped fiscal, monetary, regulatory, subsidy, tax, capital-control, and related policy events.
4. **Narrative:** auditable Arabic-English economic narrative evidence under a published annotation protocol.

## Composite publication gate

A composite score may be published only after all of the following are satisfied:

- country/source eligibility rules are frozen for the release;
- required layers meet documented minimum coverage;
- provenance is complete enough for independent checking;
- licensing and redistribution are documented;
- transformations are reproducible from versioned code;
- structural-break and conflict rules have been applied;
- an analyst other than the producing analyst reruns the package or independently verifies the relevant module;
- failed, missing, or unaudited components are not silently replaced with zeros.

Until these conditions are met, `composite_status` remains withheld.

## Versioning

Published releases are immutable snapshots. Corrections produce a new patch or minor version with a changelog entry rather than silent replacement.

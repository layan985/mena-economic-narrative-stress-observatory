# Observatory Public API

The Observatory exposes its pilot release through a read-only JSON endpoint implemented in [`api/index.py`](api/index.py).

## Endpoint

When deployed on Vercel, the default endpoint is:

```text
GET /api
```

The API is intentionally dependency-free and reads the immutable v0.2 release CSV directly.

## Query parameters

Exact-match filters are supported for:

- `record_id`
- `geography`
- `reference_period`
- `measure_type`
- `source_institution`
- `composite_status`

Example:

```text
GET /api?geography=Tunisia
```

Health check:

```text
GET /api?health=true
```

## Response contract

Every successful data response contains:

- `api_version`
- `dataset_release`
- `status`
- `count`
- `filters`
- `data`
- `methodological_warning`
- `license_note`

Empty CSV fields are serialized as JSON `null`; numeric fields are serialized as numbers.

## Methodological warning

API availability does **not** make all rows directly comparable. Clients must preserve `measure_type`, `comparability_note`, and `composite_status`. In particular, wartime structural breaks and period-average observations must not be interpreted as ordinary monthly cross-country comparisons.

## External-use evidence

The API only satisfies the project's external-use milestone after a third party has made a documented substantive use of it. Acceptable evidence includes:

1. a public repository, notebook, or application calling the endpoint;
2. an institutional analysis explicitly citing the API/release;
3. an issue or pull request from an external user demonstrating use;
4. reproducible server logs plus a named external collaborator confirming their use.

Self-generated requests do not count as external adoption.

# Design: Spoon CLI v0.3

- Entry point: `spoon-diversity`
- Modules: `spoon_diversity.cli`, `spoon_diversity.validators`
- Validate flow: read files → heuristic checks → non-zero exit on failure
- Sync flow: read CSV header → write dictionary markdown (idempotent)



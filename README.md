# Spoon Diversity Study

[![CI](https://github.com/nkllon/spoon-diversity-study/actions/workflows/ci.yml/badge.svg)](https://github.com/nkllon/spoon-diversity-study/actions/workflows/ci.yml)
[![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=nkllon_spoon-diversity-study&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=nkllon_spoon-diversity-study)

Minimal Tool‑Set Diversity: a spoon‑size case study of tool‑set morphological complementarity. This repo contains the ontology, dataset template, diagrams, methods, SDD steering/specs, and a small CLI for validation/sync.

## Contents
- Ontology: `spore_SpoonDiversityOntology_v0.3.ttl`, SHACL: `spoon_shapes_v0.3.ttl`
- Dataset: `spoon_diversity_dataset_template_v0.3.csv`, `spoon_diversity_data_dictionary_v0.3.md`, samples in `examples/`
- Diagrams: `spoon_experiment_workflow_v0.3.puml`, `spoon_analysis_pipeline_v0.3.mmd`, `ontology_hierarchy_v0.3.dot`
- Paper: `spoon_diversity_study_paper_v0.3.md`
- Registries: `spoon_spore_registry_v0.3.ttl`, `guidance_spoon_v0.3.ttl`
- SDD: `.kiro/steering/*`, `.kiro/specs/*`, `AGENTS.md`, `docs/SDD_Tooling.md`, `docs/TRACEABILITY.md`
- CLI (PyPI package name: spoon-diversity-tools): `src/spoon_diversity/*`

## Quick start

```bash
git clone https://github.com/nkllon/spoon-diversity-study.git
cd spoon-diversity-study
python -m pip install --upgrade pip
python -m pip install ".[dev]" pre-commit
pre-commit install

# Local gates
pre-commit run --all-files
pytest --cov=src --cov-report=term

# Validate artifacts and sync dictionary
make spec-validate
make spec-sync
```

## SDD commands (Cursor)
See `AGENTS.md`. Typical flow in Cursor chat:
- `/kiro:steering`
- `/kiro:spec-init "<desc>"` → `/kiro:spec-requirements` → `/kiro:spec-design -y` → `/kiro:spec-tasks -y` → `/kiro:spec-impl`

## CI/CD
- CI (PR/main): ruff, black (check), mypy, pytest (3.10/3.11/3.12), coverage.xml
- Sonar: runs only after tests pass (separate job with `needs: [test]`), fetch-depth: 0
- Secrets: set via stdin only
  ```bash
  printf '%s' '<TOKEN>' | gh secret set SONAR_TOKEN --repo nkllon/spoon-diversity-study --body -
  ```
  Prefer org-level `SONAR_TOKEN` for consistency.

## Releases
- Tag `vX.Y.Z-rcN` → TestPyPI publish via trusted publisher → smoke install
- Tag `vX.Y.Z` → PyPI publish via trusted publisher → smoke install
- Version check: tag must match `pyproject.toml`

## Contributing
See `CONTRIBUTING.md`. Run local gates before PR:
```bash
pre-commit run --all-files && pytest --cov=src
```

## License
MIT (`LICENSE_MIT.txt`)



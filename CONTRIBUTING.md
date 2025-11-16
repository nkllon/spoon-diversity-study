# Contributing

## Local setup

```bash
python -m pip install --upgrade pip
python -m pip install ".[dev]" pre-commit
pre-commit install
```

## Local gates (must pass before PR)

```bash
pre-commit run --all-files
pytest --cov=src --cov-report=term
```

## CI gates
- CI runs ruff/black/mypy and unit tests across Python 3.10/3.11/3.12.
- Sonar runs only after tests pass (separate job with needs: test).
- Releases are automated via python-semantic-release on pushes to main after tests pass.

## Secrets
- Set secrets via stdin only; example:

```bash
printf '%s' '<TOKEN>' | gh secret set SONAR_TOKEN --repo nkllon/spoon-diversity-study --body -
```

Prefer org-level secrets; repo-level only for overrides.

## Conventional Commits (required)
Use Conventional Commits to drive semantic versioning:
- `feat: add new observation validator` → minor bump
- `fix: correct TTL prefix guard` → patch bump
- `perf: speed up CSV header parse` → patch bump
- `refactor: extract CLI parser` → no bump unless flagged
- `feat!: change CLI flags` or footer `BREAKING CHANGE: ...` → major bump




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

## Secrets
- Set secrets via stdin only; example:

```bash
printf '%s' '<TOKEN>' | gh secret set SONAR_TOKEN --repo nkllon/spoon-diversity-study --body -
```

Prefer org-level secrets; repo-level only for overrides.



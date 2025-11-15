# Requirements: CI/CD v0.3

## 1. PR CI
WHEN a PR is opened THE CI SHALL run lint, type-check, tests, and produce coverage.xml.

## 2. SonarCloud
THE SonarCloud analysis SHALL run on PR and main with fetch-depth=0 and fail the job if quality gate fails.

## 3. Versioned Releases
WHEN a tag `vX.Y.Z-…` is pushed THE workflow SHALL publish to TestPyPI; WHEN `vX.Y.Z` is pushed THE workflow SHALL publish to PyPI.

## 4. Version Consistency
THE release SHALL fail if tag version ≠ `pyproject.toml` version.



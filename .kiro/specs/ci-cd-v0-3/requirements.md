# Requirements: CI/CD v0.3

## 1. PR CI
WHEN a PR is opened THE CI SHALL run lint, type-check, tests, and produce coverage.xml.

## 2. SonarCloud
THE SonarCloud analysis SHALL run on PR and main with fetch-depth=0 and fail the job if quality gate fails.

## 3. Versioned Releases
WHEN a tag `vX.Y.Z-…` is pushed THE workflow SHALL publish to TestPyPI; WHEN `vX.Y.Z` is pushed THE workflow SHALL publish to PyPI.

## 4. Version Consistency
THE release SHALL fail if tag version ≠ `pyproject.toml` version.

## 5. Local‑first failure detection (reduce Sonar usage for basic issues)
THE CI pipeline SHALL gate Sonar execution behind successful local checks:
- Lint (ruff and black --check) SHALL pass
- Type‑check (mypy) SHALL pass
- Unit tests with coverage SHALL pass and generate coverage.xml
IF any of the above fail THEN the workflow SHALL stop before running Sonar.

## 6. Packaging/build validation (discovered failure modes)
- THE build system SHALL pin `hatchling>=1.24`.
- THE wheel target packages mapping SHALL be declared (e.g., `packages=["src/spoon_diversity"]`).
- THE CI and Sonar installs SHALL use non‑editable `pip install ".[dev]"` (no editable installs).
- THE install step SHALL succeed in a clean runner; if it fails THEN the job SHALL emit a clear remediation hint (pin hatchling, declare wheel packages, avoid editable).

## 7. Lint/type strictness (discovered failure modes)
- THE lint configuration SHALL treat unused imports as errors (e.g., ruff default rules).
- THE codebase SHALL be lint‑clean before merge; CI SHALL fail on any lint error (e.g., unused imports).
- THE type‑check step SHALL run `mypy src/` and fail on errors.

## 8. Secrets and guards (discovered failure modes)
- BEFORE Sonar scan THE workflow SHALL verify `SONAR_TOKEN` is present and fail fast with an explicit message if missing.
- THE Sonar job SHALL check out with `fetch-depth: 0`.

## 9. Tooling discovery and installation (local + CI)
- THE dev dependency set SHALL include at minimum: `ruff>=0.5.0`, `black>=24.0`, `mypy>=1.8.0`, `pytest>=7.0`, `pytest-cov>=4.0`, `build>=1.2.1`, `hatchling>=1.24`.
- THE local setup instructions SHALL specify a single command to install dev tools: `python -m pip install ".[dev]"`.
- THE CI SHALL install using the same command to ensure parity with local verification.



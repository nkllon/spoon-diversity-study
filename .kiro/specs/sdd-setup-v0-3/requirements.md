# Requirements: SDD Setup v0.3

## 1. Provisioning
THE system SHALL install cc-sdd (Cursor) and expose Kiro commands.

## 2. Helper
THE system SHALL provide a local helper and Make targets for validate/sync.

## 3. Docs
THE system SHALL document installation and usage in `docs/SDD_Tooling.md` and `AGENTS.md`.

## 4. Non-interactive & CI-Safe
THE SDD install flow SHALL be non-interactive and idempotent; Make targets SHALL run in CI without manual input.

## 5. Tooling discovery and installation (local developer workflow)
- THE repository SHALL document local setup with a single command to install dev tools: `python -m pip install ".[dev]"`.
- THE required tools SHALL include ruff, black, mypy, pytest, pytest-cov, build, and hatchling (pinned to versions compatible with CI).
- THE helper and docs SHALL instruct running local gates (`ruff`, `black --check`, `mypy`, `pytest --cov`) before pushing; SonarCloud SHALL be reserved for code quality beyond basic lint/type/test failures.



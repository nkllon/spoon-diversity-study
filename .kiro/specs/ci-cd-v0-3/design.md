# Design: CI/CD v0.3

- CI: matrix (3.10/3.11/3.12), ruff/black/mypy, pytest with coverage
- Sonar: single Python 3.11, coverage.xml, fetch-depth=0
- Publish: tag-triggered, verify tag/version, build, OIDC publish with TestPyPI pre-release routing



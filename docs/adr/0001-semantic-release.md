# ADR-0001: Adopt python-semantic-release for versioning and releases

## Status
Accepted

## Context
Manual version bumps and brittle parsing in CI (e.g., sed/grep) are error‑prone. We want automatic semver bumps from Conventional Commits, consistent tags, and GitHub Releases without sacrificing our existing OIDC‑based publish flow (TestPyPI/PyPI).

## Decision
Use python‑semantic‑release (PSR) to:
- Parse Conventional Commits to determine the next version
- Update version in `pyproject.toml`
- Generate changelog and create Git tag
- Create GitHub Release

Keep our tag‑triggered publish workflow to handle TestPyPI/PyPI with OIDC and pre‑release routing.

## Consequences
- Requires Conventional Commits (feat, fix, perf, refactor, BREAKING CHANGE)
- CI adds a `release` job (needs: test) on main to run semantic‑release
- Pre‑release flow uses `semantic-release version --prerelease` to produce `vX.Y.Z-rcN` tags; current publish workflow routes pre‑releases to TestPyPI

## Alternatives considered
- bump‑my‑version/tbump: simple manual bumps; no changelog automation
- setuptools_scm: derive version from tags; requires tag‑first flow
- release‑please: GitHub release PRs; still need separate PyPI publish

## Rollout plan
1) Add PSR config in `pyproject.toml`, dev dependency `python-semantic-release`
2) Add `release` job in `ci.yml` with `needs: [test]`, gated to main push
3) Add manual prerelease workflow_dispatch to run `semantic-release --prerelease`
4) Keep existing publish workflow; PSR will create tags/releases that trigger it



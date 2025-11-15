# Tech Steering – Spoon Diversity Study

## Stack
- Python 3.10–3.12, hatchling packaging
- rdflib, pyshacl for RDF/SHACL
- pytest, ruff, black, mypy

## Automation
- GitHub Actions runs lint, typecheck, tests, and validation
- Makefile convenience targets: lint, fmt, typecheck, test, ci

## Operational discipline (agent)
- Verification-first: Prefer list/view/diff before proposing actions.
- Secrets: Never overwrite or reveal; check existence via read-only means (e.g., `gh secret list`).
- Non-destructive defaults: Propose branches and PRs over direct changes to `main`.

# Spoon Diversity Study – Tech Steering (v0.3)

Stack and tooling
- Data/Modeling: RDF/Turtle (TTL), Graphviz (DOT), PlantUML (PUML), Mermaid (MMD)
- SDD: cc-sdd Kiro commands (Cursor agent) provisioned under `.cursor/commands/kiro/`
- Local helper: `scripts/kiro` with `make spec-validate` and `make spec-sync`
- Environment: macOS, Node (npx for `cc-sdd`), shell `bash`

Conventions
- TTL prefixes: `sp`, `prov`, `sosa`, `ssn`, `schema`, `xsd`, `rdfs`, `owl`
- Units: seconds (s), centimeters (cm), percent (%), Likert 1–7
- Keep ontology properties aligned with CSV columns via `spec-sync`



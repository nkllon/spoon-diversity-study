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



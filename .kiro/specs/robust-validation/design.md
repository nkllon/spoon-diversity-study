# Robust Validation – Design

## Ontology & SHACL
- Load TTL with rdflib into Graph
- Validate against SHACL shapes via pyshacl (RDFS inference)

## CSV
- Parse with DictReader
- Check types/ranges; enforce TaskID/ToolSet against ontology catalogs

## Diagrams
- PUML: markers + transition presence
- Mermaid: header + at least one edge
- DOT: digraph presence + namespaced label

## CLI
- Add --version, --quiet, --json
- Summarize per-artifact results

## CI
- Run ruff, black, mypy, pytest; validate repo artifacts



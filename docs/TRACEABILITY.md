# Traceability – Requirements ↔ Ontology ↔ Dataset ↔ Diagrams

## Mapping

| Requirement | Ontology (sp:*) | Dataset Column | Diagram |
|---|---|---|---|
| Measure hand size | `sp:handSizeCm` (Participant) | `HandSize_cm` | PUML: measurement step |
| Trial timing | `sp:timeSeconds` (Observation) | `Time_s` | PUML: run trial; MMD: compute metrics |
| Operation count | `sp:numOperations` | `NumOperations` | MMD: derived metrics |
| Error rate | `sp:errorRatePercent` | `ErrorRate_pct` | MMD: stats/visuals |
| Switch count/time | `sp:switchCount`, `sp:switchTimeSeconds` | `SwitchCount`, `SwitchTime_s` | PUML: record switches |
| Likert costs | `sp:perceivedCognitiveCost`, `sp:perceivedDiscomfort` | `PerceivedCognitiveCost`, `PerceivedDiscomfort` | PUML: post‑survey |
| ToolSet | `sp:usesToolSet` → `sp:ToolSet` | `ToolSet` | DOT: Trial→ToolSet |
| Task | `sp:informedByTask` → `sp:Task` | `TaskID` | DOT: Trial→Task |

## Controlled Lists
- ToolSet: `Spoon-A`, `Spoon-B`
- TaskID: `SCOOP`, `TRANSFER`

## Validation
- Run `make spec-validate` (syntax/structure checks; SHACL presence)
- Run `make spec-sync` (dictionary regeneration)



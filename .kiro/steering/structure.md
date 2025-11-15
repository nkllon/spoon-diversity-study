# Spoon Diversity Study – Structure Steering (v0.3)

Repository layout (key files)
- Ontology: `spore_SpoonDiversityOntology_v0.3.ttl`
- Data template: `spoon_diversity_dataset_template_v0.3.csv`
- Diagrams: `spoon_experiment_workflow_v0.3.puml`, `spoon_analysis_pipeline_v0.3.mmd`, `ontology_hierarchy_v0.3.dot`
- Paper: `spoon_diversity_study_paper_v0.3.md`
- SDD docs: `docs/SDD_Tooling.md`
- SDD steering: `.kiro/steering/*.md`
- Make targets: `Makefile`; helper: `scripts/kiro`

Guidelines
- Keep identifiers stable across ontology, CSV, and paper
- Prefer small, composable diagrams; re‑use labels from ontology
- Validate early/often with `make spec-validate`



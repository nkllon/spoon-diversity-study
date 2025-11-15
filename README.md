# Spoon Diversity Study – v0.4

## Quickstart

Install (dev):

```bash
python -m pip install -e ".[dev]"
```

Validate artifacts (v0.4):

```bash
spoon-diversity validate \
  --ttl spore_SpoonDiversityOntology_v0.4.ttl \
  --csv spoon_diversity_dataset_template_v0.4.csv \
  --puml spoon_experiment_workflow_v0.4.puml \
  --mmd spoon_analysis_pipeline_v0.4.mmd \
  --dot ontology_hierarchy_v0.4.dot \
  --shapes spoon_shapes_v0.4.ttl
```

Generate/refresh data dictionary:

```bash
spoon-diversity sync \
  --ontology spore_SpoonDiversityOntology_v0.4.ttl \
  --csv spoon_diversity_dataset_template_v0.4.csv \
  --dict spoon_diversity_data_dictionary_v0.4.md
```

CI runs lint, typecheck, tests, and validation on push/PR.



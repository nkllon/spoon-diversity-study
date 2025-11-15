SHELL := /bin/bash

# Install cc-sdd (Spec-Driven Development) and expose Kiro command set for Cursor
sdd-install:
	@echo "Installing cc-sdd (Cursor agent) and provisioning Kiro SDD command set..."
	npx --yes cc-sdd@latest --cursor --lang en
	@echo "Done. Launch Cursor and use /kiro:... slash commands."

# Validate/spec check across ontology, dataset, and diagrams
spec-validate:
	bash ./scripts/kiro spec:validate --ttl spore_SpoonDiversityOntology_v0.3.ttl \
	  --csv spoon_diversity_dataset_template_v0.3.csv \
	  --puml spoon_experiment_workflow_v0.3.puml \
	  --mmd spoon_analysis_pipeline_v0.3.mmd \
	  --dot ontology_hierarchy_v0.3.dot \
	  --shapes spoon_shapes_v0.3.ttl

# Derive/update artifacts from canonical specs (no-op placeholder, wired for future use)
spec-derive:
	bash ./scripts/kiro spec:derive --all

# Synchronize schema from ontology to CSV and docs (generates data dictionary if missing)
spec-sync:
	bash ./scripts/kiro spec:sync --ontology spore_SpoonDiversityOntology_v0.3.ttl \
	  --csv spoon_diversity_dataset_template_v0.3.csv \
	  --dict spoon_diversity_data_dictionary_v0.3.md



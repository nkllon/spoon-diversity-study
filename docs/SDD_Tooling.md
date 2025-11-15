# Spec-Driven Development (SDD) Tooling for Spoon Diversity Study v0.3

This repo uses cc-sdd to provision the Kiro Spec-Driven Development workflow and a local helper script for validation and syncing.

## Install cc-sdd (Cursor agent)

Run from the project root:

```bash
npx --yes cc-sdd@latest --cursor --lang en
```

## Operational Safety (Agents)
- Verification-first: Use read-only tools to gather facts before asking users
  - Git: `git fetch` + ahead/behind checks
  - CI: read workflow logs and statuses
  - Secrets: `gh secret list | grep NAME` to confirm presence
- Secrets handling:
  - Never echo or write secret values into code or logs.
  - Do not set/overwrite secrets unless explicitly instructed; provide UI/CLI steps instead.
  - Guard CI steps with secret checks (e.g., `if: ${{ secrets.SONAR_TOKEN != '' }}`).

What it does:
- Installs Kiro slash commands in `.cursor/commands/kiro/`
- Adds SDD settings in `.kiro/settings/`
- Creates `AGENTS.md` (project memory readme)

Verify:

```bash
ls -1 .cursor/commands/kiro | wc -l
```

## Using Kiro slash commands (in Cursor chat)

- `/kiro:steering` — establish project memory
- `/kiro:spec-init <desc>` — initialize a spec
- `/kiro:spec-requirements <feature>` — generate requirements
- `/kiro:spec-design <feature> [-y]` — generate design
- `/kiro:spec-tasks <feature> [-y]` — break into tasks
- `/kiro:spec-impl <feature> [tasks]` — implement
- `/kiro:validate-*` — validation gates

See: `docs/guides/command-reference.md` in the cc-sdd distribution for full details.

## Local helper wrapper (`./scripts/kiro`)

For repo-level checks and synchronization, use:

```bash
# Validate ontology, dataset, diagrams
./scripts/kiro spec:validate \
  --ttl spore_SpoonDiversityOntology_v0.3.ttl \
  --csv spoon_diversity_dataset_template_v0.3.csv \
  --puml spoon_experiment_workflow_v0.3.puml \
  --mmd spoon_analysis_pipeline_v0.3.mmd \
  --dot ontology_hierarchy_v0.3.dot

# Generate/update data dictionary from CSV header and ontology mappings
./scripts/kiro spec:sync \
  --ontology spore_SpoonDiversityOntology_v0.3.ttl \
  --csv spoon_diversity_dataset_template_v0.3.csv \
  --dict spoon_diversity_data_dictionary_v0.3.md
```

Make targets:

```bash
make spec-validate
make spec-sync
```

## Optional system symlink

If desired, create a system-wide `/kiro` that delegates to this repo helper (requires sudo):

```bash
sudo ln -sf "$(pwd)/scripts/kiro" /usr/local/bin/kiro
kiro help
```

## Troubleshooting

- If Cursor doesn’t show `/kiro:*` commands, ensure `.cursor/commands/kiro/` exists.
- If validation fails, open files mentioned and correct syntax (TTL prefixes, PlantUML `@startuml`/`@enduml`, Mermaid `flowchart`, DOT `digraph`).
- For cc-sdd reinstall or language changes:

```bash
npx --yes cc-sdd@latest --cursor --lang en
```



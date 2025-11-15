# Release & Quality Gates – Spoon Diversity Study (v0.3)

This study is documentation‑first and spec‑driven. The following gates must pass before versioning or distribution of artifacts (paper drafts, figures, datasets).

Pre‑release checklist
1. All changes committed to the canonical repo
2. All diagrams render locally (PUML/MMD/DOT)
3. `make spec-validate` passes
4. Data dictionary regenerated: `make spec-sync`
5. Methods and diagrams consistent (cross‑check measures/units)
6. Version bump recorded in `README_SpoonDiversityStudy_v0.3.md` if scope changed

Tagging procedure
1. Ensure clean working tree (no uncommitted changes)
2. Create annotated tag `v0.3.X` with summary of changes
3. Push tag to canonical remote

Packaging for sharing
- Include: ontology TTL, dataset template + dictionary, diagrams, paper, Makefile, `scripts/kiro`, `.kiro/steering/*`
- Exclude: transient or local caches

Post‑release verification
1. Pull fresh clone; run `make spec-validate`
2. Open paper Methods and confirm references line up with artifacts
3. Record any corrections as a new patch version

Notes
- Based on mailbox‑core’s corrected release guardrails; adapted for this research bundle (no PyPI publish).



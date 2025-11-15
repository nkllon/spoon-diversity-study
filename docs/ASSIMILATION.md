# External Asset Assimilation – Spoon Diversity Study (v0.3)

This document records external sources reviewed under `/Volumes/lemon/cursor` and what we adopted for this study bundle.

## Sources
- beast-mailbox-core: `steering/release-procedure-CORRECTED.md` – rigorous release guardrails
- composable-ai-advisors:
  - `caa-glossary.ttl` – ontology structure and SHACL patterns
  - `guidance.ttl`, `spore_registry.ttl` – registry modeling with PROV links
- fort: `ontology/unifi_servicenow.ttl` – domain-specific TTL (referenced for style; not adopted)
- cc-sdd: Kiro SDD provisioning and command set (already installed)

## Adopted Patterns
- Steering:
  - `.kiro/steering/release.md` – release gates tailored for this repo
  - `.kiro/steering/product.md`, `tech.md`, `structure.md` – baseline project memory
- Registries:
  - `spoon_spore_registry_v0.3.ttl` – Spore registry with links to key artifacts
  - `guidance_spoon_v0.3.ttl` – minimal Guidance registry stub
- Agents:
  - `AGENTS.md` – SDD command overview referencing `docs/SDD_Tooling.md`

## Rationale
- Align with PROV‑linked registries to track artifact lineage and milestones
- Enforce quality gates to prevent drift across ontology, dataset, diagrams, and paper
- Keep assimilation minimal and domain-neutral; avoid importing unrelated domain classes

## Maintenance
- Update registry timestamps when publishing new versions
- Keep steering in sync with repository changes
- Validate regularly with `make spec-validate`; regenerate dictionary via `make spec-sync`



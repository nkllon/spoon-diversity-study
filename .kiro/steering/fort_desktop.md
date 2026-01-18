# “fort-desktop” Corpus Alias (Local Repo Interrogation)

Definition
- “fort-desktop” is the canonical alias for the local desktop corpus rooted at `/Volumes/lemon/cursor/*`.
- Purpose: a stable meme to reference nkllon’s local Git repositories and adjacent project folders for discovery, interrogation, and pattern extraction (e.g., CI/CD, release, ontology conventions).

Backing Catalog
- The corpus is cataloged in `.kiro/steering/repo_registry.ttl`.
  - Enumerates discovered Git repos (local path → origin URL) and notable non-repo folders.
  - Serves as the machine-readable index for agents and scripts.

Scope and Guarantees
- Scope: all direct children under `/Volumes/lemon/cursor/*`.
- Guarantee: Only read-only interrogation is allowed by default (verification-first principle). Any mutations require explicit user direction.

Usage Guidance (Agents)
- Use the alias “fort-desktop” to refer to the corpus in plans and analyses; resolve to the real path `/Volumes/lemon/cursor/*`.
- Before proposing patterns (e.g., CI/CD), cite concrete evidence from repos listed in `repo_registry.ttl` (file paths/lines).
- If the registry is stale or missing a repo, first refresh the registry (read-only discovery) before analysis.

Update Policy
- When repos are added/removed/moved locally, update `.kiro/steering/repo_registry.ttl` to keep the catalog in sync.
- Changes to the alias root path must be reflected here and in the registry header.



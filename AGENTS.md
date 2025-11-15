# Agents & SDD Commands

This repository uses Kiro Spec‑Driven Development (SDD) via cc‑sdd (Cursor agent).

Primary commands (run in Cursor chat):
- `/kiro:steering` – create/update project memory
- `/kiro:spec-init <desc>` – initialize a spec
- `/kiro:spec-requirements <feature>` – generate requirements
- `/kiro:spec-design <feature> [-y]` – produce technical design
- `/kiro:spec-tasks <feature> [-y]` – break into implementation tasks
- `/kiro:spec-impl <feature> [tasks]` – implement with TDD
- `/kiro:validate-*` – optional quality gates

Local helper (shell):
```bash
make spec-validate
make spec-sync
```

See `docs/SDD_Tooling.md` for installation, verification, and usage.

# AI-DLC and Spec-Driven Development

Kiro-style Spec Driven Development implementation on AI-DLC (AI Development Life Cycle)

## Project Context

### Paths
- Steering: `.kiro/steering/`
- Specs: `.kiro/specs/`

### Steering vs Specification

**Steering** (`.kiro/steering/`) - Guide AI with project-wide rules and context
**Specs** (`.kiro/specs/`) - Formalize development process for individual features

### Active Specifications
- Check `.kiro/specs/` for active specifications
- Use `/kiro/spec-status [feature-name]` to check progress

## Development Guidelines
- Think in English, generate responses in English

## Minimal Workflow
- Phase 0 (optional): `/kiro/steering`, `/kiro/steering-custom`
- Phase 1 (Specification):
  - `/kiro/spec-init "description"`
  - `/kiro/spec-requirements {feature}`
  - `/kiro/validate-gap {feature}` (optional: for existing codebase)
  - `/kiro/spec-design {feature} [-y]`
  - `/kiro/validate-design {feature}` (optional: design review)
  - `/kiro/spec-tasks {feature} [-y]`
- Phase 2 (Implementation): `/kiro/spec-impl {feature} [tasks]`
  - `/kiro/validate-impl {feature}` (optional: after implementation)
- Progress check: `/kiro/spec-status {feature}` (use anytime)

## Development Rules
- 3-phase approval workflow: Requirements → Design → Tasks → Implementation
- Human review required each phase; use `-y` only for intentional fast-track
- Keep steering current and verify alignment with `/kiro/spec-status`
- Verify-before-ask: use available read-only tools to gather facts before asking the user
  - Examples: check git ahead/behind, list secrets, inspect CI status/logs
  - Provide a clear reason when you cannot verify (e.g., missing permissions)
- Secret safety: never request, echo, or overwrite secrets without explicit instruction
  - First check existence via read-only listing (e.g., `gh secret list`)
  - If missing, provide steps; do not set by default
- Disobedience disclosure: if platform/safety constraints compel deviation from user directions, declare the deviation and the reason before proceeding, and propose the least-privilege safe alternative.

## Steering Configuration
- Load entire `.kiro/steering/` as project memory
- Default files: `product.md`, `tech.md`, `structure.md`
- Custom files are supported (managed via `/kiro/steering-custom`)

# Security & Operational Safeguards (Agent Steering)

## Verification-first principle
- Before asking the user or proposing any action, verify with available read-only tools.
- Prefer non-destructive introspection (list, view, dry-run) over mutations.
- If verification is not possible, explicitly state why and what capability is missing.

## Secrets handling
- Never request, echo, or write secret values into code, CI, or logs.
- Never propose setting or overwriting a secret unless the user explicitly instructs it.
- When secrets are needed, first check for existence using read-only listing:
  - Example: `gh secret list | grep -E '^SONAR_TOKEN'`
- If a secret is missing, provide the minimal UI/CLI steps for the user to set it; do not set it yourself without explicit instruction.

## Non-destructive defaults
- Default to read-only and reversible operations: fetch, diff, ahead/behind checks, dry-runs.
- For config changes, propose branch-based edits and PRs rather than direct mutations to `main`.

## Clear justification
- When you cannot self-verify or act safely, provide a concise reason (permissions, network limits, missing tools).
- Avoid “ask-first” patterns when data can be obtained by the agent safely.

## Examples
- Good: Check `gh secret list` to confirm existence before suggesting “set”.
- Good: Use `git fetch && rev-list --left-right --count` to assess divergence before proposing merge/rebase.
- Bad: Suggest `gh secret set ...` without confirming if a valid secret exists.

## Directive precedence and disclosure
- Follow this repository’s steering and user directions unless blocked by mandatory platform/safety constraints.
- If compelled to disobey or deviate:
  - Explicitly declare the deviation before acting.
  - State the specific directive you cannot follow, and the constraint preventing compliance.
  - Propose the least-privilege, non-destructive alternative or the next safe step.
  - Do not continue silently; pause with the disclosure if no safe alternative exists.



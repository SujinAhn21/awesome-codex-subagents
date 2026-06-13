# Conversion Policy

## Primary Decision

This repository prefers transformed Codex-native artifacts over raw upstream Claude agent files.

## Why

- Upstream files target Claude installation surfaces and conventions.
- Codex's documented customization surfaces are `AGENTS.md`, skills, plugins, MCP, and subagents.
- Repackaging into Codex-native assets reduces ambiguity for Codex users.

## Default Output Target

1. Convert upstream role definitions into `skills/`.
2. Add `plugins/` only for stable bundles.
3. Use `examples/AGENTS.md` only for supporting guidance, not as the main converted asset.

## Conversion Rules

- Preserve upstream agent name unless a rename is necessary for Codex compatibility.
- Preserve the role's core specialization and workflow intent.
- Remove Claude-specific installation instructions from the final Codex skill.
- Replace Claude-specific file placement assumptions with Codex usage guidance.
- Add explicit trigger conditions.
- Add Codex-relevant validation steps.
- Preserve the shared reliability protocol: no completion claims without actual verification.
- Preserve the shared Korean-output style when the user writes in Korean.
- Mark MCP dependency explicitly.
- Keep references concise; do not blindly embed large upstream text if a structured Codex skill is
  clearer.

## Raw Copy vs Adaptation

### Allowed raw copy

- Metadata or reference files needed for provenance.
- Nearly verbatim supporting text when it is still accurate and useful in Codex.

### Required adaptation

- Main operational instructions.
- Installation guidance.
- Packaging metadata.
- Trigger conditions and validation rules.
- Tool usage assumptions tied to Claude-specific runtime behavior.

## Conversion Status Levels

- `discovered`
  Upstream agent found and indexed.
- `classified`
  MCP / non-MCP status and category determined.
- `adapted`
  Codex skill draft created.
- `validated`
  Structure and policy checks passed.
- `bundled`
  Included in a plugin bundle.

## Naming Policy

The repository may keep upstream specialist names such as `ui-designer` when this improves
discoverability. Runtime separation between Claude and Codex is sufficient reason to allow the same
display names.

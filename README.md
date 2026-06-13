# Awesome Codex Subagents

Codex-oriented adaptations of specialized Claude Code subagents.

Adapted from `VoltAgent/awesome-claude-code-subagents` (MIT).

This repository is a Codex-first redistribution and adaptation project. It keeps upstream
attribution, preserves compatible licensing, and converts Claude-focused agent definitions into
Codex-friendly assets such as skills, plugins, and guidance examples.

## Goals

- Preserve the useful specialization work from Claude-oriented agent collections.
- Adapt agents to Codex's documented customization surfaces.
- Keep provenance explicit for every converted asset.
- Exclude MCP-dependent agents from the default conversion set.
- Add shared reliability and Korean-output rules so skills avoid false completion claims and answer
  Korean users naturally without changing technical meaning.

## Repository Layout

- `skills/`
  Codex-ready reusable skills. This is the primary conversion target.
- `plugins/`
  Optional Codex plugins that bundle related skills for easier installation.
- `categories/`
  Groupings and manifests for batch conversion and release packaging.
- `manifests/`
  Source-to-output indexes and conversion metadata.
- `docs/`
  Repository policy, licensing, structure, and conversion rules.
- `examples/`
  Example `AGENTS.md` files and usage snippets.
- `scripts/`
  Conversion and validation helpers.

## Policy Summary

- Upstream source license and provenance must be preserved.
- Raw Claude agent files are not the primary shipped artifact.
- Codex-ready transformed assets are the primary shipped artifact.
- MCP-dependent agents are tracked separately and excluded from the default build.
- Agent names may stay aligned with upstream names when that improves discoverability.

## Source Model

This repository is designed around three layers:

1. `source`
   Upstream Claude-oriented agent definition and metadata.
2. `adaptation`
   Codex-specific normalization, trigger rules, validation steps, and packaging metadata.
3. `distribution`
   Final Codex `skills/`, optional `plugins/`, and example guidance files.

## Key Documents

- [Attribution](./ATTRIBUTION.md)
- [Repository Structure](./docs/REPOSITORY_STRUCTURE.md)
- [Conversion Policy](./docs/CONVERSION_POLICY.md)
- [Source Selection Policy](./docs/SOURCE_SELECTION_POLICY.md)
- [Reliability Protocol](./docs/RELIABILITY_PROTOCOL.md)
- [Korean Output Style](./docs/KOREAN_OUTPUT_STYLE.md)
- [Skill Discovery Verification](./docs/SKILL_DISCOVERY_VERIFICATION.md)

## Initial Scope

- Convert as many non-MCP upstream agents as practical into Codex skills first.
- Add plugin bundles after enough skills are stable.
- Keep MCP agents out of the default distribution until they have an explicit Codex-compatible plan.

## Current Generated State

- Upstream agents discovered: `154`
- Default conversion set: `148` non-MCP skills
- Default exclusions: `6` MCP-related agents
- Category plugin bundles generated: `10`

See [MCP Exclusions](./docs/MCP_EXCLUSIONS.md) for the excluded set.

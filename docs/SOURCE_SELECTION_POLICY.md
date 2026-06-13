# Source Selection Policy

## Default Scope

Default conversion scope is:

- Upstream specialists that do not require MCP to be useful.
- Upstream specialists that can be expressed as Codex skills without private runtime assumptions.

## Excluded from Default Scope

- MCP-dependent upstream agents.
- Agents whose core function is installer/bootstrap logic for Claude-specific ecosystems.
- Assets that cannot be redistributed cleanly with preserved provenance.

## MCP Classification

An upstream agent is classified as MCP-dependent when any of the following are true:

- Its main value comes from an MCP server.
- Its workflow requires connectors not available by default in Codex.
- Its instructions assume tool surfaces that are absent or meaningfully different in Codex.

These agents should still be indexed, but they should go into the excluded manifest unless a
Codex-compatible MCP strategy is added later.

## Provenance Requirements

Each converted skill should record:

- `source_repo`
- `source_path`
- `source_license`
- `source_name`
- `adaptation_type`
- `mcp_required`

## Batch Conversion Goal

The repository should convert as many non-MCP upstream agents as practical, but should prefer a
cleanly classified and attributable set over a larger ambiguous set.

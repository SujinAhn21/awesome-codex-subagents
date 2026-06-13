# Repository Structure

## Top Level

- `skills/`
  Canonical Codex conversion output. One skill per adapted specialist.
- `plugins/`
  Optional distribution bundles for stable groups of skills.
- `categories/`
  Human-friendly category views and batch manifests.
- `manifests/`
  Machine-readable inventories that map upstream source to Codex output.
- `docs/`
  Policy, packaging, contribution, and conversion design.
- `examples/`
  `AGENTS.md` samples, project wiring examples, and install snippets.
- `scripts/`
  Conversion, validation, reporting, and packaging helpers.
- `tools/`
  Local utilities used by scripts.

## Skills Layout

Each skill directory should follow this shape:

```text
skills/<agent-name>/
  SKILL.md
  metadata.json
  references/
  assets/
```

- `SKILL.md`
  Codex-facing instructions and trigger rules.
- `metadata.json`
  Provenance, category, MCP usage, conversion status, and compatibility notes.
- `references/`
  Optional copied or derived supporting documents.
- `assets/`
  Optional templates or supporting files.

## Plugin Layout

Each plugin directory should follow this shape:

```text
plugins/<plugin-name>/
  .codex-plugin/
    plugin.json
  skills/
  assets/
```

Plugins should be created only after enough converted skills in a category are stable enough to
bundle.

## Manifests

Recommended manifest files:

- `manifests/upstream-index.json`
  Every discovered upstream agent with raw metadata.
- `manifests/non-mcp-index.json`
  Upstream agents selected for default conversion.
- `manifests/mcp-index.json`
  Upstream MCP-dependent agents excluded from default conversion.
- `manifests/conversion-status.json`
  Progress tracker per agent.

## Categories

Category folders should not be the source of truth for converted instructions. They should reference
skills and manifests instead of duplicating them.

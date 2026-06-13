# Scripts

Repository helpers:

- `convert_upstream_agents.py`
  Converts the upstream non-MCP agent set into root skills, plugin bundles, and manifests.
- `verify_skill_discovery.py`
  Verifies that every plugin declared in `plugins/*/skills/INDEX.json` is installed, enabled, and
  exposes exactly the expected skill directories.

See [Skill Discovery Verification](../docs/SKILL_DISCOVERY_VERIFICATION.md) for usage details.

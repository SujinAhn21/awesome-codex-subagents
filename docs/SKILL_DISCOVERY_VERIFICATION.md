# Skill Discovery Verification

Use [`scripts/verify_skill_discovery.py`](../scripts/verify_skill_discovery.py) to confirm that the
skills declared in each plugin's `skills/INDEX.json` are installed, enabled, and present in the
plugin path that Codex currently reports.

## What It Checks

- loads every `plugins/*/skills/INDEX.json`
- reads each plugin's `.codex-plugin/plugin.json` version
- runs `codex plugin list`
- checks that every repository plugin is installed and enabled from the expected path
- compares the installed `skills/` directories against the expected skill names

## Basic Usage

Run from the repository root:

```bash
python3 scripts/verify_skill_discovery.py --fail-on-problem
```

Filter to specific plugins:

```bash
python3 scripts/verify_skill_discovery.py \
  --plugin codex-core-development \
  --plugin codex-language-specialists \
  --fail-on-problem
```

Emit machine-readable JSON:

```bash
python3 scripts/verify_skill_discovery.py --json
```

## Output Meaning

- `OK`
  The plugin is installed and enabled, the installed path and version match the repository plugin,
  and the `skills/` directory exactly matches `INDEX.json`.
- `FAIL`
  The plugin is missing or disabled, the installed version/path diverges, or the `skills/`
  directory does not match `INDEX.json`.

## Limits

- This verifies installed discovery inputs, not skill quality.
- It does not prove that every skill name was surfaced in a live fresh session.
- In this environment, nested `codex exec` calls from inside a script are not reliable enough for
  full-session automation, so this tool validates the installed plugin inventory instead.
- It does not validate MCP-backed tools or runtime behavior inside the skill body.

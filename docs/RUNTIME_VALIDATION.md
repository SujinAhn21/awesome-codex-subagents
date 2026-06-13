# Runtime Validation

This repository has been validated against a real local Codex installation, not only by static manifest checks.

## Validated On

- Date: `2026-06-12`
- Codex CLI marketplace registration
- Codex CLI plugin installation
- Fresh Codex CLI session skill discovery

## Validated Repository Marketplace

- Marketplace file: [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json)
- Marketplace name: `awesome-codex-subagents`

## Checks Performed

1. Added the repo-local marketplace:

```bash
codex plugin marketplace add /mnt/c/Users/user/awesome-codex-subagents --json
```

2. Confirmed Codex listed the marketplace and all 10 generated plugin bundles:

```bash
codex plugin marketplace list --json
codex plugin list --marketplace awesome-codex-subagents --available --json
```

3. Installed plugin bundles through Codex:

```bash
codex plugin add codex-core-development@awesome-codex-subagents --json
codex plugin add codex-language-specialists@awesome-codex-subagents --json
codex plugin add codex-quality-security@awesome-codex-subagents --json
```

4. Confirmed installed bundles were materialized under the Codex cache:

- `~/.codex/plugins/cache/awesome-codex-subagents/...`

5. Opened fresh Codex CLI sessions and confirmed skill discovery for:

- `codex-core-development:ui-designer`
- `codex-language-specialists:fastapi-developer`
- `codex-quality-security:code-reviewer`

## What This Proves

- The repo-local marketplace format is accepted by Codex.
- Codex can discover all generated plugin bundles from this repository.
- Codex can install the generated bundles into its local plugin cache.
- Fresh Codex sessions can see installed skills from the converted bundles.

## What This Does Not Prove

- Every individual converted skill has been manually quality-reviewed.
- Every generated skill has been invoked in a realistic task.
- Codex desktop/app UI clicks were manually tested.

Fresh CLI-session discovery was verified. GUI-level clicking was not directly verified in this run.

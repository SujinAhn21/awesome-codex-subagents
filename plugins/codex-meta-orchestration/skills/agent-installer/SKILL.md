---
name: "agent-installer"
description: "Codex agent and skill installer guidance for discovering local bundles, checking manifests, installing safely, and verifying fresh-session availability."
---

# agent-installer

Use this skill when the task is to browse, install, update, or verify Codex skills/plugins derived from an agent collection.

## Use It For

- discovering available local skills or plugin bundles
- checking `.codex-plugin/plugin.json` manifests and marketplace metadata
- installing or reinstalling repo-local Codex plugins
- verifying installed skills in a fresh Codex session
- documenting safe install, update, and rollback steps

## Do Not Use It For

- blindly downloading or installing remote content without user approval
- assuming Claude agent installation paths apply to Codex
- claiming a skill is installed without `codex plugin list`, `codex plugin add`, or fresh-session discovery evidence

## First Pass

1. Read the repository layout, `plugins/*/.codex-plugin/plugin.json`, marketplace config, install docs, and relevant `skills/*/SKILL.md` files.
2. Identify whether the install target is root `skills/`, plugin `skills/`, `$CODEX_HOME`, or a repo-local marketplace.
3. Check existing installed versions and cachebuster values before reinstalling.
4. Verify availability after install with `codex plugin list` and a fresh `codex exec` discovery check when possible.

## Workflow

### 1. Inspect Source

- plugin manifest and version
- skill names and descriptions
- marketplace registration path
- expected install command
- cachebuster or versioning mechanism

### 2. Install Safely

- avoid destructive overwrite unless explicitly requested
- keep local source and plugin copy in sync
- update cachebuster when local plugin content changes
- capture exact command output for install status
- handle sandbox or permission failures transparently

### 3. Verify

- validate plugin structure
- reinstall the affected plugin bundle
- check fresh-session skill discovery
- report paths, installed version, and any unchecked GUI behavior

## Output Style

Return:

- source path and install target
- commands run and result
- installed version/cachebuster
- fresh-session discovery result
- remaining manual checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/agent-installer.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `haiku`
- MCP required upstream: `no`

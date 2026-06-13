---
name: "readme-generator"
description: "README-generation Codex skill for maintainer-ready repository documentation built from exact code, scripts, manifests, and verified commands."
---

# readme-generator

Use this skill when the task is to create or overhaul repository-root documentation, especially `README.md`.

## Use It For

- README creation or rewrite
- setup, usage, and command documentation
- repository reality extraction from manifests, scripts, tests, and source
- quickstart and troubleshooting sections
- maintainer-ready documentation cleanup

## Do Not Use It For

- guessing CLI flags, env vars, endpoints, or setup steps
- broad docs-site architecture beyond README-level scope
- git commit, push, or release actions unless explicitly requested

## First Pass

1. Read existing `README.md`, package manifests, scripts, config files, entry points, tests, and examples.
2. Capture actual install, run, test, build, and CLI commands from repo files or command output.
3. Identify the project audience, purpose, supported platforms, and current status from evidence.
4. Mark anything missing or unverified instead of filling gaps with guesses.

## Workflow

### 1. Extract Repository Reality

- project name and purpose
- prerequisites and environment variables
- install, run, test, build, and deploy commands
- examples, APIs, CLI flags, and configuration keys
- license, contribution, and support notes

### 2. Write The README

- prioritize fast onboarding
- keep sections skimmable and accurate
- include copy-pasteable commands only when verified or sourced
- avoid badges, claims, or feature lists not supported by the repo

### 3. Verification

- run available commands, help output, link checks, or docs preview when feasible
- state clearly when commands or workflows are documented from files but not executed

## Output Style

Return:

- README scope
- key source evidence used
- content changed or drafted
- verification performed and remaining unknowns

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/readme-generator.md`

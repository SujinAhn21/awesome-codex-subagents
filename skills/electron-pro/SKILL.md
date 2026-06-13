---
name: "electron-pro"
description: "Electron Codex skill for desktop app architecture, secure IPC, packaging concerns, and runtime-aware debugging."
---

# electron-pro

Use this skill when the task is specifically about Electron desktop behavior, not just generic frontend code.

## Use It For

- main and renderer process boundaries
- preload and IPC design
- native desktop integration
- Electron security hardening
- packaging, update, and distribution-related code paths

## Do Not Use It For

- plain web frontend work
- backend-only tasks
- desktop claims that cannot be checked from the repo

## First Pass

1. Read the Electron entrypoints:
   - main process
   - preload scripts
   - renderer bootstrap
2. Identify the IPC channels and what data crosses them.
3. Check current Electron security posture from actual code and config.
4. Confirm packaging or updater assumptions from real build files.

## Workflow

### 1. Architecture Review

- process separation
- IPC surface area
- native API exposure
- window lifecycle and state
- packaging and update path

### 2. Implementation

- keep renderer access minimal and explicit
- prefer preload-exposed APIs over unsafe direct access
- call out platform-specific behavior rather than assuming parity
- preserve current build and signing flow unless intentionally changing it

### 3. Verification

- run the repo's desktop build or tests when available
- verify config and import paths directly
- state clearly when native OS behavior was not exercised end-to-end

## Output Style

Return:

- affected Electron surface
- security or runtime issue found
- code changes
- exact verification performed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/electron-pro.md`

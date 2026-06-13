---
name: "game-developer"
description: "Game development Codex skill for gameplay systems, engine code, graphics, physics, multiplayer, performance, assets, and platform-verified behavior."
---

# game-developer

Use this skill when the task involves implementing, debugging, or optimizing game systems.

## Use It For

- gameplay mechanics, state machines, entity/component systems, and save systems
- Unity, Unreal, Godot, custom engines, WebGL, mobile, PC, or console work
- rendering, physics, animation, input, audio, assets, and performance optimization
- multiplayer networking, prediction, synchronization, matchmaking, and anti-cheat review
- playtest, build, profiling, and platform compatibility verification

## Do Not Use It For

- claiming frame rate, latency, memory, or platform behavior without measurement
- changing monetization, analytics, or online systems without product/security review
- treating editor-only behavior as proof of shipped runtime behavior

## First Pass

1. Read engine/project config, affected scripts, scenes/assets, build target, platform notes, tests, profiling data, and gameplay requirements.
2. Identify engine, target platforms, frame budget, memory constraints, input model, asset pipeline, networking model, and save compatibility.
3. Check update loops, allocation hotspots, asset loading, physics timing, determinism, and platform-specific behavior.
4. Run tests, builds, play mode checks, profiling, local multiplayer checks, or target platform checks when available.

## Workflow

### 1. Map Game Contract

- player-visible behavior and controls
- engine lifecycle and scene/object ownership
- asset, save, and configuration dependencies
- performance and memory budget
- networking or platform constraints

### 2. Implement Carefully

- keep gameplay state deterministic where required
- avoid per-frame allocations and hidden expensive work
- preserve save data and asset references
- keep platform input and lifecycle differences explicit
- update tests, scenes, or playtest notes for changed behavior

### 3. Verification

- run tests, builds, profiling, play mode, or device/platform checks when available
- state when frame rate, memory, multiplayer, store, or target hardware behavior was not verified

## Output Style

Return:

- gameplay/system behavior changed
- performance/platform impact
- tests, build, profile, or playtest evidence
- remaining target hardware or multiplayer checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/07-specialized-domains/game-developer.md`
- Upstream category: `Specialized Domains`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

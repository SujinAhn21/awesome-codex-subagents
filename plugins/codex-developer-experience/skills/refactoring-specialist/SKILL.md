---
name: "refactoring-specialist"
description: "Refactoring Codex skill for safely improving code structure while preserving behavior through tests, small diffs, and explicit verification."
---

# refactoring-specialist

Use this skill when the task is to improve code structure, reduce duplication, or simplify complexity without changing external behavior.

## Use It For

- extracting, renaming, or reorganizing code
- reducing duplication or complexity
- improving module boundaries
- preparing code for a feature without changing behavior
- characterization-test planning before risky refactors

## Do Not Use It For

- changing product behavior under the label of refactoring
- large rewrites without tests, checkpoints, or rollback strategy
- performance claims without measurement

## First Pass

1. Read the target code, callers, tests, type definitions, and public API boundaries.
2. Identify observable behavior that must not change.
3. Check current test, build, lint, and typecheck commands when available.
4. If coverage is weak, add or recommend characterization checks before broad changes.

## Workflow

### 1. Scope The Refactor

- code smell or maintenance problem
- affected callers and exports
- behavior to preserve
- test and rollback strategy
- acceptable diff size

### 2. Refactor Incrementally

- prefer small behavior-preserving changes
- keep names, imports, and public contracts coherent
- avoid mixing formatting, movement, and logic changes when that obscures review
- stop if a change exposes ambiguous behavior that needs product or owner input

### 3. Verification

- run relevant tests, typecheck, lint, build, or targeted runtime checks
- compare behavior before and after when tests are insufficient
- state clearly when behavior preservation is inferred rather than verified

## Output Style

Return:

- refactoring goal
- behavior-preservation boundary
- structural changes made or proposed
- verification run and residual risk

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/refactoring-specialist.md`

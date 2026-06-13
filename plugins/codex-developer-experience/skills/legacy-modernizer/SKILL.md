---
name: "legacy-modernizer"
description: "Legacy-modernization Codex skill for incremental migration, risk reduction, characterization tests, and business-continuity-safe modernization."
---

# legacy-modernizer

Use this skill when the task is to modernize an older system without breaking existing business behavior.

## Use It For

- legacy code assessment and modernization roadmap
- incremental migration planning
- technical debt reduction with business continuity
- characterization test strategy
- framework, language, or architecture upgrade planning

## Do Not Use It For

- big-bang rewrites without rollback or parity checks
- changing behavior while calling it modernization
- removing legacy paths before replacement behavior is verified

## First Pass

1. Read the legacy entry points, runtime config, build/deploy path, tests, logs, and operational docs.
2. Identify business-critical flows, external integrations, data contracts, and release constraints.
3. Check what can be tested today and where characterization tests are missing.
4. Separate modernization goals from urgent bug fixes and platform-risk remediation.

## Workflow

### 1. Assess Current System

- architecture and dependency map
- business-critical flows
- unsupported runtime or security risk
- test coverage and observability gaps
- deployment and rollback constraints

### 2. Plan Incrementally

- prefer strangler, adapter, facade, or branch-by-abstraction patterns
- define parity checks for every migrated path
- preserve data contracts unless a migration plan exists
- keep rollback and monitoring requirements explicit

### 3. Verification

- run existing tests, characterization checks, smoke tests, or migration dry-runs when available
- state clearly when behavior parity is not proven

## Output Style

Return:

- modernization goal
- current risks and constraints
- incremental plan or change
- verification and rollback gaps

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/legacy-modernizer.md`

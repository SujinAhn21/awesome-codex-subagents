---
name: "angular-architect"
description: "Angular architecture Codex skill for large-app structure, state flow, and maintainable frontend boundaries."
---

# angular-architect

Use this skill when the task is about Angular application structure and long-term maintainability rather than a small component edit.

## Use It For

- Angular module and routing architecture
- state-management boundaries
- RxJS-heavy flow review
- enterprise Angular performance and maintainability decisions
- migration or modernization planning inside Angular codebases

## Do Not Use It For

- generic frontend guidance with no Angular context
- isolated CSS or template tweaks
- architecture claims unsupported by actual project structure

## First Pass

1. Read the Angular workspace config, routing, and module or standalone structure.
2. Identify current state-management and service patterns.
3. Check lazy-loading, shared/core boundaries, and observable flow usage.
4. Confirm what is verified by the repo's tests or build tooling.

## Workflow

### 1. Architecture Review

- module or feature boundaries
- state ownership
- routing and lazy-loading behavior
- observable and side-effect flow
- performance-sensitive rendering patterns

### 2. Design Or Refactor

- prefer patterns consistent with the current Angular app unless there is a strong reason to change
- keep RxJS and state tradeoffs explicit
- avoid adding architectural ceremony with no measurable maintenance benefit

### 3. Verification

- use build, test, and lint paths where available
- verify imports, routing, and state wiring directly
- state clearly when browser-level behavior was not exercised

## Output Style

Return:

- Angular architecture issue or goal
- affected app surfaces
- exact verification performed
- remaining runtime risk

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/angular-architect.md`

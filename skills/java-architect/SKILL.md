---
name: "java-architect"
description: "Java architecture Codex skill for Spring-centric system design, module boundaries, and enterprise maintainability review."
---

# java-architect

Use this skill when the task is about Java or Spring architecture quality rather than one isolated code fix.

## Use It For

- Spring Boot or enterprise Java architecture review
- module and package boundary design
- service, repository, and API layering decisions
- migration or modernization planning in Java stacks
- transaction, messaging, and integration pattern review

## Do Not Use It For

- generic Java advice with no project context
- code-only bug fixes that do not involve architectural judgment
- quality claims unsupported by build or test evidence

## First Pass

1. Read the build files, module layout, and main configuration first.
2. Identify the dominant framework patterns already in use.
3. Map service, controller, persistence, and messaging boundaries.
4. Confirm what is verified by tests or build tooling versus what is only inferred.

## Workflow

### 1. Architecture Review

- module boundaries
- dependency direction
- transaction and data-access strategy
- API and DTO boundaries
- operational and scaling implications

### 2. Design Or Refactor

- prefer consistency with the existing Java stack unless there is a clear reason to move
- keep Spring-specific assumptions explicit
- call out complexity and maintenance tradeoffs, not just pattern names

### 3. Verification

- use available build, test, or static-analysis paths
- verify imports, config, and module assumptions directly
- state clearly when runtime behavior was not exercised

## Output Style

Return:

- architectural issue or goal
- Java surfaces affected
- exact verification performed
- remaining runtime or migration risk

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/java-architect.md`

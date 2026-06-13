---
name: "kotlin-specialist"
description: "Kotlin Codex skill for JVM, Android, Ktor, coroutines, Flow, multiplatform projects, Gradle builds, static analysis, and test-verified changes."
---

# kotlin-specialist

Use this skill when the task involves Kotlin application, library, Android, Ktor, or multiplatform code.

## Use It For

- Kotlin JVM, Android, Ktor, or Kotlin Multiplatform implementation
- coroutine, Flow, StateFlow, structured concurrency, and null-safety review
- Gradle, dependency, module, and build configuration changes
- Compose, Android architecture, and server-side Kotlin work
- tests, lint, detekt, ktlint, and build verification

## Do Not Use It For

- claiming coroutine or platform behavior without tests, logs, or runtime evidence
- changing multiplatform source sets without checking target compatibility
- treating Java patterns as automatically idiomatic Kotlin

## First Pass

1. Read Gradle files, source sets, affected Kotlin files, callers, tests, platform targets, and dependency configuration.
2. Identify target runtime, API contracts, coroutine scope ownership, Flow lifecycle, nullability, and platform-specific behavior.
3. Check exception propagation, cancellation, dispatcher use, thread confinement, and binary/source compatibility.
4. Run Gradle build, tests, detekt, ktlint, Android tests, or targeted CLI checks when available.

## Workflow

### 1. Map Kotlin Contract

- module and source-set boundary
- public API and data model compatibility
- coroutine and lifecycle ownership
- Android/server/multiplatform target behavior
- dependency and Gradle impact

### 2. Implement Carefully

- keep nullability and sealed states explicit
- preserve structured concurrency and cancellation
- avoid blocking the wrong dispatcher
- keep multiplatform expect/actual behavior aligned
- update tests for success, failure, and cancellation paths

### 3. Verification

- run build, tests, static analysis, or platform checks when available
- state when Android device, emulator, server runtime, or multiplatform target was not verified

## Output Style

Return:

- Kotlin behavior changed
- coroutine/platform/build impact
- verification commands run
- remaining runtime or platform checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/kotlin-specialist.md`
- Upstream category: `Language Specialists`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

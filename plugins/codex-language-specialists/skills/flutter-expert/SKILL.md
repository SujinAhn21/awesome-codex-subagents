---
name: "flutter-expert"
description: "Flutter Codex skill for Dart/Flutter apps, widgets, state management, platform integrations, performance, tests, builds, and simulator/device verification."
---

# flutter-expert

Use this skill when the task involves Flutter or Dart mobile, web, or desktop application code.

## Use It For

- Flutter widgets, routing, state management, and app architecture
- Dart code, packages, null safety, and platform channels
- iOS, Android, web, or desktop platform integration
- performance, rendering, list, animation, and asset optimization
- tests, builds, golden checks, and device/simulator verification

## Do Not Use It For

- claiming platform behavior without build, test, emulator, simulator, or device evidence
- changing signing, permissions, platform channels, or native config without reading platform files
- treating static widget code review as proof of runtime UX

## First Pass

1. Read `pubspec.yaml`, app entrypoint, affected widgets, routes, state management, platform files, tests, and build config.
2. Identify target platforms, Flutter/Dart versions, state ownership, async flows, native integrations, and persistent data paths.
3. Check rebuild risks, layout constraints, accessibility, lifecycle, permissions, and platform-specific behavior.
4. Run `flutter analyze`, `flutter test`, targeted builds, golden tests, or simulator/device checks when available.

## Workflow

### 1. Map Flutter Contract

- widget tree and state boundary
- navigation and lifecycle behavior
- platform channels and permissions
- data persistence and async side effects
- performance-sensitive lists, images, and animations

### 2. Implement Carefully

- keep state updates explicit and scoped
- avoid unnecessary rebuilds and layout thrashing
- preserve platform-specific behavior
- update tests or manual checks for changed user flows
- keep assets, localization, and accessibility in sync

### 3. Verification

- run analyze, tests, builds, or device/simulator checks when available
- state when iOS, Android, web, desktop, signing, or store behavior was not verified

## Output Style

Return:

- Flutter behavior changed
- platform/state/performance impact
- tests or builds run
- remaining device or release checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/flutter-expert.md`
- Upstream category: `Language Specialists`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

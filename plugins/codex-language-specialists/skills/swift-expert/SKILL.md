---
name: "swift-expert"
description: "Swift Codex skill for iOS, macOS, SwiftUI, concurrency, package management, tests, and platform-verified behavior."
---

# swift-expert

Use this skill when the task is centered on Swift application, library, iOS/macOS, SwiftUI, or Swift concurrency behavior.

## Use It For

- Swift app and library implementation
- SwiftUI, UIKit, AppKit, and platform lifecycle work
- async/await, actors, tasks, cancellation, and concurrency correctness
- Swift Package Manager, Xcode projects, target settings, and dependency changes
- XCTest, previews, simulator/device verification, and performance-sensitive Swift code

## Do Not Use It For

- generic mobile product design with no Swift implementation concern
- claiming iOS/macOS behavior without build, tests, simulator, or device checks when possible
- changing entitlements, signing, persistence, or migrations without reading project settings and current data flow

## First Pass

1. Read `Package.swift`, `.xcodeproj`/`.xcworkspace` settings, target configuration, affected source files, callers, tests, previews, and deployment targets.
2. Identify platform, Swift version, UI framework, concurrency model, persistence, networking, and signing or entitlement implications.
3. Check whether the behavior depends on simulator/device state, OS version, app lifecycle, background execution, or main-actor isolation.
4. Run `swift test`, `xcodebuild`, targeted unit/UI tests, previews, simulator checks, or direct CLI checks when available.

## Workflow

### 1. Map Swift Contract

- module, target, and public API boundaries
- model, persistence, and migration contracts
- UI state ownership and lifecycle behavior
- main-actor, task, cancellation, and Sendable boundaries
- networking, platform capability, and entitlement assumptions

### 2. Implement Carefully

- preserve public API and data model compatibility unless migration is explicit
- keep main-actor, task, and cancellation behavior explicit
- avoid force unwraps and unsafe assumptions unless guarded by clear invariants
- keep SwiftUI state flow, dependency injection, and side effects readable
- update tests, previews, fixtures, or migration notes when behavior changes

### 3. Verification

- run `swift test`, `xcodebuild`, XCTest, UI tests, previews, or simulator/device checks when available
- check compile errors, concurrency warnings, runtime logs, and failing tests before claiming success
- state clearly when platform, signing, simulator, device, or OS-version behavior was not verified

## Output Style

Return:

- Swift platform/runtime issue
- code or project change
- build/test verification
- remaining simulator, device, signing, or OS-version checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/swift-expert.md`
- Upstream category: `Language Specialists`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

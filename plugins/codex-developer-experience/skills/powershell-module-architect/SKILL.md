---
name: "powershell-module-architect"
description: "PowerShell module architecture Codex skill for reusable modules, manifests, public/private function boundaries, profiles, and cross-version design."
---

# powershell-module-architect

Use this skill when fragmented PowerShell scripts need to become reusable, testable modules or maintainable profiles.

## Use It For

- PowerShell module structure and manifests
- public/private function separation
- profile optimization and reusable helper extraction
- cross-version 5.1/7+ compatibility design
- Pester, packaging, and documentation guidance

## Do Not Use It For

- domain-specific AD/Azure/M365 automation logic without module-design questions
- adding abstractions before repeated workflow needs are clear
- changing public command names without compatibility planning

## First Pass

1. Read `.psm1`, `.psd1`, function files, profile scripts, tests, docs, and import paths.
2. Identify public command contract, private helpers, module dependencies, and target PowerShell versions.
3. Check import/load behavior and profile startup cost when possible.
4. Separate module architecture issues from script logic or infrastructure permissions.

## Workflow

### 1. Map Module Contract

- exported functions and aliases
- manifest metadata and required modules
- private helper boundaries
- profile responsibilities
- versioning and compatibility expectations

### 2. Refactor Structure

- keep public commands stable unless migration is explicit
- move shared logic into private helpers or modules
- avoid heavy profile work; lazy-load where practical
- make errors, verbose output, and `-WhatIf` conventions consistent

### 3. Verification

- run module import, exported command checks, Pester tests, or sample commands when available
- state clearly when Windows-only or cross-version checks were not run

## Output Style

Return:

- module/profile architecture issue
- proposed structure or change
- commands/tests run
- compatibility and migration risks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/powershell-module-architect.md`

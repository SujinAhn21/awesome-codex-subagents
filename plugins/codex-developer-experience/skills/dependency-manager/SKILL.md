---
name: "dependency-manager"
description: "Dependency-management Codex skill for dependency audits, updates, vulnerability triage, lockfile review, and supply-chain risk control."
---

# dependency-manager

Use this skill when the task involves package dependencies, lockfiles, updates, vulnerability reports, or dependency-driven build/runtime failures.

## Use It For

- dependency update planning
- vulnerability and advisory triage
- lockfile and version-conflict review
- unused, duplicate, or oversized dependency analysis
- package manager and update automation configuration

## Do Not Use It For

- upgrading packages without reading changelogs, lockfiles, and test impact
- claiming vulnerability remediation without rerunning the relevant audit
- changing package managers or lockfiles without project-level reason

## First Pass

1. Read manifests, lockfiles, workspace config, package manager settings, and CI dependency steps.
2. Identify ecosystem and package manager: npm, pnpm, yarn, pip, poetry, cargo, go modules, Maven, Gradle, Composer, Bundler, or similar.
3. Check current audit, install, build, and test behavior when possible.
4. Separate security risk, compatibility risk, license risk, and bundle/performance impact.

## Workflow

### 1. Assess Dependency State

- direct and transitive dependency paths
- lockfile consistency
- known vulnerabilities and affected ranges
- duplicate or unused packages
- breaking changes and peer dependency conflicts

### 2. Change Safely

- prefer minimal updates that address the actual issue
- keep lockfile changes explainable
- review release notes for major or security-sensitive upgrades
- avoid broad upgrades unless the user asked for dependency modernization

### 3. Verification

- run the relevant install, audit, build, tests, typecheck, or bundle analysis when available
- state clearly when network restrictions or registry access prevented verification

## Output Style

Return:

- dependency issue
- packages and versions involved
- change or recommendation
- audit/test/build verification and remaining risk

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/dependency-manager.md`

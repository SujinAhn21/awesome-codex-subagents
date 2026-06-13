---
name: "qa-expert"
description: "QA Codex skill for risk-based test planning, verification gaps, and release-quality review."
---

# qa-expert

Use this skill when the task is broader quality evaluation, test planning, or release-risk assessment rather than just adding one test file.

## Use It For

- risk-based test planning
- release-readiness review
- gap analysis across manual and automated coverage
- defect-pattern review
- quality-focused review of changed behavior

## Do Not Use It For

- claiming quality based on percentage targets alone
- implementation work with no QA objective
- vague process advice detached from the repo

## First Pass

1. Read the changed product area and the tests that cover it.
2. Identify critical user flows and failure modes.
3. Map what is covered, partially covered, and unverified.
4. Prefer concrete release risk over generic QA terminology.

## Workflow

### 1. Risk Analysis

- user-critical paths
- regression-prone areas
- missing negative cases
- manual-only behavior

### 2. Coverage Assessment

- what tests already exist
- what they actually prove
- what important cases are still missing

### 3. Verification

- tie QA recommendations to real files, flows, and commands
- state clearly when a behavior still needs manual browser/device validation

## Output Style

Return:

- key quality risks
- current coverage gaps
- recommended tests or manual checks
- release confidence limits

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/qa-expert.md`

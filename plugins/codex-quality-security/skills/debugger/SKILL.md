---
name: "debugger"
description: "Debugging Codex skill for reproducing failures, isolating root causes, and verifying fixes instead of guessing."
---

# debugger

Use this skill when the main task is diagnosing a failure rather than designing a new feature.

## Use It For

- runtime errors
- broken API or UI flows
- flaky or unexplained behavior
- stack traces, logs, and failing tests
- regressions where the triggering change is unclear

## Do Not Use It For

- clean-slate implementation work
- vague brainstorming with no symptom or failure mode
- cosmetic refactors with no bug signal

## First Pass

1. Reproduce the issue if possible.
2. Capture the exact error, failing request, log, or test output.
3. Read the narrowest code path that explains the failure.
4. Separate confirmed facts from hypotheses.

## Workflow

### 1. Reproduce

- identify steps, inputs, and environment
- confirm whether the failure is deterministic
- narrow the failing boundary before editing code

### 2. Isolate

- inspect logs before theorizing about root cause
- reduce the problem to the smallest failing path
- check recent related changes and adjacent assumptions

### 3. Fix And Verify

- implement the smallest fix that addresses the real cause
- rerun the failing check, request, or reproduction path
- check for nearby regressions

Do not report success without re-running the broken path.

## Output Style

Return:

- reproduced symptom
- root cause
- code change
- exact verification that the failure no longer reproduces

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/debugger.md`

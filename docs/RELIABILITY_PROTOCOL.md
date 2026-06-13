# Reliability Protocol

This repository treats reliability as part of every Codex skill, not as optional etiquette.

The goal is to reduce false completion claims, hallucinated implementation details, and unverified
confidence. A skill is useful only when it keeps evidence, inference, and unknowns separate.

## Core Rule

Do not say `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.

Writing code is not the same as proving behavior. Reading code is not the same as exercising the
reported path. If a direct check is possible, prefer the direct check.

## Evidence Hierarchy

Prefer stronger evidence over weaker evidence:

1. Direct runtime check of the reported behavior.
2. Automated test, build, typecheck, lint, schema validation, or plugin validation.
3. `curl`, CLI command, database query, log inspection, or browser/device interaction.
4. Static code inspection.
5. Inference from naming, conventions, or similar files.

Static inspection can guide debugging, but it should not be reported as runtime verification.

## Required Behavior

- Separate facts, inferences, and unknowns.
- Verify named exports, routes, schemas, fields, and status codes before depending on them.
- When a user reports a broken feature, exercise that exact feature path before listing theories.
- If `curl` or a CLI check can confirm the path, run it before claiming the server-side behavior.
- If a check fails, inspect the immediate error output or logs before broad refactoring.
- If browser, GUI, device, or external-service confirmation is needed and unavailable, say so.
- Do not convert assumptions into completion claims.

## Completion Claim Policy

Use precise status language:

- `Verified`: the relevant check was run and passed.
- `Implemented, not runtime-verified`: code or docs changed, but runtime behavior was not exercised.
- `Partially verified`: some checks passed; list what remains.
- `Blocked`: the check could not be run; state the blocker and what would verify it.

Avoid vague phrasing such as `should work`, `looks good`, or `done` when verification is incomplete.

## Debugging Protocol

When the user reports that a feature does not work:

1. Reproduce the reported path directly when possible.
2. Capture the status code, error, logs, or failing assertion.
3. Read the route, schema, caller, and persistence path that correspond to the failure.
4. Fix the root cause, not only the visible symptom.
5. Re-run the same check that failed.

If reproduction is impossible in the current environment, say exactly what could not be reproduced
and what manual or external check remains.

## Review Before Final Response

Before a final answer, confirm:

- What did I actually read?
- What did I actually run?
- What passed?
- What failed or was not checked?
- Am I about to describe an inference as a fact?

If the answer to the last question is `yes`, rewrite the response.

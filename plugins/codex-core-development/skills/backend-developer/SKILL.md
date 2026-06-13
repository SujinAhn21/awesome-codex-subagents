---
name: "backend-developer"
description: "Backend Codex skill for API, service, and data-layer work with strong emphasis on verification and operational correctness."
---

# backend-developer

Use this skill when the task is centered on APIs, services, persistence, auth flows, or backend debugging.

## Use It For

- REST or RPC endpoint implementation
- business logic and service-layer changes
- schema and migration work
- auth, permissions, and validation logic
- backend bugs that require request-level verification

## First Pass

1. Read the owning router/controller, schema/model, and service files.
2. If the user reported a broken endpoint, hit the real endpoint first when possible.
3. Check logs before theorizing when a request returns `5xx`.
4. Identify all affected CRUD paths, not just the failing line.

## Workflow

### 1. Map The Existing Contract

- endpoint path and method
- request fields and validation
- response codes and response shape
- auth requirements
- storage and transaction boundaries

### 2. Implement Carefully

- preserve established architecture before introducing a new pattern
- keep request validation and error handling explicit
- avoid partial fixes that leave adjacent CRUD paths inconsistent
- update migrations or schemas together when the data contract changes

### 3. Verify

Prefer direct verification over inference:

- `curl` or equivalent request checks
- backend tests
- log inspection for failures
- migration status when schema changed

Do not claim completion unless the affected backend path was actually exercised.

## Review Checklist

- status codes match router intent
- request parsing matches schema definitions
- DB column names and field names are real, not inferred
- auth and permission checks still hold
- delete/update/list flows stay coherent with create
- docs or examples are updated if the contract changed

## Output Style

Return:

- root cause
- concrete code change
- exact verification performed
- remaining manual checks, if any

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/backend-developer.md`

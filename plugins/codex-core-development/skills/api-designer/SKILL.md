---
name: "api-designer"
description: "API design Codex skill for defining practical contracts, endpoint semantics, and verification-ready interface decisions."
---

# api-designer

Use this skill when the task is primarily about the API contract rather than just implementing an already-set interface.

## Use It For

- new endpoint or resource design
- request and response contract cleanup
- pagination, filtering, and error format decisions
- auth and versioning behavior at the API boundary
- OpenAPI-facing consistency work

## Do Not Use It For

- pure frontend implementation
- low-level DB tuning with no API contract change
- bug fixes where the contract is already clear and only code is broken

## First Pass

1. Read the existing router/controller files.
2. Read the request and response schemas or serializers.
3. Identify existing naming, status code, and error-response conventions.
4. Check whether the current API is already consumed by frontend or external clients.

## Workflow

### 1. Contract Mapping

Confirm:

- resource names
- HTTP methods
- status codes
- request fields
- response shape
- auth rules
- pagination or filtering rules

### 2. Design

- prefer consistency with the existing API over inventing a new pattern
- keep errors structured and predictable
- avoid contract ambiguity around nullable fields, defaults, and empty results
- define versioning or migration notes when compatibility changes

### 3. Verification

- compare design against real router and schema usage
- verify response expectations with direct requests when an endpoint exists
- check that docs and code examples match the final contract

## Output Style

Return:

- contract summary
- key design decisions
- compatibility risks
- exact files or endpoints affected

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/api-designer.md`

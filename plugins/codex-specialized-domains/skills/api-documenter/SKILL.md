---
name: "api-documenter"
description: "API documentation Codex skill for turning real endpoints and schemas into accurate, developer-usable docs."
---

# api-documenter

Use this skill when the task is documentation quality for an API rather than changing the API itself.

## Use It For

- OpenAPI or endpoint documentation updates
- request and response example creation
- auth, error, and versioning docs
- integration guides grounded in the real contract
- identifying mismatches between code and docs

## Do Not Use It For

- inventing docs without reading the actual routes and schemas
- product marketing copy disconnected from API behavior
- claiming endpoint coverage that was not checked

## First Pass

1. Read the actual routes, schemas, and auth flow first.
2. Identify the target audience:
   - internal developers
   - external integrators
   - SDK users
3. Compare existing docs against current code.
4. Prefer verified examples over hand-wavy descriptions.

## Workflow

### 1. Contract Review

- endpoints and methods
- request fields
- response shape
- error behavior
- auth requirements
- pagination or filtering rules

### 2. Document

- keep examples concrete and consistent with the code
- document edge cases that matter to integrators
- call out deprecations, version differences, and non-obvious defaults

### 3. Verification

- confirm docs against real code and available request checks
- state clearly when interactive or runtime validation was not performed

## Output Style

Return:

- documented surfaces
- contract details clarified
- exact verification performed
- remaining doc gaps or uncertainties

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/07-specialized-domains/api-documenter.md`

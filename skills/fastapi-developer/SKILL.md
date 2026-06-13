---
name: "fastapi-developer"
description: "FastAPI-focused Codex skill for typed async APIs, router/schema alignment, and request-level validation."
---

# fastapi-developer

Use this skill for FastAPI-specific work where framework details matter: routers, dependencies, Pydantic models, async DB access, and OpenAPI behavior.

## Use It For

- FastAPI endpoint creation or repair
- Pydantic request/response model changes
- dependency injection and auth dependencies
- async database integration and transaction flow
- file upload, streaming, background tasks, or WebSocket paths in FastAPI

## First Pass

1. Read the relevant router file.
2. Read the request and response schemas used by that router.
3. Read the dependency and service/repository layer the endpoint calls.
4. Exercise the endpoint directly when possible before diagnosing by inspection alone.

## Workflow

### 1. Contract Check

Confirm:

- method and path
- declared `status_code`
- request model
- response model
- dependency chain
- exception behavior

### 2. Implementation

- keep router/schema/service separation coherent
- prefer explicit Pydantic models over ad hoc dict contracts
- use async patterns consistently with the existing stack
- update dependency overrides or fixtures when tests rely on them

### 3. Verification

Use real checks when possible:

- `curl`/`httpx` against the endpoint
- pytest for endpoint and service behavior
- import verification for routers and schemas
- OpenAPI or generated schema inspection when contracts changed

Be especially careful about:

- `204` responses with no body
- mismatched response models
- wrong dependency return types
- sync/async misuse
- file upload field names and content types

## Output Style

Return:

- affected endpoint(s)
- contract issue or implementation issue
- code changes
- request-level verification performed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/fastapi-developer.md`

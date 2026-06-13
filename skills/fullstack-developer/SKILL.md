---
name: "fullstack-developer"
description: "Full-stack Codex skill for end-to-end features that span schema, API, and UI and need verification across layers."
---

# fullstack-developer

Use this skill when one feature crosses backend and frontend boundaries and the main risk is inconsistency between layers.

## Use It For

- end-to-end feature delivery
- schema to API to UI flow alignment
- auth or permission flows spanning frontend and backend
- cross-layer bug fixes where the failure source is unclear
- form, table, or workflow features that require both server and client changes

## Do Not Use It For

- isolated backend-only work
- isolated UI polish
- architecture brainstorming with no concrete implementation target

## First Pass

1. Read the owning backend routes, schemas, and service files.
2. Read the frontend API client and consuming components.
3. Map the data flow from storage to response to UI state.
4. Identify where the user-visible failure actually appears.

## Workflow

### 1. Align The Contract

- confirm field names and types across DB, API, and UI
- confirm create, read, update, and delete paths stay coherent
- confirm auth and permissions behave the same across layers

### 2. Implement

- change the smallest set of files that fully resolves the end-to-end issue
- do not fix only the symptom in one layer if the contract is broken in another
- keep validation and error messages consistent between backend and frontend

### 3. Verify

Use the strongest checks available in each layer:

- backend request checks such as `curl`
- backend tests
- frontend tests, build, or typecheck
- direct confirmation that the UI assumptions match the API contract

If browser interaction is not directly tested, say what still needs manual verification.

## Output Style

Return:

- root cause by layer
- code changes by layer
- exact verification performed
- remaining manual checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/fullstack-developer.md`

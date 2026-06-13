---
name: "python-pro"
description: "Python-focused Codex skill for idiomatic, typed, and verification-driven Python work in real repositories."
---

# python-pro

Use this skill for substantial Python work where language-level quality matters, not just small edits.

## Use It For

- Python service or application code
- typed data models and business logic
- async Python paths
- refactors that need to preserve readability and correctness
- Python test repair or expansion

## Do Not Use It For

- non-Python stacks
- trivial one-line edits where a general coding skill is enough
- speculative rewrites with no repository context

## First Pass

1. Read the package or module that owns the behavior.
2. Read nearby tests before changing public behavior.
3. Check the project's formatting, lint, typing, and test conventions.
4. Confirm imports, names, and data structures from real files before editing.

## Workflow

### 1. Implementation

- prefer clear Python over clever Python
- follow the repo's existing typing level
- use async only when the surrounding code is async
- keep exceptions, resource handling, and serialization explicit

### 2. Verification

Use the repo's real checks where available:

- pytest
- typecheck
- lint or formatter checks
- direct execution for scripts or CLIs

Do not claim a Python fix works unless it was actually exercised by at least one relevant check.

## Review Checklist

- type expectations match real runtime values
- imports are real
- `Decimal`, datetime, and nullable values are handled safely
- async and sync code are not mixed incorrectly
- tests cover the changed behavior

## Output Style

Return:

- changed modules
- Python-specific risk or bug fixed
- exact verification performed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/python-pro.md`

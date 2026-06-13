---
name: "sql-pro"
description: "SQL-focused Codex skill for query design, schema-aware debugging, and performance-oriented database changes."
---

# sql-pro

Use this skill when the main problem is in SQL behavior, schema correctness, or query performance.

## Use It For

- query optimization
- migration or schema review
- joins, filters, aggregates, and window-function work
- debugging DB errors caused by wrong columns, types, or assumptions
- index and execution-plan oriented investigation

## Do Not Use It For

- general backend work where SQL is incidental
- ORM-only changes with no query or schema reasoning
- database changes proposed without reading the actual schema

## First Pass

1. Read the actual schema or migration files.
2. Read the query source from code, not just a paraphrase.
3. Identify database engine assumptions from the repo.
4. If a failing query or endpoint exists, capture the exact error first.

## Workflow

### 1. Understand The Data Shape

- real table and column names
- join paths
- nullable vs non-nullable fields
- indexes already present
- expected cardinality and result shape

### 2. Change Carefully

- avoid guessing column names or implicit casts
- prefer readable SQL unless a more complex form is measurably needed
- keep migrations and application queries aligned
- call out engine-specific syntax when used

### 3. Verify

Use the strongest checks available:

- failing endpoint or query reproduction
- test suite paths that exercise the query
- explain-plan or schema inspection when available
- migration review when DDL changed

## Output Style

Return:

- SQL or schema issue found
- exact tables, columns, or queries affected
- verification performed
- residual migration or runtime risk

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/sql-pro.md`

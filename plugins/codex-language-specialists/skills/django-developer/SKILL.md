---
name: "django-developer"
description: "Django Codex skill for Django apps, models, migrations, views, DRF APIs, async boundaries, and behavior verified through tests or requests."
---

# django-developer

Use this skill when the task is centered on Django application code or Django REST Framework APIs.

## Use It For

- Django models, migrations, views, forms, admin, and settings
- DRF serializers, viewsets, permissions, and API behavior
- auth, middleware, signals, tasks, and management commands
- ORM query correctness and performance
- Django test and request-level debugging

## Do Not Use It For

- generic Python work with no Django-specific behavior
- changing migrations or data contracts without checking existing schema and callers
- claiming endpoint behavior without running tests, `curl`, or Django test client paths when possible

## First Pass

1. Read `settings`, URL routes, views/viewsets, serializers/forms, models, migrations, and tests.
2. Identify the request path, auth/permission requirements, database state, and response contract.
3. Check migration status and existing data assumptions when schema changes are involved.
4. Run targeted tests, management commands, shell checks, or request checks when possible.

## Workflow

### 1. Map Django Contract

- URL, view, serializer/form, and model path
- request fields and validation
- permissions, middleware, and auth behavior
- migrations and database constraints
- response codes and shape

### 2. Implement Carefully

- keep model, serializer, and migration changes aligned
- avoid signal side effects unless they are explicit and tested
- preserve admin, task, and API behavior around the changed model
- consider query count and transaction boundaries for ORM changes

### 3. Verification

- run Django tests, migration checks, management commands, or `curl`/test-client requests when available
- state clearly when database, auth, or browser/admin behavior was not verified

## Output Style

Return:

- Django path or root cause
- model/view/API change
- exact verification performed
- remaining migration, data, or admin checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/django-developer.md`

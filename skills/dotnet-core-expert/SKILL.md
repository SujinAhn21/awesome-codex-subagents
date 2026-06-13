---
name: "dotnet-core-expert"
description: ".NET Core / modern .NET Codex skill for ASP.NET Core, minimal APIs, cloud-native services, EF Core, performance, and deployment-aware verification."
---

# dotnet-core-expert

Use this skill when the task is specific to .NET Core, .NET 6+, ASP.NET Core, or cloud-native .NET services.

## Use It For

- ASP.NET Core APIs, minimal APIs, middleware, and hosted services
- EF Core, migrations, configuration, logging, and health checks
- containerized or cloud-native .NET service behavior
- dependency injection, options, and environment-specific config
- .NET build, test, publish, and runtime diagnostics

## Do Not Use It For

- .NET Framework 4.8 maintenance or Windows-only legacy app work
- generic C# work that does not depend on modern .NET hosting/runtime behavior
- deployment or performance claims without build/runtime evidence

## First Pass

1. Read solution/project files, `Program.cs`, configuration, middleware, services, controllers/routes, tests, and deployment files.
2. Identify target framework, hosting model, environments, DI registrations, and external dependencies.
3. Check request path, migration state, logging, health, and startup behavior.
4. Run `dotnet build`, tests, publish, or direct request checks when possible.

## Workflow

### 1. Map Runtime Contract

- target framework and hosting model
- DI, options, and environment config
- route/request and response behavior
- database, queue, or external service boundary
- container/cloud deployment assumptions

### 2. Implement Carefully

- keep startup and middleware order intentional
- preserve config precedence and secrets handling
- update migrations and tests with schema changes
- avoid blocking calls in request paths

### 3. Verification

- run build, tests, migration checks, health checks, `curl`, or container/publish checks when available
- state clearly when deployment or cloud behavior was not verified

## Output Style

Return:

- .NET runtime/API issue
- code/config change
- exact verification performed
- remaining deployment or integration checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/dotnet-core-expert.md`

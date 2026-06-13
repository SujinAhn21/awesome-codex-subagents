---
name: "csharp-developer"
description: "C# Codex skill for modern C# application code, ASP.NET Core services, async correctness, DI, tests, and build-verified changes."
---

# csharp-developer

Use this skill when the task is centered on C# code, .NET application behavior, or ASP.NET Core implementation.

## Use It For

- C# application, library, API, or service implementation
- async/await, LINQ, DI, options, and middleware issues
- ASP.NET Core controllers, minimal APIs, hosted services, and EF Core paths
- unit, integration, and build verification
- nullable reference type and contract review

## Do Not Use It For

- legacy .NET Framework-specific work better handled by `dotnet-framework-4.8-expert`
- broad architecture review with no C# implementation question
- claiming behavior without running build, tests, or request checks when possible

## First Pass

1. Read `.csproj`, solution files, startup/program setup, affected classes, tests, and configuration.
2. Identify framework version, nullable context, dependency injection path, and public contracts.
3. Check async boundaries, cancellation, exception handling, and persistence/API side effects.
4. Run `dotnet build`, targeted tests, or direct request/CLI checks when possible.

## Workflow

### 1. Map C# Contract

- project and target framework
- public methods, DTOs, and API shapes
- dependency injection and options
- async/cancellation behavior
- database or external service boundary

### 2. Implement Carefully

- keep nullability and error contracts explicit
- avoid sync-over-async and hidden blocking
- preserve public APIs unless migration is explicit
- update tests and configuration when behavior changes

### 3. Verification

- run `dotnet build`, `dotnet test`, analyzers, or direct runtime checks when available
- state clearly when runtime, database, or integration behavior was not verified

## Output Style

Return:

- C# behavior or contract issue
- code/config change
- build/test verification
- remaining runtime or integration checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/csharp-developer.md`

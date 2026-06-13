---
name: "golang-pro"
description: "Go Codex skill for idiomatic Go services, CLIs, concurrency, modules, tests, benchmarks, and runtime-verified behavior."
---

# golang-pro

Use this skill when the task is centered on Go code, Go modules, services, CLIs, or concurrency behavior.

## Use It For

- Go application, service, library, or CLI implementation
- goroutine, channel, context, and cancellation issues
- `go.mod`, module, build, test, and benchmark workflows
- HTTP handlers, middleware, and data access code
- race, performance, and memory behavior analysis

## Do Not Use It For

- generic backend architecture with no Go-specific concern
- adding concurrency before proving it is needed
- claiming correctness without running `go test`, targeted checks, or direct requests when possible

## First Pass

1. Read `go.mod`, package layout, target package, callers, tests, and build/test scripts.
2. Identify public API, context/cancellation behavior, error contracts, and concurrency boundaries.
3. Check whether race detection, benchmarks, or integration tests matter for the task.
4. Run targeted `go test`, build, benchmark, race, or request checks when possible.

## Workflow

### 1. Map Go Contract

- package and exported API boundary
- error wrapping and sentinel behavior
- context propagation and cancellation
- goroutine ownership and cleanup
- module and dependency constraints

### 2. Implement Carefully

- keep code idiomatic and simple before adding abstractions
- avoid goroutine leaks and shared mutable state
- preserve existing API and wire formats unless migration is explicit
- update tests and examples when behavior changes

### 3. Verification

- run `go test`, `go test -race`, `go test -bench`, `go vet`, build, or direct runtime checks when available
- state clearly when race, benchmark, or integration behavior was not verified

## Output Style

Return:

- Go package or runtime issue
- code/API change
- exact verification performed
- remaining race, benchmark, or integration checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/golang-pro.md`

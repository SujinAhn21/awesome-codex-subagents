---
name: "cli-developer"
description: "CLI-development Codex skill for command design, argument parsing, terminal UX, exit codes, distribution, and direct CLI behavior verification."
---

# cli-developer

Use this skill when the task is to design, implement, debug, or document command-line tools.

## Use It For

- CLI command and subcommand design
- argument, flag, config, and environment handling
- terminal output, prompts, progress, and error messages
- shell completion and distribution strategy
- CLI tests and behavior verification

## Do Not Use It For

- documenting CLI flags without checking real parser or help output
- changing command behavior without considering scripts and existing users
- TUI or GUI work where command-line behavior is not central

## First Pass

1. Read the CLI entry point, parser configuration, command handlers, tests, and docs.
2. Run `--help`, version, and the reported command path when possible.
3. Identify exit codes, stdout/stderr contract, config precedence, and platform assumptions.
4. Separate CLI UX issues from backend/API failures invoked by the CLI.

## Workflow

### 1. Map The Command Contract

- command and subcommand names
- positional arguments and flags
- defaults, aliases, and environment variables
- exit codes and error output
- interactive versus non-interactive behavior

### 2. Implement Carefully

- keep help text and docs aligned with parser behavior
- preserve scriptability and stable output when users may parse it
- make errors actionable without hiding debug detail
- avoid network or filesystem side effects in dry-run/help paths

### 3. Verification

- run help output, representative commands, error cases, and tests when available
- state clearly when cross-platform behavior was not verified

## Output Style

Return:

- CLI behavior changed or diagnosed
- command examples tested
- exit code/output implications
- unverified platform or shell checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/cli-developer.md`

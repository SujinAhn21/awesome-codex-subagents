---
name: "agent-organizer"
description: "Codex orchestration planning skill for selecting specialist skills, decomposing work, sequencing verification, and avoiding fictional agent handoffs."
---

# agent-organizer

Use this skill when the task requires choosing the right specialist skills, sequencing multi-step work, or coordinating a complex repo task without relying on imaginary agent protocols.

## Use It For

- mapping a complex request to available Codex skills/plugins
- decomposing work into safe, verifiable phases
- identifying which files, commands, and checks each phase needs
- coordinating parallelizable reads or validations
- documenting handoff state for later resume

## Do Not Use It For

- pretending to call unavailable peer agents or context managers
- adding orchestration overhead to a simple single-skill task
- making autonomous product decisions where the user must choose among risky options

## First Pass

1. Read the user request, relevant repo docs, available skill/plugin list, and current worktree state.
2. Identify required capabilities, dependencies, irreversible actions, and verification gates.
3. Choose the minimum set of skills needed instead of invoking broad teams by default.
4. Plan concrete reads, edits, commands, and stopping conditions before execution.

## Workflow

### 1. Decompose Work

- goal and non-goals
- affected files, systems, and plugins
- dependencies and ordering constraints
- safe parallel work
- verification evidence required before claiming completion

### 2. Coordinate Execution

- use specialist skills only when their guidance materially improves the task
- keep root and generated/plugin copies synchronized when both are source of truth
- surface blockers quickly when local evidence cannot answer the question
- leave resumable notes for long-running work

### 3. Verify And Report

- confirm each phase with commands, tests, diffs, or direct checks
- separate completed, partially verified, and unverified work
- report exact paths, counts, versions, and remaining scope

## Output Style

Return:

- selected workflow and why
- execution phases
- verification gates
- current status and resume point
- decisions that still require the user

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/agent-organizer.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

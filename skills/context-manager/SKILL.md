---
name: "context-manager"
description: "Codex context management skill for gathering task evidence, organizing repo state, preserving decisions, and leaving resumable handoff notes without fictional agent protocols."
---

# context-manager

Use this skill when a task has enough files, decisions, state, or interruptions that context needs to be deliberately gathered, structured, and preserved.

## Use It For

- gathering relevant repo, command, and decision context before work
- keeping long-running tasks resumable
- separating facts, assumptions, and unknowns
- summarizing current state without losing verification caveats
- preparing handoff notes for later sessions

## Do Not Use It For

- pretending there is a separate context-manager service to query
- adding process overhead to a small one-step task
- treating memory or previous conversation as stronger evidence than current files and command output

## First Pass

1. Read the user request, current working directory, relevant docs, current worktree state, and any known progress notes.
2. Identify authoritative evidence: files, manifests, command output, tests, logs, installed plugin state, or runtime checks.
3. Record open questions only when they block safe progress; otherwise make explicit assumptions and keep moving.
4. Preserve enough path, command, and result detail that another Codex session can resume without guessing.

## Workflow

### 1. Gather Context

- objective and non-goals
- relevant files and directories
- current modified state
- prior verification evidence
- constraints, permissions, and risky actions

### 2. Organize State

- separate completed, in-progress, and pending work
- track exact counts, versions, paths, and commands
- distinguish facts from inferences
- keep verification status attached to each claim
- avoid carrying stale assumptions forward

### 3. Preserve Handoff

- write or update progress notes when useful
- include next concrete step, not just broad intent
- list commands already run and their results
- call out unverified areas plainly

## Output Style

Return:

- current objective
- authoritative state
- completed and pending items
- verification evidence
- exact resume point

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/context-manager.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

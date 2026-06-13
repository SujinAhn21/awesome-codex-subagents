---
name: "task-distributor"
description: "Task distribution Codex skill for decomposing work, queueing tasks, sequencing dependencies, load balancing available capabilities, and preserving verification gates."
---

# task-distributor

Use this skill when a large task needs practical work breakdown, dependency ordering, and verification-aware sequencing.

## Use It For

- Breaking large work into small, ordered, verifiable tasks.
- Identifying dependencies, parallel-safe reads/checks, and serialization points for writes.
- Balancing work across available local skills, tools, scripts, and repo conventions.
- Creating continuation notes that preserve paths, counts, verification status, and next actions.
- Avoiding overload by batching repetitive work with consistent checks.

## Do Not Use It For

- Inventing unavailable workers, hidden queues, or external automation.
- Replacing actual implementation and verification with a task list.
- Splitting simple tasks where direct execution is clearer.
- Running risky or destructive actions without approval.

## First Pass

1. Read the user request, repo instructions, current worktree state, available skills/plugins, and relevant progress docs.
2. Identify deliverables, dependencies, repeated patterns, risk points, and verification commands.
3. Separate tasks that can run in parallel from tasks that must be sequential.
4. Define batch size based on verification cost and rollback risk.
5. Keep enough state for a fresh session to continue from disk and command evidence.

## Workflow

1. Convert the goal into concrete batches with a completion check for each batch.
2. Do independent reads and checks in parallel where safe.
3. Avoid parallel writes to the same file or same generated artifact.
4. After each batch, verify before expanding scope.
5. Record counts and remaining work from filesystem or command output, not memory.
6. If blocked, state the blocker and the exact missing input or permission.

## Verification

- Prefer command output, file comparisons, tests, builds, plugin discovery, and explicit counts.
- Do not call a batch complete until its verification checks have run.
- If only planning was done, say implementation and verification have not happened.
- Reconfirm remaining work from disk before reporting progress.

## Output Style

- For Korean users, keep progress updates natural and concrete: what batch, what changed, what was verified, what remains.
- Avoid project-management filler and abstract orchestration terms.
- Use exact paths, counts, and commands when they matter.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/task-distributor.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `haiku`
- MCP required upstream: `no`

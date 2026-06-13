---
name: "multi-agent-coordinator"
description: "Coordination Codex skill for decomposing complex work across available skills, sequencing tasks, preserving verification gates, and avoiding fictional agent handoffs."
---

# multi-agent-coordinator

Use this skill when a task spans multiple domains and needs explicit sequencing, handoff notes, and verification gates across available Codex capabilities.

## Use It For

- Decomposing complex work into ordered, parallelizable, and verifiable chunks.
- Selecting relevant available skills or plugins without pretending unavailable tools exist.
- Coordinating implementation, review, testing, documentation, and release checks.
- Preserving constraints, assumptions, open questions, and evidence across long work sessions.
- Creating concise continuation notes when work must resume later.

## Do Not Use It For

- Simple single-file or single-domain tasks where direct execution is faster.
- Inventing peer agents, hidden state channels, external workers, or unavailable runtime features.
- Bypassing user approval for risky, destructive, credentialed, or externally visible actions.
- Replacing actual verification with a coordination plan.

## First Pass

1. Read the user request, current repo instructions, available skill/plugin list, worktree state, and relevant docs.
2. Identify required domains, dependencies, blockers, verification gates, and whether any work can safely run in parallel.
3. Separate actions that can be done autonomously from actions that need approval or user input.
4. Define a short plan only when it reduces risk or clarifies sequencing.
5. Keep enough notes that another fresh Codex session can resume from disk state and verified facts.

## Workflow

1. Break the task into concrete deliverables with clear completion evidence.
2. Use available skills only when their body has been read and they fit the current work.
3. Parallelize safe reads and independent checks, but avoid parallel writes to the same files.
4. After each implementation slice, verify before moving to the next slice when verification is available.
5. Track what was changed, what was checked, and what remains unverified.
6. If the work spans sessions, leave a concise progress artifact or final note with exact paths, counts, and next candidates.

## Verification

- Treat tests, builds, lint, typecheck, CLI output, `curl`, logs, and direct discovery checks as stronger evidence than plans.
- Do not report a coordinated workflow as complete until each required deliverable has its relevant check or an explicit unverified caveat.
- If a proposed subtask depends on unavailable tools, state that limitation and use the closest verifiable local path.
- Reconfirm counts and file lists from the filesystem before reporting progress on batch work.

## Output Style

- For Korean users, keep updates natural and operational: what changed, what was verified, what is next.
- Avoid management jargon, vague orchestration language, and inflated completion claims.
- Prefer compact continuation notes with exact commands, paths, and counts.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/multi-agent-coordinator.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `opus`
- MCP required upstream: `no`

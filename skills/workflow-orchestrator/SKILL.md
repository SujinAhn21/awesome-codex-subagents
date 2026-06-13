---
name: "workflow-orchestrator"
description: "Workflow orchestration Codex skill for state machines, process flows, retries, compensation, idempotency, audit trails, monitoring, and verified workflow behavior."
---

# workflow-orchestrator

Use this skill for business or system workflows where state transitions, retries, compensation, and auditability must be explicit.

## Use It For

- Designing or reviewing workflow state machines, process flows, approvals, and asynchronous orchestration.
- Retry, timeout, dead-letter, compensation, saga, idempotency, and rollback behavior.
- Workflow engines, queues, event orchestration, job pipelines, and human-in-the-loop steps.
- Debugging stuck workflows, duplicate execution, inconsistent state, and missing audit events.
- Documenting workflow states, transitions, invariants, and verification checks.

## Do Not Use It For

- Replacing implementation with a process diagram.
- Claiming a workflow is reliable without exercising transitions, retries, failure paths, or logs.
- Hiding state changes, side effects, or compensation gaps.
- Inventing external orchestrators or workers that are not available in the current system.

## First Pass

1. Read workflow definitions, queue/job code, state models, database schema, event contracts, logs, runbooks, and tests.
2. Identify states, transitions, triggers, side effects, idempotency keys, failure modes, and audit requirements.
3. Check whether retries, timeouts, deduplication, compensation, and manual intervention are implemented.
4. Find the smallest verification path: unit test, integration test, fixture replay, local worker run, log inspection, or API check.
5. If workflow engine behavior or queue semantics may have changed, verify from official/current docs.

## Workflow

1. Model the happy path and each failure path before editing.
2. Make state transitions explicit and reject invalid transitions.
3. Keep side effects idempotent or guarded by durable keys.
4. Add compensation or manual recovery for irreversible actions.
5. Preserve audit logs and observability for each important transition.
6. Verify the changed transition or failure path directly.

## Verification

- Prefer tests, replay logs, worker output, queue inspection, database state checks, and direct API calls.
- Report exact workflow path, state transition, command, and result.
- Do not call a workflow fixed unless the failing transition or retry path was checked.
- If only code was inspected, say workflow behavior remains unverified.

## Output Style

- For Korean users, explain workflow state naturally while preserving state names, event names, queue names, IDs, commands, and error text exactly.
- Lead with the affected transition, failure mode, change, and verification status.
- Avoid abstract orchestration language when concrete states and side effects are available.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/workflow-orchestrator.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `opus`
- MCP required upstream: `no`

---
name: "error-coordinator"
description: "Error coordination Codex skill for cross-service failure handling, cascade prevention, recovery plans, error budgets, runbooks, and evidence-based resilience actions."
---

# error-coordinator

Use this skill when errors span multiple components or require coordinated recovery, prevention, and communication.

## Use It For

- cross-service error handling and recovery planning
- cascade prevention with timeouts, retries, circuit breakers, and bulkheads
- incident runbook, rollback, and fallback design
- error budget, alert, and recovery workflow review
- coordinating remediation across services without fictional agent handoffs

## Do Not Use It For

- replacing root-cause investigation when the error source is still unknown
- adding retries or fallbacks without understanding idempotency and blast radius
- claiming recovery works without logs, tests, drills, or production evidence

## First Pass

1. Read service topology, logs, traces, alerts, recent deploys, incident notes, runbooks, retry policies, and dependency contracts.
2. Identify affected services, user impact, error propagation path, recovery owner, and current safeguards.
3. Check timeouts, retry budgets, queue behavior, idempotency, circuit breakers, fallback paths, and rollback options.
4. Verify with tests, logs, staging drills, alert history, or controlled recovery checks when available.

## Workflow

### 1. Map Failure Coordination

- impacted services and dependencies
- error propagation and cascade risk
- current detection and escalation path
- recovery and rollback owners
- user-visible degradation strategy

### 2. Design Recovery

- prioritize stopping cascade before optimizing root fix
- keep retries bounded and idempotent
- define fallback and degraded-mode behavior
- make alerts actionable and tied to runbooks
- capture follow-up checks for resilience gaps

### 3. Verify

- run targeted tests, staging drills, or log/trace validation
- confirm recovery criteria and post-recovery health checks
- state when live failover, production recovery, or full drill was not performed

## Output Style

Return:

- failure coordination summary
- cascade and recovery risks
- proposed or implemented controls
- verification evidence
- remaining drill or production checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/error-coordinator.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

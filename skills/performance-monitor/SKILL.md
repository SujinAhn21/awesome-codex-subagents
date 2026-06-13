---
name: "performance-monitor"
description: "Performance monitoring Codex skill for observability, metrics, traces, logs, baselines, alerting, dashboards, anomaly triage, and evidence-backed performance reports."
---

# performance-monitor

Use this skill for observability and performance monitoring work where baselines, metrics, logs, traces, and alert behavior must be checked before making claims.

## Use It For

- Metrics, logs, traces, dashboards, alert rules, SLO/SLA indicators, and runbook review.
- Establishing baselines for latency, throughput, error rate, saturation, cost, and resource use.
- Investigating performance regressions, bottlenecks, anomalies, and noisy alerts.
- Reviewing instrumentation, sampling, cardinality, retention, and dashboard usefulness.
- Turning monitoring data into practical operational recommendations.

## Do Not Use It For

- Claiming performance improved without before/after measurements.
- Treating one local run as production performance evidence.
- Adding high-cardinality or sensitive metrics without reviewing cost, privacy, and retention.
- Replacing profiling, load testing, or logs with dashboard screenshots alone.

## First Pass

1. Read service docs, telemetry config, instrumentation code, dashboard definitions, alert rules, runbooks, and recent incident notes.
2. Identify the user-visible symptom, affected service, time window, deployment version, traffic pattern, and relevant SLO.
3. Check available evidence: logs, traces, metrics queries, profiler output, load-test output, CI performance tests, or cloud monitoring data.
4. Separate baseline behavior from regression, anomaly, or expected traffic change.
5. If monitoring platform behavior, query syntax, or service limits may have changed, verify from official/current docs.

## Workflow

1. Map the request path and telemetry coverage from entrypoint through dependencies.
2. Define the metric or trace evidence needed before changing code or alert rules.
3. Reduce noise by checking labels, cardinality, sampling, aggregation windows, and alert thresholds.
4. Tie recommendations to observed bottlenecks, not generic tuning advice.
5. Preserve existing dashboard and alert conventions unless there is a clear defect.
6. Document exactly what was measured and what remains blind.

## Verification

- Prefer direct metric queries, trace samples, logs, load-test output, profiler output, and alert evaluation output.
- Report the time window, environment, query or command, and before/after numbers.
- Do not call a performance change verified without measured evidence on the relevant path.
- If production data is inaccessible, state what local or staging evidence was checked and what production check remains.

## Output Style

- For Korean users, explain performance findings in natural Korean while preserving metric names, query names, units, timestamps, commands, and service identifiers exactly.
- Lead with observed evidence, likely bottleneck, action taken, and remaining blind spots.
- Avoid vague “optimized” or “stable” claims without numbers.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/09-meta-orchestration/performance-monitor.md`
- Upstream category: `Meta Orchestration`
- Upstream model hint: `haiku`
- MCP required upstream: `no`

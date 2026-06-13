---
name: "cohort-analysis"
description: "Cohort analysis Codex skill for retention, activation, segment behavior, cohort tables, data validation, and product recommendations from time-based user data."
---

# cohort-analysis

Use this skill when the task is to analyze how user groups behave over time.

## Use It For

- retention, activation, and engagement cohort analysis
- acquisition, behavioral, and segment cohort comparisons
- cohort SQL/notebook review
- retention curve diagnosis and drop-off analysis
- product recommendations grounded in cohort evidence

## Do Not Use It For

- claiming retention improved without validated cohort data
- mixing cohort definitions or time windows without calling it out
- using post-hoc segment stories as proof without caveats

## First Pass

1. Read the metric definition, event schema, cohort assignment logic, date range, timezone, filters, and existing query or notebook.
2. Identify cohort type, retention definition, denominator, activity event, and observation window.
3. Check for missing data, backfills, bot/test users, survivorship bias, and incomplete recent cohorts.
4. Verify calculations with SQL, notebook output, sample rows, or reproducible formulas when available.

## Workflow

### 1. Define Cohort Contract

- cohort start event and start date
- retained/active event definition
- exact time buckets and timezone
- denominator and inclusion rules
- segment dimensions and exclusion rules

### 2. Analyze Behavior

- build or verify cohort retention table
- identify biggest drop-off periods
- compare cohorts across releases, channels, plans, or behaviors
- distinguish correlation from causal activation claims
- flag incomplete or biased cohorts

### 3. Recommend Action

- tie recommendations to specific cohort evidence
- state what data would confirm activation hypotheses
- suggest product or research follow-up only where evidence supports it

## Output Style

Return:

- cohort definition
- retention/engagement findings
- data quality caveats
- recommended action
- queries or verification performed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/10-research-analysis/cohort-analysis.md`
- Upstream category: `Research Analysis`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

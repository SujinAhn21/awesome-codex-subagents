---
name: "ab-test-analysis"
description: "A/B test analysis Codex skill for experiment validity, lift, confidence intervals, p-values, guardrails, and ship/no-ship recommendations."
---

# ab-test-analysis

Use this skill when the task is to interpret experiment results or make an evidence-based product decision from A/B test data.

## Use It For

- A/B test result interpretation
- p-values, confidence intervals, lift, power, and effect size review
- sample ratio mismatch and early-stopping checks
- guardrail metric analysis
- ship, no-ship, iterate, or extend recommendations

## Do Not Use It For

- designing an experiment when there are no results yet
- treating statistical significance as business significance
- claiming a test is valid without checking assignment, sample size, duration, and guardrails

## First Pass

1. Read the experiment brief, hypothesis, primary metric, guardrails, assignment logic, sample sizes, dates, and analysis query or notebook.
2. Confirm whether the test was pre-planned, ran for the intended duration, and avoided peeking or post-hoc metric switching.
3. Calculate or verify control/treatment rates, lift, confidence interval, p-value, and practical effect size.
4. Check sample ratio mismatch, segment imbalance, guardrail regressions, and missing-data assumptions before recommending action.

## Workflow

### 1. Validate Experiment

- primary metric and minimum detectable effect
- randomization and assignment unit
- sample sizes and exposure counts
- test duration and stopping rule
- guardrail and segmentation plan

### 2. Analyze Result

- report absolute and relative lift
- include confidence interval and p-value
- separate statistical significance from practical significance
- call out underpowered or invalid tests directly
- avoid post-hoc segment claims unless clearly labeled exploratory

### 3. Recommend Action

- ship only when primary metric, effect size, and guardrails support it
- no-ship when the primary metric or guardrails show meaningful harm
- extend when the result is underpowered but still decision-relevant
- iterate when the evidence suggests product direction but not launch readiness

## Output Style

Return:

- experiment validity status
- result summary with effect size and uncertainty
- guardrail status
- ship/no-ship/iterate recommendation
- caveats and missing checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/10-research-analysis/ab-test-analysis.md`
- Upstream category: `Research Analysis`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

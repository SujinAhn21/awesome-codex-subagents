---
name: "growth-loops"
description: "Growth-loop Codex skill for designing, diagnosing, and measuring compounding product-led, viral, content, sales, or paid acquisition loops."
---

# growth-loops

Use this skill when the task is to design or improve a repeatable growth mechanism rather than a one-time campaign.

## Use It For

- growth loop design
- PLG, viral, content, network, or paid loop analysis
- acquisition constraint diagnosis
- loop metric and experiment planning
- turning product usage into repeatable distribution

## Do Not Use It For

- generic marketing advice with no loop mechanics
- claiming viral or PLG potential without user behavior evidence
- replacing product strategy, positioning, or retention work

## First Pass

1. Read product docs, current funnel metrics, acquisition channels, user behavior notes, and growth experiments when available.
2. Identify the user action, product value, output, new-user touchpoint, and activation path.
3. Separate observed loop behavior from desired loop behavior.
4. Check whether each loop step has a measurable metric.

## Workflow

### 1. Map The Loop

- starting user segment
- core action and value moment
- output or invitation surface
- new-user touchpoint
- activation path back into the loop

### 2. Diagnose Constraints

- identify the weakest conversion or cycle-time step
- distinguish acquisition, activation, retention, and sharing problems
- propose small experiments before broad growth programs
- avoid recommending paid scale before unit economics are known

### 3. Verification

- tie loop claims to analytics, user research, channel data, or experiment results
- state clearly when the loop is hypothetical and needs validation

## Output Style

Return:

- loop type and diagram
- metric for each step
- weakest constraint
- top experiments and validation plan

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/08-business-product/growth-loops.md`

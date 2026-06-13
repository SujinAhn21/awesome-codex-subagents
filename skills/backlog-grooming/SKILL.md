---
name: "backlog-grooming"
description: "Backlog-refinement Codex skill for cleaning, splitting, prioritizing, and making product backlog items sprint-ready."
---

# backlog-grooming

Use this skill when the task is to refine a product backlog into clear, prioritized, buildable work.

## Use It For

- backlog cleanup and hygiene review
- story splitting and acceptance-criteria improvement
- readiness assessment for sprint planning
- duplicate, stale, or blocked item triage
- refinement agenda preparation

## Do Not Use It For

- making product priority decisions without product context
- estimating work without team input or implementation context
- turning vague ideas into commitments before scope and acceptance criteria are clear

## First Pass

1. Read the actual backlog items, roadmap context, sprint goal, team capacity notes, and prior refinement decisions.
2. Identify item status, owner, priority, dependencies, acceptance criteria, and age.
3. Separate ready work from items that need discovery, design, technical review, or product decisions.
4. Preserve rejected or archived decisions with reasons when available.

## Workflow

### 1. Assess Hygiene

- stale or duplicated items
- unclear owner or priority
- missing acceptance criteria
- oversized stories
- unresolved dependencies or questions

### 2. Refine

- split large stories into independently valuable increments
- make acceptance criteria specific and testable
- mark blockers and required decisions explicitly
- keep near-term items detailed and later items directional

### 3. Verification

- check refined items against the team's definition of ready when available
- state clearly where estimates, priorities, or scope require team or product-owner confirmation

## Output Style

Return:

- backlog health summary
- sprint-ready items
- items needing more work
- archive, split, or priority recommendations

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/08-business-product/backlog-grooming.md`

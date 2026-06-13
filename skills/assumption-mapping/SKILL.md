---
name: "assumption-mapping"
description: "Product assumption mapping Codex skill for surfacing value, usability, viability, and feasibility risks before committing build effort."
---

# assumption-mapping

Use this skill when the task is to identify, prioritize, and test risky assumptions behind a product idea, feature, strategy, or roadmap decision.

## Use It For

- product idea and feature risk mapping
- value, usability, business viability, and feasibility assumptions
- de-risking plans before engineering investment
- validation experiment design
- decision rules for continue, pivot, pause, or build

## Do Not Use It For

- treating brainstorming as validation
- recommending implementation before the riskiest assumptions are named
- inventing customer evidence that has not been collected

## First Pass

1. Read the product idea, target user, business goal, constraints, existing research, metrics, and any proposed implementation plan.
2. Extract what must be true for the idea to work across value, usability, viability, and feasibility.
3. Score each assumption by importance and current evidence strength.
4. Propose the cheapest credible test for the highest-importance, weakest-evidence assumptions.

## Workflow

### 1. Extract Assumptions

- customer problem and willingness to act
- usability and workflow fit
- revenue, cost, distribution, and operational viability
- technical feasibility, data availability, compliance, and timeline
- dependencies on partners, platforms, or behavior change

### 2. Prioritize Risk

- rank by importance to success
- rank by evidence strength
- separate known facts from beliefs and guesses
- identify the top assumptions that would kill or reshape the idea

### 3. Design Tests

- use the smallest test that can change the decision
- define success and failure thresholds in advance
- prefer direct customer or system evidence over opinions
- specify what to do if the assumption is validated or invalidated

## Output Style

Return:

- assumption map
- top risks to test first
- experiment plan
- decision rules
- evidence gaps

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/08-business-product/assumption-mapping.md`
- Upstream category: `Business Product`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

---
name: "first-principles-thinking"
description: "First-principles reasoning Codex skill for breaking down problems, separating facts from assumptions, challenging inherited constraints, and rebuilding solution options."
---

# first-principles-thinking

Use this skill when the task is to rethink a problem from fundamentals rather than copy an existing pattern.

## Use It For

- challenging assumptions in product, technical, or business decisions
- reframing vague solution requests into precise problems
- separating facts, constraints, assumptions, and preferences
- generating alternatives from fundamental requirements
- deciding what small test would validate a rebuilt approach

## Do Not Use It For

- replacing evidence gathering with abstract reasoning
- ignoring user constraints that are real and non-negotiable
- overcomplicating a straightforward implementation task

## First Pass

1. Restate the actual problem without embedding the proposed solution.
2. List facts that are directly evidenced, assumptions that need proof, and constraints that appear non-negotiable.
3. Challenge inherited process, technology, business, and user assumptions.
4. Rebuild 2-3 solution directions and define the smallest evidence-gathering step for each.

## Workflow

### 1. Decompose

- problem statement
- affected user/system/business outcome
- current approach and hidden assumptions
- hard constraints versus preferences
- missing evidence

### 2. Rebuild

- start from validated facts
- remove inherited constraints where possible
- generate multiple solution directions
- compare impact, effort, risk, and reversibility
- avoid pretending uncertain assumptions are facts

### 3. Test

- define the smallest test that changes the decision
- state success and failure criteria
- identify owner, artifact, or command needed for validation

## Output Style

Return:

- reframed problem
- facts, assumptions, and constraints
- challenged assumptions
- rebuilt options with tradeoffs
- next validation step

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/10-research-analysis/first-principles-thinking.md`
- Upstream category: `Research Analysis`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

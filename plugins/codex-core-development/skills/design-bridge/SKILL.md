---
name: "design-bridge"
description: "Design translation Codex skill for turning design docs and reference UIs into implementation-ready instructions."
---

# design-bridge

Use this skill when the input is a design document, reference product, or visual brief that needs to be translated into concrete implementation guidance.

## Use It For

- turning design docs into actionable UI instructions
- extracting layout, typography, color, and component rules
- aligning implementation with a referenced visual system
- preparing handoff notes for UI or frontend work

## Do Not Use It For

- direct backend implementation
- generic brainstorming with no design source
- pixel-level verification when no visual reference exists

## First Pass

1. Read the design source completely before summarizing it.
2. Separate factual tokens from interpretation:
   - colors
   - typography
   - spacing
   - components
   - responsive rules
3. Compare the design source against the actual repo UI when code already exists.
4. Call out what is explicit in the design and what still requires judgment.

## Workflow

### 1. Extract

- visual tone and density
- color roles, not just color values
- typography hierarchy
- component patterns and states
- layout rules and spacing rhythm
- responsive behavior

### 2. Translate

- convert design language into developer-ready instructions
- prefer file-targeted implementation notes over vague aesthetic language
- preserve the source style instead of averaging it into generic UI advice

### 3. Verify

- make sure translated guidance does not contradict the actual design source
- if implementation exists, compare key patterns against the current code
- if runtime visual validation is unavailable, state that clearly

## Output Style

Return:

- source summary
- extracted design rules
- implementation guidance
- gaps or ambiguities that still need human choice

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/design-bridge.md`

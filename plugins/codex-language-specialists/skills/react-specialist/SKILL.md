---
name: "react-specialist"
description: "React Codex skill for component architecture, state, effects, performance, accessibility, and behavior verified through real app paths."
---

# react-specialist

Use this skill when the task is centered on React components, hooks, state, rendering behavior, or React app architecture.

## Use It For

- React component implementation and refactoring
- hook, effect, and state-flow debugging
- client performance and render behavior
- accessibility and interaction review
- React test and story coverage planning

## Do Not Use It For

- generic JavaScript or CSS work with no React-specific concern
- adding memoization before measuring or understanding render cost
- claiming UI behavior without browser, test, story, or app-path verification

## First Pass

1. Read the component, parent/child callers, state source, hooks, tests, stories, and route/page usage.
2. Identify controlled/uncontrolled state, server/client boundaries, and side effects.
3. Check existing design-system and accessibility patterns before introducing new UI patterns.
4. Run relevant tests, story, build, or browser path when possible.

## Workflow

### 1. Map UI Behavior

- props and state ownership
- data fetching and mutation path
- effect dependencies and cleanup
- loading, empty, error, and disabled states
- keyboard and screen-reader interactions

### 2. Implement Carefully

- preserve established component patterns
- avoid unnecessary `useMemo`/`useCallback` unless justified by existing guidance or measurement
- keep accessibility and user feedback states explicit
- update tests or stories when behavior changes

### 3. Verification

- run component tests, app tests, build, typecheck, story checks, or manual browser checks when available
- state clearly when UI interaction was not directly verified

## Output Style

Return:

- React behavior or architecture issue
- component/state changes
- verification performed
- remaining browser or accessibility checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/react-specialist.md`

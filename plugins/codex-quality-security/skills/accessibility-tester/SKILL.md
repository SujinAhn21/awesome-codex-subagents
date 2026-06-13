---
name: "accessibility-tester"
description: "Accessibility testing Codex skill for WCAG review, keyboard support, screen reader behavior, contrast, semantic HTML, and verified remediation."
---

# accessibility-tester

Use this skill when the task is to assess or fix accessibility issues in a UI, document, app, or component library.

## Use It For

- WCAG-oriented accessibility review
- keyboard navigation, focus order, and focus trapping checks
- screen reader label, landmark, and announcement behavior
- color contrast, zoom, motion, and touch target review
- accessibility regression tests and remediation plans

## Do Not Use It For

- purely visual design critique with no accessibility concern
- claiming screen reader compatibility without testing or clearly stating it was not tested
- adding ARIA before checking whether semantic HTML solves the issue

## First Pass

1. Read the affected UI code, routes, components, forms, design notes, and existing accessibility tests or reports.
2. Identify user flows, interactive controls, content hierarchy, keyboard path, error states, and responsive/mobile behavior.
3. Run available automated checks such as axe, Playwright accessibility checks, Storybook addon checks, lint rules, or project-specific tests.
4. Manually inspect keyboard behavior and state which assistive technology checks were or were not performed.

## Workflow

### 1. Map Accessibility Surface

- page/component role and user task
- semantic structure and heading order
- control labels, descriptions, and errors
- focus management and keyboard path
- contrast, motion, zoom, and responsive constraints

### 2. Remediate

- prefer semantic HTML over ARIA
- keep visible labels and programmatic names aligned
- make errors, loading states, and dynamic updates perceivable
- preserve design intent while meeting accessibility requirements
- add regression tests where the project supports them

### 3. Verification

- run automated accessibility checks when available
- test keyboard-only operation for affected flows
- verify contrast and focus visibility
- state whether NVDA, VoiceOver, JAWS, Narrator, mobile screen reader, or browser checks were not run

## Output Style

Return:

- accessibility issue and affected users
- evidence from checks performed
- remediation change
- remaining manual or assistive-technology verification

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/accessibility-tester.md`
- Upstream category: `Quality Security`
- Upstream model hint: `haiku`
- MCP required upstream: `no`

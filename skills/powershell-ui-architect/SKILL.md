---
name: "powershell-ui-architect"
description: "PowerShell UI Codex skill for WinForms, WPF, Metro-style dashboards, and terminal UIs that keep automation logic separate from UI code."
---

# powershell-ui-architect

Use this skill when a PowerShell automation tool needs a GUI or terminal UI layer.

## Use It For

- WinForms or WPF PowerShell front ends
- Metro-style dashboards using WPF frameworks
- terminal menus and TUI workflows
- UI/business-logic separation for automation tools
- responsive progress, cancellation, and error UX

## Do Not Use It For

- core infrastructure automation with no UI concern
- embedding large UI definitions inside unstructured scripts
- claiming UI behavior without manual or automated interaction checks

## First Pass

1. Read UI scripts, XAML/forms, core automation modules, event handlers, and user workflows.
2. Identify target runtime: Windows PowerShell 5.1, `pwsh`, desktop Windows, remote shell, or server console.
3. Map long-running operations, validation, cancellation, and failure handling.
4. Separate UI orchestration from privileged or state-changing automation logic.

## Workflow

### 1. Choose UI Layer

- TUI for remote/server workflows
- WinForms for quick Windows-only utilities
- WPF for richer desktop tools and maintainable layout
- Metro-style WPF only when dashboard UX is justified

### 2. Structure Safely

- keep core automation in modules
- keep UI code thin and event handlers small
- avoid freezing UI threads during long-running work
- provide clear cancel, confirm, and error paths for state changes

### 3. Verification

- run available script checks, UI smoke paths, or manual interaction checks when possible
- state clearly when GUI interaction was not directly tested

## Output Style

Return:

- UI scenario and chosen approach
- separation-of-concerns changes
- interaction checks performed
- manual UI checks still needed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/06-developer-experience/powershell-ui-architect.md`

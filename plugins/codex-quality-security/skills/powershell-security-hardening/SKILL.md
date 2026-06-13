---
name: "powershell-security-hardening"
description: "PowerShell security-hardening Codex skill for remoting, logging, credentials, least privilege, script safety, and Windows automation baselines."
---

# powershell-security-hardening

Use this skill when PowerShell automation, remoting, credentials, or Windows endpoint configuration needs security review or hardening.

## Use It For

- PowerShell remoting and JEA hardening
- transcript, module, and script-block logging review
- credential and secret handling
- least-privilege automation design
- secure scheduled tasks, WinRM, and script publishing

## Do Not Use It For

- claiming compliance without checking actual settings
- weakening execution, logging, or remoting controls for convenience
- changing production security baselines without rollback and approval path

## First Pass

1. Read scripts, modules, remoting config, scheduled tasks, credential flows, logging policy, and relevant GPO/baseline docs.
2. Identify state-changing commands, secrets, privilege boundaries, and audit requirements.
3. Check whether controls can be inspected with read-only commands before recommending changes.
4. Separate script-level issues from Windows, AD, endpoint, and compliance policy issues.

## Workflow

### 1. Assess Controls

- remoting and endpoint exposure
- credential storage and secret flow
- execution policy, signing, and script publishing
- logging, transcript, and audit evidence
- least-privilege and service account boundaries

### 2. Harden Safely

- prefer read-only audit before remediation
- protect secrets in output, logs, and errors
- make changes reversible and documented
- coordinate with AD, endpoint, or compliance owners where needed

### 3. Verification

- run read-only configuration checks, policy inspection, script analysis, or test hardening commands when available
- state clearly when domain, GPO, endpoint, or compliance validation was not run

## Output Style

Return:

- security issue or control gap
- hardening recommendation
- evidence or commands checked
- residual risk and approval needs

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/powershell-security-hardening.md`

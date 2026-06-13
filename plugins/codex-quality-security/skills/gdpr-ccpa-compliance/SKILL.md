---
name: "gdpr-ccpa-compliance"
description: "GDPR/CCPA privacy compliance Codex skill for data inventory, consent, rights requests, retention, privacy notices, processor contracts, and evidence-based gap review."
---

# gdpr-ccpa-compliance

Use this skill when the task involves GDPR, CCPA/CPRA, privacy compliance, consent, deletion, access requests, or personal data handling.

## Use It For

- GDPR and CCPA/CPRA product or engineering gap review
- data inventory, purpose, retention, consent, and legal basis mapping
- data subject/consumer rights implementation planning
- privacy notice, cookie, opt-out, deletion, and portability workflow review
- processor/vendor, breach, audit, and evidence readiness checks

## Do Not Use It For

- formal legal advice or certification
- claiming compliance without evidence from product flows, policies, logs, contracts, or controls
- ignoring jurisdiction, data type, processor/controller role, or business applicability thresholds

## First Pass

1. Read product flows, data inventory, privacy notice, consent screens, cookie behavior, DSR/consumer request process, retention rules, vendor list, and relevant policies.
2. Identify jurisdiction, data subjects/consumers, personal/sensitive data, processing purposes, legal basis, sale/share status, and processor/controller roles.
3. Map requirements to implementation evidence and mark missing evidence separately from true non-compliance.
4. State when legal counsel, DPO, privacy officer, or certified auditor review is required.

## Workflow

### 1. Scope Privacy Obligations

- GDPR, CCPA/CPRA, or both
- affected users and geography
- data categories and sensitive data
- processing purpose, legal basis, and retention
- vendor, processor, sale/share, and cross-border transfer status

### 2. Assess Gaps

- consent and opt-out flows
- access, deletion, correction, portability, objection, and restriction workflows
- privacy notice and disclosure accuracy
- retention and deletion enforcement
- evidence quality and control ownership

### 3. Recommend Remediation

- prioritize by user rights, enforcement risk, and implementation effort
- specify product, engineering, policy, and vendor-contract changes separately
- include evidence needed to close each gap
- avoid legal conclusions where facts or counsel review are missing

## Output Style

Return:

- scope and applicability assumptions
- data/privacy gaps with evidence status
- prioritized remediation
- legal/counsel review items
- unverified controls

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/gdpr-ccpa-compliance.md`
- Upstream category: `Quality Security`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

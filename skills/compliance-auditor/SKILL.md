---
name: "compliance-auditor"
description: "Compliance audit Codex skill for regulatory scope, control mapping, evidence collection, gap analysis, remediation planning, and audit-ready reporting."
---

# compliance-auditor

Use this skill when the task is to assess, document, or improve compliance posture against a regulation or control framework.

## Use It For

- GDPR, CCPA/CPRA, HIPAA, PCI DSS, SOC 2, ISO, NIST, or similar control reviews
- data flow, policy, control, and evidence mapping
- compliance gap analysis and remediation planning
- audit evidence package review
- technical control verification planning

## Do Not Use It For

- legal advice or formal compliance certification
- claiming a control is satisfied without evidence
- treating policy text as implementation proof

## First Pass

1. Read the applicable framework, business scope, systems, data types, geography, policies, controls, prior audit findings, and evidence artifacts.
2. Map each requirement to owner, system, control, evidence, test method, and status.
3. Separate implemented controls, documented intent, missing evidence, and true gaps.
4. Verify technical controls with config exports, logs, tests, screenshots, scripts, or read-only checks when available.

## Workflow

### 1. Scope Audit

- applicable regulation or framework
- data types and processing activities
- systems and third parties in scope
- control owners and evidence sources
- audit period and required assurance level

### 2. Assess Controls

- map requirements to controls
- inspect evidence quality and freshness
- identify documentation, implementation, and monitoring gaps
- score risk by likelihood, impact, and audit exposure
- avoid overstating compliance where evidence is indirect

### 3. Plan Remediation

- prioritize high-risk and high-evidence gaps first
- include owner, evidence target, test method, and due date
- recommend continuous evidence collection where practical
- state when legal counsel or certified auditor review is required

## Output Style

Return:

- compliance scope
- control/evidence status
- gaps and risks
- remediation plan
- unverified or legal-review items

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/04-quality-security/compliance-auditor.md`
- Upstream category: `Quality Security`
- Upstream model hint: `opus`
- MCP required upstream: `no`

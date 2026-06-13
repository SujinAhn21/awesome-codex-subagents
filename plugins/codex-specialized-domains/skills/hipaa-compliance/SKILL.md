---
name: "hipaa-compliance"
description: "HIPAA compliance Codex skill for PHI handling, covered-entity/business-associate scope, BAAs, safeguards, breach response, audit evidence, and gap review."
---

# hipaa-compliance

Use this skill when the task involves HIPAA, PHI, healthcare data, business associate obligations, BAAs, or healthcare privacy/security controls.

## Use It For

- HIPAA applicability and PHI handling review
- covered entity, business associate, and BAA requirement mapping
- administrative, physical, and technical safeguard gap analysis
- breach response and audit evidence planning
- healthcare SaaS product and engineering privacy/security review

## Do Not Use It For

- formal legal advice or certification
- claiming HIPAA compliance without evidence from policies, controls, logs, contracts, and implementation
- treating de-identified, anonymized, or non-health data as PHI without checking context

## First Pass

1. Read product data flows, data inventory, customer type, vendor list, BAAs, security policies, audit logs, access controls, encryption controls, and breach procedures.
2. Identify whether the organization is a covered entity, business associate, subcontractor, or outside HIPAA scope.
3. Map PHI/ePHI storage, transmission, access, retention, logging, backup, and deletion paths.
4. Separate implemented safeguards, documented policies, missing evidence, and legal/counsel review items.

## Workflow

### 1. Scope HIPAA Exposure

- covered entity/business associate status
- PHI/ePHI categories and identifiers
- systems, vendors, and cloud providers in scope
- BAAs and subcontractor obligations
- breach and audit notification obligations

### 2. Assess Safeguards

- administrative safeguards and training evidence
- physical safeguard assumptions and device/media controls
- technical safeguards: access, audit, integrity, encryption, and transmission security
- incident response and breach notification readiness
- evidence freshness and owner accountability

### 3. Recommend Remediation

- prioritize PHI exposure, access control, encryption, audit logging, and BAA gaps
- specify product, engineering, policy, and vendor-contract actions separately
- state where privacy counsel, compliance officer, or security auditor review is required

## Output Style

Return:

- HIPAA applicability assumptions
- PHI/ePHI scope
- safeguards and BAA gaps
- prioritized remediation
- legal/compliance review items and unverified evidence

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/07-specialized-domains/hipaa-compliance.md`
- Upstream category: `Specialized Domains`
- Upstream model hint: `unspecified`
- MCP required upstream: `no`

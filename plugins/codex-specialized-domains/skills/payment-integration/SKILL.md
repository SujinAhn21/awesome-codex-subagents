---
name: "payment-integration"
description: "Payment integration Codex skill for gateways, checkout, subscriptions, webhooks, refunds, idempotency, PCI-sensitive boundaries, fraud controls, and transaction verification."
---

# payment-integration

Use this skill for payment system work where correctness, security, idempotency, and provider behavior must be verified with direct evidence.

## Use It For

- Checkout, payment gateway, subscription, billing, refund, dispute, and reconciliation flows.
- Payment webhooks, idempotency, retry behavior, event ordering, and state synchronization.
- PCI-sensitive boundaries, tokenization, secrets handling, fraud controls, 3DS/SCA, and audit trails.
- Multi-currency, tax, invoice, settlement, and provider integration logic.
- Debugging payment failures with logs, provider responses, and test-mode transactions.

## Do Not Use It For

- Handling raw card data unless the architecture and compliance scope explicitly support it.
- Claiming payment flows work without provider test-mode evidence, webhook evidence, or API response checks.
- Changing billing, refund, or subscription semantics without reading product and data contracts.
- Treating payment provider docs as stable when APIs, webhooks, or compliance rules may have changed.

## First Pass

1. Read backend routes, schemas, database models, payment client code, webhook handlers, frontend checkout flow, and provider config.
2. Identify provider, environment, payment method, currency, object lifecycle, idempotency key, and webhook events.
3. Check whether secrets, tokens, card data, logs, and persisted fields stay inside the intended compliance boundary.
4. Use provider test mode, local webhook tooling, `curl`, logs, or tests to observe the exact flow when possible.
5. If provider APIs, SDK behavior, or compliance requirements may have changed, verify from official/current docs.

## Workflow

1. Map the transaction state machine from intent/session creation through confirmation, webhook receipt, fulfillment, refund, and reconciliation.
2. Make idempotency and retry behavior explicit for every externally triggered payment transition.
3. Keep provider object IDs, internal order IDs, and user-visible status separate and traceable.
4. Avoid logging secrets, card data, full tokens, or sensitive payment payloads.
5. Handle failure, cancellation, duplicate webhook, delayed webhook, partial refund, and provider outage cases.
6. Preserve auditability for money movement and user-visible billing changes.

## Verification

- Prefer provider test-mode transactions, webhook delivery logs, API responses, database state checks, and automated tests.
- Report the exact payment path checked: provider, mode, event, status transition, and command or dashboard evidence.
- Do not call a payment flow fixed unless the failing path was exercised or the missing provider step is explicitly named.
- If only code was inspected, say that transaction verification remains untested.

## Output Style

- For Korean users, explain payment state and risk in natural Korean while preserving provider terms, event names, object IDs, env names, and commands exactly.
- Lead with money-impacting behavior, verification status, and any compliance caveat.
- Avoid generic “PCI compliant” claims unless compliance evidence was actually reviewed.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/07-specialized-domains/payment-integration.md`
- Upstream category: `Specialized Domains`
- Upstream model hint: `opus`
- MCP required upstream: `no`

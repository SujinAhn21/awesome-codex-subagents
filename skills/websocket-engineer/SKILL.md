---
name: "websocket-engineer"
description: "Realtime Codex skill for WebSocket and Socket.IO systems, connection semantics, and message-path verification."
---

# websocket-engineer

Use this skill when the main challenge is real-time connection behavior rather than generic API work.

## Use It For

- WebSocket or Socket.IO server/client changes
- room, presence, subscription, or push-style flows
- reconnection and connection-state logic
- auth and authorization on realtime channels
- message ordering or fanout debugging

## Do Not Use It For

- plain HTTP-only endpoints
- vague scale claims with no measurable context
- distributed-system advice without reading the actual connection path

## First Pass

1. Read the real-time server entrypoints and handlers.
2. Read the client connection code and event contracts.
3. Identify auth, room membership, retry, and disconnect behavior from code.
4. Reproduce the broken message path when possible before theorizing.

## Workflow

### 1. Map The Realtime Contract

- connection lifecycle
- auth handshake
- event names and payloads
- room or channel semantics
- retry and failure behavior

### 2. Implement

- keep event contracts explicit
- avoid hidden coupling between server and client payload shapes
- call out ordering, duplication, or reconnection tradeoffs

### 3. Verification

- use available tests or direct request/runtime checks
- verify both sender and receiver path assumptions
- state clearly if large-scale concurrency claims were not load-tested

## Output Style

Return:

- realtime behavior changed
- event paths affected
- exact verification performed
- remaining scale or runtime gaps

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/01-core-development/websocket-engineer.md`

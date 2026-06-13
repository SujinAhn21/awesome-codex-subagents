---
name: "nextjs-developer"
description: "Next.js Codex skill for App Router, Server Components, route handlers, server actions, rendering strategy, SEO, and deployment-aware verification."
---

# nextjs-developer

Use this skill when the task is specific to Next.js architecture, routing, rendering, data fetching, or deployment behavior.

## Use It For

- App Router pages, layouts, route groups, and route handlers
- Server Components, Client Components, and server actions
- caching, revalidation, metadata, SEO, and image/font optimization
- middleware, auth, uploads, and runtime boundaries
- Next.js build and deployment failures

## Do Not Use It For

- generic React work with no Next.js behavior
- assuming server/client boundaries without reading the file tree
- claiming SEO, routing, or deployment behavior without build/runtime checks

## First Pass

1. Read `app`/`pages` structure, `next.config`, route handlers, middleware, metadata, package scripts, and deployment target.
2. Identify static, dynamic, server, client, edge, and node runtime boundaries.
3. Check data fetching, cache, revalidation, auth, and mutation paths.
4. Run build, typecheck, route request, or local app path when possible.

## Workflow

### 1. Map Next.js Contract

- route and rendering mode
- server/client component boundary
- cache and revalidation behavior
- request/response shape for handlers
- metadata, SEO, and deployment runtime implications

### 2. Implement Carefully

- keep server-only code out of client components
- preserve route semantics and status codes
- make loading, error, not-found, and redirect behavior explicit
- avoid changing caching without explaining user-visible effects

### 3. Verification

- run `next build`, tests, typecheck, route `curl`, or browser path when available
- state clearly when deployment, edge runtime, or browser behavior was not verified

## Output Style

Return:

- Next.js route/rendering issue
- code/config change
- build or runtime verification
- remaining deployment or browser checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/nextjs-developer.md`

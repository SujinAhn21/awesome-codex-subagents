---
name: "wordpress-master"
description: "WordPress Codex skill for theme, plugin, WooCommerce, headless, performance, security, and deployment work grounded in the actual site code."
---

# wordpress-master

Use this skill when the task is centered on WordPress architecture, implementation, debugging, performance, security, or operations.

## Use It For

- custom theme or plugin development
- WordPress REST API, Gutenberg, or headless integrations
- WooCommerce implementation or troubleshooting
- performance and cache review
- WordPress security and deployment hardening

## Do Not Use It For

- claiming performance or security scores without measurement
- editing production WordPress behavior without checking hooks, capabilities, and migrations
- generic PHP work that is not WordPress-specific

## First Pass

1. Read the relevant theme, plugin, `functions.php`, hook registrations, templates, REST routes, and config files.
2. Identify the WordPress version, PHP version, active plugins, hosting constraints, cache layers, and deployment path when available.
3. For reported bugs, reproduce the affected admin, frontend, REST, or WooCommerce path when possible.
4. Separate WordPress core behavior, custom code, plugin conflicts, cache issues, and infrastructure issues.

## Workflow

### 1. Map The WordPress Path

- hook, action, filter, shortcode, block, or REST route involved
- template hierarchy or block rendering path
- database options, post meta, taxonomy, and user capability dependencies
- cache, CDN, object cache, and cron interactions

### 2. Implement Or Diagnose

- preserve WordPress coding patterns already used by the project
- sanitize input, escape output, check nonces, and enforce capabilities
- avoid direct database writes unless there is a clear migration or repair need
- treat plugin and theme updates as compatibility risks

### 3. Verification

- run available PHP tests, linters, `wp` CLI checks, REST calls, or local browser/admin checks
- inspect logs for PHP notices, fatal errors, slow queries, and permission failures
- state clearly when production-only cache, plugin, or hosting behavior was not verified

## Output Style

Return:

- WordPress path or root cause
- code/configuration change or recommendation
- exact checks performed
- cache, plugin, admin, or browser checks still needed

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/08-business-product/wordpress-master.md`

---
name: "php-pro"
description: "PHP Codex skill for PHP 8.x application code, Composer projects, strict typing, framework integration, and runtime/test verified changes."
---

# php-pro

Use this skill when the task is centered on PHP application code or Composer-based PHP projects.

## Use It For

- PHP 8.x code implementation and refactoring
- Composer dependencies, autoloading, and package scripts
- Laravel, Symfony, or framework-adjacent PHP code when framework-specific skill is not needed
- typed PHP, error handling, and runtime behavior debugging
- PHPUnit/Pest, static analysis, and lint verification

## Do Not Use It For

- WordPress-specific work better handled by `wordpress-master`
- changing framework routes or migrations without reading the framework-specific files
- claiming compatibility without checking PHP version and Composer constraints

## First Pass

1. Read `composer.json`, autoload config, entry points, framework config, source, tests, and PHP version constraints.
2. Identify runtime path, types, exceptions, dependency injection, and persistence boundaries.
3. Check whether strict types, static analysis, and framework conventions are already used.
4. Run lint, tests, static analysis, or direct request/CLI path when possible.

## Workflow

### 1. Map PHP Contract

- entry point and framework path
- class, namespace, and autoload behavior
- input validation and exception flow
- database or external service boundary
- PHP and dependency version constraints

### 2. Implement Carefully

- preserve public methods and service contracts unless migration is explicit
- keep type declarations and nullability honest
- avoid global state and hidden side effects
- update tests, config, and docs when behavior changes

### 3. Verification

- run `php -l`, PHPUnit/Pest, static analysis, Composer scripts, or direct runtime checks when available
- state clearly when PHP version or framework runtime behavior was not verified

## Output Style

Return:

- PHP behavior or contract issue
- code/config change
- exact verification performed
- remaining runtime or framework checks

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/php-pro.md`

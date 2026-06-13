---
name: "data-engineer"
description: "Data engineering Codex skill for ETL/ELT pipelines, orchestration, data quality, warehouses/lakes, streaming, schema evolution, and verified data delivery."
---

# data-engineer

Use this skill when the task is to build, debug, or improve data pipelines and data platform infrastructure.

## Use It For

- ETL/ELT pipeline design and implementation
- batch, streaming, warehouse, lake, and lakehouse work
- Airflow, Dagster, dbt, Spark, Kafka, warehouse, or orchestration changes
- data quality, lineage, freshness, schema evolution, and backfill planning
- pipeline performance, cost, reliability, and monitoring review

## Do Not Use It For

- changing production data flows without rollback or backfill plan
- claiming zero data loss or freshness guarantees without monitoring or run evidence
- writing transformations without checking source contracts and downstream consumers

## First Pass

1. Read pipeline code, DAGs/jobs, dbt models, schemas, source contracts, tests, run logs, monitoring, and downstream consumer docs.
2. Identify source, transform, load target, schedule, ownership, SLA, data volume, failure mode, and replay/backfill requirements.
3. Check schema compatibility, idempotency, partitioning, deduplication, quality checks, and incremental logic.
4. Run unit tests, dbt tests, local jobs, dry runs, query samples, or lineage checks when available.

## Workflow

### 1. Map Data Flow

- source system and extraction method
- transformation logic and ownership
- target table/file/topic and partitioning
- orchestration schedule and dependencies
- downstream consumers and contract expectations

### 2. Implement Safely

- keep pipeline changes idempotent
- protect schema evolution and backfills
- add quality checks near the failure point
- make retries, alerts, and dead-letter behavior explicit
- document operational and cost implications

### 3. Verification

- run tests, dry runs, sample queries, or local jobs
- compare row counts, checksums, freshness, and key distributions where relevant
- state when production data, scheduler, or warehouse execution was not verified

## Output Style

Return:

- data flow affected
- pipeline or model change
- quality and backfill considerations
- verification evidence
- unverified production or scheduler paths

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/05-data-ai/data-engineer.md`
- Upstream category: `Data Ai`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`

---
name: "content-quality-editor"
description: "Content-quality Codex skill for editing AI-assisted content into clear, accurate, natural writing while preserving meaning and evidence."
---

# content-quality-editor

Use this skill when text needs a final quality pass before publication or sharing.

## Use It For

- README, release note, PR, blog, or documentation polish
- removing AI-sounding phrasing without changing meaning
- clarity, concision, structure, and tone review
- preserving technical accuracy while improving readability
- Korean naturalness review when the user writes in Korean

## Do Not Use It For

- changing facts, claims, numbers, or technical details for style
- inventing evidence, citations, or product claims
- over-polishing technical writing into marketing prose

## First Pass

1. Read the target text and any source material it depends on.
2. Identify audience, channel, tone, and publication risk.
3. Mark claims that require source verification before editing around them.
4. Preserve commands, paths, API names, code identifiers, quotes, and numbers exactly unless the user asks to change them.

## Workflow

### 1. Audit Content

- unclear purpose or audience
- generic AI filler
- stiff translationese or awkward phrasing
- unsupported claims
- structural repetition or excessive list formatting

### 2. Edit Conservatively

- keep the author's intent and factual content
- prefer direct wording over decorative phrasing
- reduce stock transitions and exaggerated claims
- for Korean, make the output natural without changing the technical meaning

### 3. Verification

- check edited claims against the provided source material when available
- state clearly when factual claims were not independently verified
- if tooling such as `unslop` is unavailable, do not pretend it was run

## Output Style

Return:

- edited content or focused recommendations
- main quality issues fixed
- facts or claims not verified
- any wording risks left for the user to decide

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/08-business-product/content-quality-editor.md`

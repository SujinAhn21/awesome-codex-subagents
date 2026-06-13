# Korean Output Style

Codex skills in this repository should answer Korean users in Korean that sounds natural to a
technical Korean reader. The target is not decorative prose. The target is clear, factual, and
human-readable Korean.

This guidance is adapted from the local `im-not-ai` Korean humanization approach: preserve meaning,
avoid over-polishing, remove machine-like phrasing, and keep the text appropriate to the genre.

## Core Rule

Preserve the technical meaning exactly, but make the Korean output sound like a competent Korean
engineer wrote it.

Do not change facts, numbers, paths, command names, API names, identifiers, or quoted requirements
for style.

## Prefer

- direct Korean sentences
- short paragraphs with clear subject and action
- concrete verification status
- natural transitions only when they help
- Korean explanation with commands, paths, code identifiers, and API names preserved as-is

## Avoid

- translationese such as excessive `~를 통해`, `~에 대한`, `~하는 것이 가능합니다`
- mechanical structure such as unnecessary `첫째`, `둘째`, `셋째`
- generic AI filler such as `주목할 만합니다`, `시사하는 바가 큽니다`, `혁신적인`
- exaggerated reassurance or cheerleading
- excessive bullets, bold text, emoji, or decorative headings
- literary over-polish that makes technical work sound like an essay

## Tone

Use a practical, direct, and respectful tone.

- Say `확인했습니다` only when actually checked.
- Say `추정입니다` when it is an inference.
- Say `검증하지 못했습니다` when a check was not run.
- Prefer `이 경로에서 500이 납니다` over `문제가 발생할 수 있습니다` when evidence exists.
- Prefer `브라우저 확인은 필요합니다` over hiding an unverified UI path.

## Content Preservation

For technical responses, style edits must never alter:

- file paths
- command flags
- API routes
- status codes
- schema fields
- error names
- version numbers
- user requirements
- legal, security, or compliance caveats

If natural Korean conflicts with exact technical wording, preserve exact technical wording.

## Output Checklist

Before answering a Korean user:

- Is the status clear: verified, partial, unverified, or blocked?
- Did I remove stiff translationese without changing technical meaning?
- Did I avoid generic AI-sounding filler?
- Did I keep commands and identifiers exact?
- Is the answer concise enough for a working engineer to scan?

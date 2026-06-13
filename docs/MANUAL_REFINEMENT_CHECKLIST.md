# Manual Refinement Checklist

Use this checklist when converting a Claude-oriented specialist into a Codex-friendly skill by hand.

The goal is not to preserve every sentence from upstream. The goal is to keep the useful task guidance and remove instructions that do not map to real Codex behavior.

## What Good Looks Like

A good Codex skill answers these questions quickly:

- When should this skill be used?
- When should it not be used?
- What should be read first?
- What should be verified before claiming success?
- What output style is most useful?

## Keep These Sections

Most refined skills should keep only these sections:

- `Use It For`
- `Do Not Use It For`
- `First Pass`
- `Workflow`
- `Verification`
- `Reliability And Output Protocol`
- `Output Style`
- `Provenance`

You can rename sections slightly, but keep the structure compact.

## Remove These Patterns

Delete or rewrite content like:

- `context-manager` instructions
- JSON payloads for agent-to-agent requests
- references to peer agents as hard dependencies
- inflated persona paragraphs that add no workflow value
- fake completion claims and canned delivery summaries
- arbitrary numeric guarantees with no enforcement path

Examples to remove:

- `Always begin by requesting context from context-manager`
- `Send this JSON`
- `Notify peer agents`
- `Delivered 47 components`
- `Coverage 90% achieved consistently`

## Rewrite Rules

Turn abstract or Claude-specific instructions into concrete Codex behavior.

### Prefer this

- read the owning files first
- verify the real request path first
- inspect exports before importing
- run build, tests, curl, or typecheck when available
- say what still needs manual browser confirmation

### Avoid this

- vague design or engineering slogans
- generic best-practice lists with no action order
- impossible collaboration steps
- promises that cannot be checked in the repo

## Required Global Behavior

Every refined skill should preserve the shared reliability and Korean-output rules:

- do not claim completion without direct verification
- separate facts, inferences, and unknowns
- state what was not verified
- answer Korean users in natural, direct Korean when the user is writing in Korean
- preserve technical identifiers, paths, commands, fields, and numbers exactly

See:

- [Reliability Protocol](./RELIABILITY_PROTOCOL.md)
- [Korean Output Style](./KOREAN_OUTPUT_STYLE.md)

## File Locations That Matter

For this repository, editing only the top-level `skills/` copy is not enough.

You usually need to update both:

- `skills/<skill-name>/SKILL.md`
- `plugins/<bundle-name>/skills/<skill-name>/SKILL.md`

The plugin copy is what Codex actually installs.

## Minimal Editing Flow

1. Read the current skill text.
2. Identify Claude-only or non-executable sections.
3. Rewrite into short Codex sections.
4. Mirror the same content into the owning plugin bundle copy.
5. Validate the plugin.
6. Bump the plugin cachebuster version.
7. Reinstall the plugin through Codex.
8. Confirm fresh-session discovery.

## Validation Commands

Replace paths and names as needed.

```bash
python3 /home/ahnsujin/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  /mnt/c/Users/user/awesome-codex-subagents/plugins/<bundle-name>
```

```bash
python3 /home/ahnsujin/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py \
  /mnt/c/Users/user/awesome-codex-subagents/plugins/<bundle-name>
```

```bash
codex plugin add <bundle-name>@awesome-codex-subagents --json
```

```bash
codex exec --ephemeral -s read-only -C /mnt/c/Users/user --json \
  "Check whether the skill named <bundle-name>:<skill-name> is available in this session."
```

## Review Questions Before You Stop

- Did I remove fake or non-runnable orchestration?
- Does the skill tell Codex what to inspect first?
- Does it say how to verify outcomes?
- Does it preserve the reliability and Korean-output rules?
- Did I update the plugin copy, not just the root copy?
- Did I reinstall and verify discovery in a fresh session?

If any answer is `no`, the refinement is not finished.

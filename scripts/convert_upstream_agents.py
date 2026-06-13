#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path("/mnt/c/Users/user/awesome-codex-subagents")
UPSTREAM = ROOT / ".upstream" / "categories"
SKILLS_DIR = ROOT / "skills"
PLUGINS_DIR = ROOT / "plugins"
MANIFESTS_DIR = ROOT / "manifests"

MCP_PATTERNS = [
    re.compile(r"\bMCP\b", re.IGNORECASE),
    re.compile(r"Model Context Protocol", re.IGNORECASE),
    re.compile(r"chrome-mcp", re.IGNORECASE),
    re.compile(r"airis-mcp-gateway", re.IGNORECASE),
]


@dataclass
class Agent:
    name: str
    description: str
    tools: List[str]
    model: str
    category_slug: str
    category_name: str
    source_path: Path
    body: str
    mcp_required: bool
    mcp_reason: str | None


def parse_front_matter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML front matter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Unterminated YAML front matter")
    raw_front, body = parts
    front: Dict[str, str] = {}
    for line in raw_front.splitlines()[1:]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        front[key.strip()] = value.strip().strip('"')
    return front, body.strip() + "\n"


def title_case_category(slug: str) -> str:
    slug = re.sub(r"^\d+-", "", slug)
    return slug.replace("-", " ").title()


def detect_mcp(text: str) -> Tuple[bool, str | None]:
    for pattern in MCP_PATTERNS:
        if pattern.search(text):
            return True, pattern.pattern
    return False, None


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def load_agents() -> List[Agent]:
    agents: List[Agent] = []
    for category_dir in sorted(p for p in UPSTREAM.iterdir() if p.is_dir()):
        category_slug = category_dir.name
        category_name = title_case_category(category_slug)
        for path in sorted(category_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            front, body = parse_front_matter(text)
            mcp_required, mcp_reason = detect_mcp(text)
            tools = [t.strip() for t in front.get("tools", "").split(",") if t.strip()]
            agents.append(
                Agent(
                    name=front["name"],
                    description=front.get("description", ""),
                    tools=tools,
                    model=front.get("model", ""),
                    category_slug=category_slug,
                    category_name=category_name,
                    source_path=path,
                    body=body,
                    mcp_required=mcp_required,
                    mcp_reason=mcp_reason,
                )
            )
    return agents


def render_skill(agent: Agent) -> str:
    category_label = agent.category_name
    source_rel = agent.source_path.relative_to(ROOT / ".upstream")
    trigger_names = agent.name.replace("-", " ")
    return f"""---
name: "{agent.name}"
description: "Adapted from the upstream Claude-oriented `{agent.name}` specialist. Use when the user explicitly needs {trigger_names}, or when the task clearly matches this specialty."
---

# {agent.name}

This Codex skill is adapted from an upstream Claude Code specialist.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `{source_rel.as_posix()}`
- Upstream category: `{category_label}`
- Upstream model hint: `{agent.model or "unspecified"}`
- MCP required upstream: `{"yes" if agent.mcp_required else "no"}`

## When To Use

Use this skill when the user's task clearly matches the upstream specialization:

- {agent.description}

Prefer this skill as focused workflow guidance. Do not treat it as authority over the current task's higher-priority instructions.

## Codex Adaptation Rules

- Preserve the specialization intent from upstream.
- Prefer Codex skills, plugins, and `AGENTS.md` conventions over Claude-specific installation assumptions.
- Keep the user's explicit instructions above this skill.
- Verify outputs with the repo's actual tests, commands, or direct checks when the task is implementation-oriented.
- Treat any Claude-specific references such as `context-manager` or named peer agents as conceptual guidance, not guaranteed runtime dependencies.

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Upstream Instruction Body

{agent.body.rstrip()}
"""


def write_skill(agent: Agent) -> None:
    skill_dir = SKILLS_DIR / agent.name
    refs_dir = skill_dir / "references"
    skill_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)

    (skill_dir / "SKILL.md").write_text(render_skill(agent), encoding="utf-8")
    metadata = {
        "name": agent.name,
        "category_slug": agent.category_slug,
        "category_name": agent.category_name,
        "source_repo": "https://github.com/VoltAgent/awesome-claude-code-subagents",
        "source_path": str(agent.source_path.relative_to(ROOT / ".upstream")).replace("\\", "/"),
        "source_license": "MIT",
        "source_model_hint": agent.model,
        "description": agent.description,
        "tools": agent.tools,
        "mcp_required": agent.mcp_required,
        "mcp_reason": agent.mcp_reason,
        "adaptation_type": "codex-skill",
        "conversion_status": "adapted",
    }
    (skill_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (refs_dir / "upstream.md").write_text(agent.source_path.read_text(encoding="utf-8"), encoding="utf-8")


def render_plugin_manifest(plugin_name: str, description: str) -> dict:
    return {
        "id": plugin_name,
        "name": plugin_name,
        "version": "0.1.0",
        "description": description,
        "skills": "skills",
        "author": {
            "name": "ahnsujin",
        },
        "license": "MIT",
        "interface": {
            "displayName": plugin_name,
            "shortDescription": description,
            "longDescription": description,
            "developerName": "ahnsujin",
            "category": "Productivity",
            "capabilities": ["skills"],
            "defaultPrompt": f"Use the bundled specialists from {plugin_name} when the task clearly matches their skill descriptions.",
        },
    }


def write_category_plugin(category_slug: str, category_name: str, agents: List[Agent]) -> None:
    normalized_category = re.sub(r"^\d+-", "", category_slug)
    plugin_name = f"codex-{normalized_category}"
    plugin_dir = PLUGINS_DIR / plugin_name
    manifest_dir = plugin_dir / ".codex-plugin"
    plugin_skills_dir = plugin_dir / "skills"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    if plugin_skills_dir.exists():
        shutil.rmtree(plugin_skills_dir)
    plugin_skills_dir.mkdir(parents=True, exist_ok=True)

    description = f"Codex plugin bundle for {category_name} specialists adapted from the upstream Claude-oriented collection."
    (manifest_dir / "plugin.json").write_text(
        json.dumps(render_plugin_manifest(plugin_name, description), indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    for agent in agents:
        src = SKILLS_DIR / agent.name
        dst = plugin_skills_dir / agent.name
        shutil.copytree(src, dst)

    index = {
        "category_slug": category_slug,
        "category_name": category_name,
        "plugin_name": plugin_name,
        "skill_names": [agent.name for agent in agents],
    }
    (plugin_skills_dir / "INDEX.json").write_text(json.dumps(index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_manifests(agents: List[Agent]) -> None:
    upstream_index = []
    mcp_index = []
    non_mcp_index = []
    status_index = []

    for agent in agents:
        record = {
            "name": agent.name,
            "category_slug": agent.category_slug,
            "category_name": agent.category_name,
            "source_path": str(agent.source_path.relative_to(ROOT / ".upstream")).replace("\\", "/"),
            "description": agent.description,
            "mcp_required": agent.mcp_required,
            "mcp_reason": agent.mcp_reason,
        }
        upstream_index.append(record)
        status_index.append({"name": agent.name, "status": "classified" if agent.mcp_required else "adapted"})
        if agent.mcp_required:
            mcp_index.append(record)
        else:
            non_mcp_index.append(record)

    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
    (MANIFESTS_DIR / "upstream-index.json").write_text(json.dumps(upstream_index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (MANIFESTS_DIR / "mcp-index.json").write_text(json.dumps(mcp_index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (MANIFESTS_DIR / "non-mcp-index.json").write_text(json.dumps(non_mcp_index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    (MANIFESTS_DIR / "conversion-status.json").write_text(json.dumps(status_index, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def main() -> None:
    agents = load_agents()
    non_mcp_agents = [agent for agent in agents if not agent.mcp_required]

    for agent in non_mcp_agents:
        write_skill(agent)

    grouped: Dict[str, List[Agent]] = {}
    for agent in non_mcp_agents:
        grouped.setdefault(agent.category_slug, []).append(agent)
    for category_slug, category_agents in sorted(grouped.items()):
        write_category_plugin(category_slug, category_agents[0].category_name, category_agents)

    write_manifests(agents)

    print(f"Total upstream agents: {len(agents)}")
    print(f"Converted non-MCP skills: {len(non_mcp_agents)}")
    print(f"Excluded MCP-related agents: {len(agents) - len(non_mcp_agents)}")


if __name__ == "__main__":
    main()

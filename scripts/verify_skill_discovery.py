#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class PluginIndex:
    plugin_name: str
    index_path: Path
    plugin_path: Path
    manifest_path: Path
    expected_version: str
    skill_names: list[str]


@dataclass(frozen=True)
class InstalledPlugin:
    plugin_name: str
    status: str
    version: str
    path: Path


@dataclass
class VerificationResult:
    plugin_name: str
    expected_version: str
    expected_path: str
    installed: bool
    enabled: bool
    installed_version: str | None
    installed_path: str | None
    expected_skills: list[str]
    available_skills: list[str]
    missing_skills: list[str]
    unexpected_skills: list[str]
    errors: list[str]

    @property
    def ok(self) -> bool:
        return (
            self.installed
            and self.enabled
            and not self.missing_skills
            and not self.unexpected_skills
            and not self.errors
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Verify that every plugin declared in this repository is installed, enabled, and exposes "
            "the expected skill directories from its INDEX.json."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root containing the plugins/ directory.",
    )
    parser.add_argument(
        "--plugin",
        action="append",
        default=[],
        help="Limit verification to one or more plugin names. Repeatable.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the final report as JSON instead of text.",
    )
    parser.add_argument(
        "--fail-on-problem",
        action="store_true",
        help="Exit with status 1 if any plugin is missing, disabled, or structurally inconsistent.",
    )
    return parser.parse_args()


def load_plugin_indexes(root: Path, selected_plugins: set[str]) -> list[PluginIndex]:
    indexes: list[PluginIndex] = []
    for index_path in sorted((root / "plugins").glob("*/skills/INDEX.json")):
        data = json.loads(index_path.read_text(encoding="utf-8"))
        plugin_name = str(data["plugin_name"])
        if selected_plugins and plugin_name not in selected_plugins:
            continue
        plugin_path = index_path.parents[1]
        manifest_path = plugin_path / ".codex-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        indexes.append(
            PluginIndex(
                plugin_name=plugin_name,
                index_path=index_path,
                plugin_path=plugin_path,
                manifest_path=manifest_path,
                expected_version=str(manifest["version"]),
                skill_names=sorted(str(name) for name in data["skill_names"]),
            )
        )
    if selected_plugins:
        found = {index.plugin_name for index in indexes}
        missing_plugins = sorted(selected_plugins - found)
        if missing_plugins:
            raise SystemExit(f"Unknown plugin names: {', '.join(missing_plugins)}")
    return indexes


def load_installed_plugins() -> dict[str, InstalledPlugin]:
    completed = subprocess.run(
        ["codex", "plugin", "list"],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(
            "Failed to run `codex plugin list`:\n"
            f"{completed.stderr.strip() or completed.stdout.strip()}"
        )

    installed: dict[str, InstalledPlugin] = {}
    target_marketplace = False
    for raw_line in completed.stdout.splitlines():
        line = raw_line.rstrip()
        if line.startswith("Marketplace `"):
            target_marketplace = line == "Marketplace `awesome-codex-subagents`"
            continue
        if not target_marketplace:
            continue
        if not line or line.startswith("PLUGIN ") or line.startswith("/"):
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        plugin_and_market = parts[0]
        if not plugin_and_market.endswith("@awesome-codex-subagents"):
            continue
        path = parts[-1]
        version = parts[-2]
        status = " ".join(parts[1:-2])
        suffix = "@awesome-codex-subagents"
        plugin_name = plugin_and_market[:-len(suffix)]
        installed[plugin_name] = InstalledPlugin(
            plugin_name=plugin_name,
            status=status,
            version=version,
            path=Path(path).resolve(),
        )
    return installed


def collect_skill_dirs(skills_path: Path) -> list[str]:
    if not skills_path.exists():
        return []
    return sorted(
        path.name
        for path in skills_path.iterdir()
        if path.is_dir()
    )


def verify_plugin(index: PluginIndex, installed_plugins: dict[str, InstalledPlugin]) -> VerificationResult:
    installed = installed_plugins.get(index.plugin_name)
    errors: list[str] = []
    available_skills: list[str] = []
    missing_skills = list(index.skill_names)
    unexpected_skills: list[str] = []
    installed_version: str | None = None
    installed_path: str | None = None
    is_installed = False
    is_enabled = False

    if installed is None:
        errors.append("plugin is not listed in `codex plugin list` for marketplace `awesome-codex-subagents`")
    else:
        installed_version = installed.version
        installed_path = str(installed.path)
        status_lower = installed.status.lower()
        is_installed = "installed" in status_lower
        is_enabled = "enabled" in status_lower

        if not is_installed:
            errors.append(f"plugin status does not include `installed`: {installed.status}")
        if not is_enabled:
            errors.append(f"plugin status does not include `enabled`: {installed.status}")
        if installed.version != index.expected_version:
            errors.append(
                f"installed version mismatch: expected {index.expected_version}, got {installed.version}"
            )
        expected_plugin_path = index.plugin_path.resolve()
        if installed.path != expected_plugin_path:
            errors.append(
                f"installed path mismatch: expected {expected_plugin_path}, got {installed.path}"
            )
        skill_dir = installed.path / "skills"
        available_skills = collect_skill_dirs(skill_dir)
        missing_skills = sorted(set(index.skill_names) - set(available_skills))
        unexpected_skills = sorted(set(available_skills) - set(index.skill_names))

    return VerificationResult(
        plugin_name=index.plugin_name,
        expected_version=index.expected_version,
        expected_path=str(index.plugin_path.resolve()),
        installed=is_installed,
        enabled=is_enabled,
        installed_version=installed_version,
        installed_path=installed_path,
        expected_skills=index.skill_names,
        available_skills=available_skills,
        missing_skills=missing_skills,
        unexpected_skills=unexpected_skills,
        errors=errors,
    )


def render_text_report(results: list[VerificationResult]) -> str:
    lines: list[str] = []
    ok_count = sum(1 for result in results if result.ok)
    lines.append(f"Verified plugins: {len(results)}")
    lines.append(f"Passing plugins: {ok_count}")
    lines.append(f"Failing plugins: {len(results) - ok_count}")
    lines.append("")
    for result in results:
        status = "OK" if result.ok else "FAIL"
        lines.append(
            f"[{status}] {result.plugin_name} "
            f"(expected={len(result.expected_skills)} available={len(result.available_skills)} "
            f"missing={len(result.missing_skills)} unexpected={len(result.unexpected_skills)})"
        )
        if result.errors:
            for error in result.errors:
                lines.append(f"  error: {error}")
        if result.missing_skills:
            lines.append(f"  missing: {', '.join(result.missing_skills)}")
        if result.unexpected_skills:
            lines.append(f"  unexpected: {', '.join(result.unexpected_skills)}")
    return "\n".join(lines)


def render_json_report(results: list[VerificationResult]) -> str:
    payload: dict[str, Any] = {
        "summary": {
            "plugins": len(results),
            "passing_plugins": sum(1 for result in results if result.ok),
            "failing_plugins": sum(1 for result in results if not result.ok),
            "expected_skills": sum(len(result.expected_skills) for result in results),
            "available_skills": sum(len(result.available_skills) for result in results),
            "missing_skills": sum(len(result.missing_skills) for result in results),
            "unexpected_skills": sum(len(result.unexpected_skills) for result in results),
        },
        "results": [
            {
                "plugin_name": result.plugin_name,
                "ok": result.ok,
                "expected_version": result.expected_version,
                "installed_version": result.installed_version,
                "expected_path": result.expected_path,
                "installed_path": result.installed_path,
                "installed": result.installed,
                "enabled": result.enabled,
                "expected_skills": result.expected_skills,
                "available_skills": result.available_skills,
                "missing_skills": result.missing_skills,
                "unexpected_skills": result.unexpected_skills,
                "errors": result.errors,
            }
            for result in results
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=True)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    selected_plugins = set(args.plugin)
    indexes = load_plugin_indexes(root, selected_plugins)
    if not indexes:
        raise SystemExit("No plugin indexes found to verify.")

    installed_plugins = load_installed_plugins()
    results = [verify_plugin(index, installed_plugins) for index in indexes]
    results.sort(key=lambda item: item.plugin_name)

    report = render_json_report(results) if args.json else render_text_report(results)
    print(report)

    has_problem = any(not result.ok for result in results)
    if has_problem and args.fail_on_problem:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fetch all public repos, run tokei, and update README with LOC tables."""

import json
import os
import subprocess
import tempfile
from pathlib import Path

GITHUB_USER = "Ameyanagi"
README_PATH = Path(__file__).resolve().parent.parent.parent / "README.md"
START_MARKER = "<!-- LOC:START -->"
END_MARKER = "<!-- LOC:END -->"

# Languages to ignore (markup, config, etc.)
IGNORED_LANGUAGES = {
    "HTML", "CSS", "SCSS", "Less", "Sass",
    "Dockerfile", "Makefile", "Shell", "Nix",
    "JSON", "YAML", "TOML", "XML", "SVG",
    "Markdown", "Plain Text", "Text", "INI",
    "Batch", "CSV", "Diff", "Git Attributes",
    "EditorConfig", "Ignore List",
}


def get_repos():
    """Get all public, non-fork, non-archived repos."""
    result = subprocess.run(
        [
            "gh", "api", f"/users/{GITHUB_USER}/repos",
            "--paginate",
            "-q", '.[] | select(.fork == false and .archived == false) | .name',
        ],
        capture_output=True, text=True, check=True,
    )
    return [name.strip() for name in result.stdout.strip().split("\n") if name.strip()]


def clone_and_count(repo_name, tmpdir):
    """Shallow-clone a repo and run tokei on it."""
    repo_dir = os.path.join(tmpdir, repo_name)
    try:
        subprocess.run(
            ["git", "clone", "--depth=1", "--quiet",
             f"https://github.com/{GITHUB_USER}/{repo_name}.git", repo_dir],
            capture_output=True, text=True, check=True, timeout=120,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print(f"  Skipping {repo_name} (clone failed)")
        return None

    try:
        result = subprocess.run(
            ["tokei", "--output", "json", repo_dir],
            capture_output=True, text=True, check=True, timeout=60,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError):
        print(f"  Skipping {repo_name} (tokei failed)")
        return None


def aggregate(all_results):
    """Aggregate tokei results across all repos.

    Returns:
        lang_totals: {language: {code, comments, blanks, files}}
        repo_totals: {repo_name: {code, primary_language}}
    """
    lang_totals = {}
    repo_totals = {}

    for repo_name, tokei_data in all_results.items():
        if not tokei_data:
            continue

        repo_code = 0
        repo_primary_lang = ""
        repo_primary_code = 0

        for lang, stats in tokei_data.items():
            if lang in IGNORED_LANGUAGES or lang == "Total":
                continue

            code = stats.get("code", 0)
            comments = stats.get("comments", 0)
            blanks = stats.get("blanks", 0)
            children = stats.get("children", {})
            # tokei nests file-level stats under "reports" or at top level
            files = len(stats.get("reports", []))

            # Also check children for additional stats
            for child_stats in children.values():
                code += child_stats.get("code", 0)
                comments += child_stats.get("comments", 0)
                blanks += child_stats.get("blanks", 0)
                files += len(child_stats.get("reports", []))

            if code == 0:
                continue

            if lang not in lang_totals:
                lang_totals[lang] = {"code": 0, "comments": 0, "blanks": 0, "files": 0}

            lang_totals[lang]["code"] += code
            lang_totals[lang]["comments"] += comments
            lang_totals[lang]["blanks"] += blanks
            lang_totals[lang]["files"] += files

            repo_code += code
            if code > repo_primary_code:
                repo_primary_code = code
                repo_primary_lang = lang

        if repo_code > 0:
            repo_totals[repo_name] = {"code": repo_code, "primary_language": repo_primary_lang}

    return lang_totals, repo_totals


def fmt(n):
    """Format number with commas."""
    return f"{n:,}"


def generate_tables(lang_totals, repo_totals):
    """Generate markdown tables."""
    total_code = sum(v["code"] for v in lang_totals.values())
    if total_code == 0:
        return "No data available.\n"

    lines = []

    # Language summary table
    lines.append("### Languages")
    lines.append("")
    lines.append("| Language | Files | Lines of Code | % |")
    lines.append("|----------|------:|-------------:|--:|")

    sorted_langs = sorted(lang_totals.items(), key=lambda x: x[1]["code"], reverse=True)
    for lang, stats in sorted_langs:
        pct = stats["code"] / total_code * 100
        if pct < 0.5:
            continue
        lines.append(f"| {lang} | {fmt(stats['files'])} | {fmt(stats['code'])} | {pct:.1f}% |")

    lines.append(f"| **Total** | **{fmt(sum(v['files'] for v in lang_totals.values()))}** | **{fmt(total_code)}** | **100%** |")
    lines.append("")

    # Top repos table
    lines.append("### Top Repositories by Lines of Code")
    lines.append("")
    lines.append("| Repository | Primary Language | Lines of Code |")
    lines.append("|------------|-----------------|-------------:|")

    sorted_repos = sorted(repo_totals.items(), key=lambda x: x[1]["code"], reverse=True)
    for repo_name, stats in sorted_repos[:15]:
        link = f"[{repo_name}](https://github.com/{GITHUB_USER}/{repo_name})"
        lines.append(f"| {link} | {stats['primary_language']} | {fmt(stats['code'])} |")

    lines.append("")
    return "\n".join(lines)


def update_readme(tables_md):
    """Replace content between markers in README.md."""
    content = README_PATH.read_text()

    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)

    if start_idx == -1 or end_idx == -1:
        print("Markers not found in README.md")
        return False

    new_content = (
        content[:start_idx + len(START_MARKER)]
        + "\n"
        + tables_md
        + content[end_idx:]
    )

    if new_content == content:
        print("No changes to README.md")
        return False

    README_PATH.write_text(new_content)
    print("README.md updated successfully")
    return True


def main():
    repos = get_repos()
    print(f"Found {len(repos)} repos")

    all_results = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        for i, repo in enumerate(repos, 1):
            print(f"[{i}/{len(repos)}] {repo}")
            all_results[repo] = clone_and_count(repo, tmpdir)

    lang_totals, repo_totals = aggregate(all_results)
    tables_md = generate_tables(lang_totals, repo_totals)
    print("\n" + tables_md)
    update_readme(tables_md)


if __name__ == "__main__":
    main()

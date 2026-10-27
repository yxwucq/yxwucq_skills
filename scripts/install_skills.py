#!/usr/bin/env python3
"""Install repository skills locally; back up existing copies when replacing."""

import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import re
import shutil
import tempfile


def main():
    source_root = Path(__file__).resolve().parents[1] / "skills"
    codex_dir = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=codex_dir / "skills")
    parser.add_argument("--skill", action="append", help="Install only this skill; repeat to select more.")
    parser.add_argument("--replace", action="store_true", help="Back up existing copies before replacing them.")
    args = parser.parse_args()
    available = {p.name: p for p in sorted(source_root.iterdir()) if p.is_dir() and (p / "SKILL.md").is_file()}
    selected = list(dict.fromkeys(args.skill or available))
    if not selected:
        parser.error("No skills found in the repository.")
    for name in selected:
        if name not in available or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            parser.error("Unknown or invalid skill: " + name)
        for p in available[name].rglob("*"):
            if p.is_symlink():
                parser.error("Skill resources must be self-contained; symbolic link found: " + str(p))
    destination = args.dest.expanduser().resolve()
    source_location = source_root.resolve()
    if destination == source_location or source_location in destination.parents:
        parser.error("Installation destination must be outside the repository skills directory.")
    existing = [name for name in selected if (destination / name).exists() or (destination / name).is_symlink()]
    if existing and not args.replace:
        parser.error("Already installed: " + ", ".join(existing) + ". Use --replace to back up and update.")
    destination.mkdir(parents=True, exist_ok=True)
    backup_root = None
    if existing:
        backup_parent = destination.parent / "skill-backups"
        backup_parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-")
        backup_root = Path(tempfile.mkdtemp(prefix=stamp, dir=backup_parent))
    # Stage all copies before touching any installed skill.
    with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=destination.parent) as temp:
        staging = Path(temp)
        for name in selected:
            shutil.copytree(available[name], staging / name, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"))
        completed = []
        moved_backups = []
        try:
            for name in selected:
                target = destination / name
                if name in existing:
                    target.rename(backup_root / name)
                    moved_backups.append(name)
                (staging / name).rename(target)
                completed.append(name)
        except Exception:
            for name in reversed(completed):
                shutil.rmtree(destination / name)
            for name in reversed(moved_backups):
                (backup_root / name).rename(destination / name)
            raise
    for name in selected:
        print("Installed: " + str(destination / name))
    if backup_root:
        print("Previous versions: " + str(backup_root))
    print("The skills will be available on your next Codex turn.")


if __name__ == "__main__":
    main()

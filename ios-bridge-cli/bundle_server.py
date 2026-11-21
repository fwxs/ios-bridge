#!/usr/bin/env python3
"""Copy the iOS Bridge server (app/, static/, templates/, run.py) into the CLI package.

Run before `python -m build` so the wheel ships a working server. The copy lives in
ios_bridge_cli/server/ and is gitignored.
"""
import shutil
from pathlib import Path

CLI_ROOT = Path(__file__).resolve().parent
REPO_ROOT = CLI_ROOT.parent
TARGET = CLI_ROOT / "ios_bridge_cli" / "server"
ENTRIES = ["app", "static", "templates", "run.py"]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def bundle_server() -> Path:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)
    for entry in ENTRIES:
        source = REPO_ROOT / entry
        if not source.exists():
            raise FileNotFoundError(f"server entry not found: {source}")
        if source.is_dir():
            shutil.copytree(source, TARGET / entry, ignore=IGNORE)
        else:
            shutil.copy2(source, TARGET / entry)
    return TARGET


if __name__ == "__main__":
    print(f"Bundled server into {bundle_server()}")

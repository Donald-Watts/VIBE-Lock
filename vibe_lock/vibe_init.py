"""Initialize VIBE-Lock project configuration and ledger."""

import os
import sys
from pathlib import Path
import yaml
from git import Repo

def create_vibe_dir():
    """Create .vibe directory and initialize configuration."""
    vibe_dir = Path(".vibe")
    vibe_dir.mkdir(exist_ok=True)
    
    config = {
        "version": "0.0.1a1",
        "ledger_path": str(vibe_dir / "tpo_ledger.log"),
        "watermark_config": {
            "style": "n-gram",
            "strength": "medium"
        }
    }
    
    with open(vibe_dir / "config.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False)
    
    # Initialize empty ledger
    with open(vibe_dir / "tpo_ledger.log", "w") as f:
        f.write("# VIBE-Lock Temporal Proof-of-Origin Ledger\n")
        f.write("# Format: timestamp|hash|file_path|commit_id\n\n")

def setup_git_hooks():
    """Set up Git hooks for automatic ledger updates."""
    repo = Repo(".")
    hooks_dir = Path(repo.git_dir) / "hooks"
    
    pre_commit_script = """#!/bin/sh
# VIBE-Lock pre-commit hook
vibe-stamp "$@"
"""
    
    with open(hooks_dir / "pre-commit", "w") as f:
        f.write(pre_commit_script)
    os.chmod(hooks_dir / "pre-commit", 0o755)

def main():
    """Main entry point for vibe-init command."""
    try:
        create_vibe_dir()
        setup_git_hooks()
        print("✓ VIBE-Lock initialized successfully")
        print("  - Created .vibe/ directory")
        print("  - Initialized TPO ledger")
        print("  - Set up Git hooks")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

"""Apply VIBE-Lock watermarks and temporal proof-of-origin to files."""

import os
import sys
import time
import hashlib
from pathlib import Path
import yaml
from git import Repo

def load_config():
    """Load VIBE-Lock configuration."""
    config_path = Path(".vibe/config.yaml")
    if not config_path.exists():
        print("Error: VIBE-Lock not initialized. Run 'vibe-init' first.", file=sys.stderr)
        sys.exit(1)
    
    with open(config_path) as f:
        return yaml.safe_load(f)

def calculate_hash(file_path):
    """Calculate SHA-256 hash of file contents."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_git_commit():
    """Get current Git commit ID."""
    try:
        repo = Repo(".")
        return repo.head.commit.hexsha
    except:
        return "no-commit"

def apply_watermark(file_path, config):
    """Apply watermark to file based on configuration."""
    # TODO: Implement actual watermarking based on config["watermark_config"]
    # For now, just append a comment
    with open(file_path, "a") as f:
        f.write(f"\n# VIBE-Lock: {time.time()}\n")

def update_ledger(file_path, config):
    """Update TPO ledger with file information."""
    timestamp = int(time.time())
    file_hash = calculate_hash(file_path)
    commit_id = get_git_commit()
    
    ledger_entry = f"{timestamp}|{file_hash}|{file_path}|{commit_id}\n"
    
    with open(config["ledger_path"], "a") as f:
        f.write(ledger_entry)

def main():
    """Main entry point for vibe-stamp command."""
    if len(sys.argv) < 2:
        print("Usage: vibe-stamp <file>", file=sys.stderr)
        return 1
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found", file=sys.stderr)
        return 1
    
    try:
        config = load_config()
        apply_watermark(file_path, config)
        update_ledger(file_path, config)
        print(f"✓ Stamped {file_path}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

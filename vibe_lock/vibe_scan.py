"""Scan files for VIBE-Lock watermarks and verify temporal proof-of-origin."""

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

def check_ledger(file_path, config):
    """Check if file hash exists in ledger."""
    current_hash = calculate_hash(file_path)
    
    with open(config["ledger_path"]) as f:
        for line in f:
            if line.startswith("#"):
                continue
            try:
                timestamp, hash_val, path, commit = line.strip().split("|")
                if path == str(file_path) and hash_val == current_hash:
                    return {
                        "found": True,
                        "timestamp": int(timestamp),
                        "commit": commit
                    }
            except ValueError:
                continue
    
    return {"found": False}

def check_watermark(file_path, config):
    """Check for watermark in file."""
    # TODO: Implement actual watermark detection based on config["watermark_config"]
    # For now, just check for the comment
    with open(file_path) as f:
        content = f.read()
        return "VIBE-Lock:" in content

def main():
    """Main entry point for vibe-scan command."""
    if len(sys.argv) < 2:
        print("Usage: vibe-scan <file>", file=sys.stderr)
        return 1
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found", file=sys.stderr)
        return 1
    
    try:
        config = load_config()
        ledger_result = check_ledger(file_path, config)
        watermark_result = check_watermark(file_path, config)
        
        print(f"\nScanning {file_path}:")
        print("----------------------------------------")
        
        if ledger_result["found"]:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", 
                                   time.localtime(ledger_result["timestamp"]))
            print(f"✓ TPO Verified")
            print(f"  - Timestamp: {timestamp}")
            print(f"  - Commit: {ledger_result['commit']}")
        else:
            print("✗ No TPO record found")
        
        if watermark_result:
            print("✓ Watermark detected")
        else:
            print("✗ No watermark found")
        
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

"""
CiteGuard AI - GitHub Remote Push Utility
=========================================
Pushes the local git repository (campus-helpdesk-assistant) to the remote GitHub repository:
https://github.com/aarnavsingh999-avs/Citeguard

Usage:
    python code/push_to_github.py [GITHUB_TOKEN]
Or set environment variable GITHUB_TOKEN:
    set GITHUB_TOKEN=ghp_xxxx
    python code/push_to_github.py
"""

import os
import sys
from pathlib import Path
import dulwich.porcelain as p

REPO_DIR = Path(__file__).resolve().parent.parent
REMOTE_REPO = "github.com/aarnavsingh999-avs/Citeguard.git"

def push_repo(token: str = None):
    if not token:
        token = os.environ.get("GITHUB_TOKEN", "").strip()

    if not token and len(sys.argv) > 1:
        token = sys.argv[1].strip()

    if not token:
        print("[ERROR] No GitHub Personal Access Token provided.")
        print("Please provide a GitHub Personal Access Token (classic or fine-grained with 'Contents: Read and Write' permission):")
        print("  python code/push_to_github.py <YOUR_GITHUB_TOKEN>")
        print("Or set the GITHUB_TOKEN environment variable.")
        sys.exit(1)

    remote_url = f"https://{token}@{REMOTE_REPO}"
    print(f"Pushing branch 'main' to https://github.com/aarnavsingh999-avs/Citeguard ...")
    
    try:
        p.push(str(REPO_DIR), remote_url, "refs/heads/main")
        print("[SUCCESS] Successfully pushed all commits to https://github.com/aarnavsingh999-avs/Citeguard on branch 'main'!")
    except Exception as e:
        print(f"[ERROR] Push failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    push_repo()

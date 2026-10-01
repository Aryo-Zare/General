

# %%

import os
import subprocess
from pathlib import Path

# %%


# --- CONFIGURATION ---
# Change this to the folder where you keep all your Git projects
PROJECTS_ROOT = r"C:\code" 

def run_git_command(repo_path, command):
    """Runs a git command inside a specific directory and returns the output."""
    try:
        result = subprocess.run(
            ["git"] + command,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def check_repos():
    print(f"{'PROJECT':<20} | {'LOCAL CHANGES':<15} | {'UNPUSHED COMMITS'}")
    print("-" * 65)

    root = Path(PROJECTS_ROOT)
    
    # Scan for folders containing a .git directory
    for repo_dir in root.iterdir():
        if repo_dir.is_dir() and (repo_dir / ".git").exists():
            
            # 1. Check for uncommitted changes (dirty working directory)
            # --porcelain gives a stable output for scripts
            status = run_git_command(repo_dir, ["status", "--porcelain"])
            has_changes = "YES (Dirty)" if status else "Clean"

            # 2. Check for unpushed commits
            # cherry compares local branch to upstream
            unpushed = run_git_command(repo_dir, ["cherry", "-v"])
            has_unpushed = "YES (Push me!)" if unpushed else "Synced"

            # Formatting the output
            proj_name = repo_dir.name[:30]
            print(f"{proj_name:<20} | {has_changes:<15} | {has_unpushed}")

#========================================================================================

check_repos()

# if __name__ == "__main__":
#     if os.path.exists(PROJECTS_ROOT):
#         check_repos()
#     else:
#         print(f"Error: The path {PROJECTS_ROOT} does not exist. Please update the script.")

# %%


# PROJECT                        | LOCAL CHANGES   | UNPUSHED COMMITS
# -----------------------------------------------------------------
# composition                    | Clean           | Synced
# cq                             | Clean           | Synced
# DL                             | Clean           | Synced
# EMKA                           | Clean           | Synced
# General                        | YES (Dirty)     | Synced
# kidney                         | Clean           | Synced
# math                           | Clean           | Synced
# miscellaneous                  | YES (Dirty)     | Synced
# sam3                           | Clean           | Synced
# shell                          | Clean           | Synced
# telemetry                      | Clean           | Synced
# VISION                         | Clean           | Synced


# %%


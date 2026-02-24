#!/usr/bin/env python3
"""
Run pip-audit from pinned requirement files for deterministic pre-push checks.
"""

import os
import subprocess
import sys


def main():
    """
    Main entry point for pip-audit hook.
    Checks if we're in a venv and audits pinned dependencies.
    """
    # 1) Check if we are inside a virtual environment.
    if "VIRTUAL_ENV" not in os.environ:
        print("ERROR: You must activate a local .venv before pushing.")
        sys.exit(1)

    # 2) Run pip-audit against requirements files (no environment mutation).
    try:
        subprocess.check_call(["pip-audit", "-r", "requirements.txt"])
        subprocess.check_call(["pip-audit", "-r", "requirements-dev.txt"])
    except subprocess.CalledProcessError as e:
        print("pip-audit found vulnerabilities or failed.")
        sys.exit(e.returncode)

    print("No known vulnerabilities found in requirement files.")
    sys.exit(0)


if __name__ == "__main__":
    main()

# AGENTS.md

## Code Quality Workflow
Always use the virtual environment via `.venv/bin/activate` which has the development tools installed.

Known environment issue: `black` can hang when run inside the Codex sandbox in this repository. Run `black .` and `black --check .` outside the sandbox with the `.venv` active.

Before finalizing any code change:
1. Run `isort .`
2. Run `black .`
3. Run `pylint .`
4. Run `pytest`
5. Fix issues introduced by the change. Do NOT fix pylint issues by disabling checks UNLESS this is justified by code style considerations.
6. Re-run checks to confirm clean output.

## Strict Fail Conditions
- Do not finalize if `isort --check-only .` fails.
- Do not finalize if `black --check .` fails.
- Do not finalize if `pylint .` fails.
- Do not finalize if `pylint` score is below `10/10`.
- Do not finalize if `pytest` fails.

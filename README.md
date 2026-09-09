# EECA Python Template

[![CI](https://github.com/EECA-NZ/eeca-python-template/actions/workflows/ci-and-deploy.yml/badge.svg)](https://github.com/EECA-NZ/eeca-python-template/actions/workflows/ci-and-deploy.yml)
[Coverage report](https://eeca-nz.github.io/eeca-python-template/)

A small, modern starting point for EECA Python packages: PEP 621 metadata, a
`src/` layout, uv-locked dependencies, quality checks, dependency auditing,
conventional-commit validation, and coverage publishing from `main`.

## Before using this template

Replace the placeholder distribution/package names, description, version,
repository URL, dependencies, and test. The example test deliberately only
demonstrates pytest discovery; replace it when the project has behaviour to
test. It also means the initial coverage report only describes the test file;
configure a package-only coverage source and threshold once real code exists.

The template supports Python 3.11+. CI tests 3.11 and 3.13. Keep this policy,
`.python-version`, and CI aligned when changing it.

## Quick start

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv sync --all-groups
uv run pre-commit install --install-hooks --hook-type pre-commit
uv run pre-commit install --hook-type commit-msg
uv run pre-commit run --all-files
uv run coverage run -m pytest
uv run coverage report
uv run pip-audit
```

Use `uv lock` after intentionally changing `pyproject.toml`, and commit
`uv.lock`. CI uses `uv sync --locked` to enforce reproducibility.

## CI, Pages, and releases

CI runs on pushes, pull requests to `main`, and manual dispatch. Pages deploys
only after a successful push to `main`; enable **GitHub Actions** under
repository **Settings → Pages**.

This stub deliberately has no automatic release/publishing workflow. Add one
only after its package index, version owner, branch rules, and release policy
are known—this prevents tags, changelogs, and package metadata diverging.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

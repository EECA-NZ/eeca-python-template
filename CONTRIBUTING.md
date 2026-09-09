# Contributing

Use a branch and open a pull request to `main`. PR commits must use
[Conventional Commits](https://www.conventionalcommits.org/), for example
`feat: add calculation API` or `fix(parser): handle blank input`.

Before opening a PR, run:

```bash
uv sync --all-groups
uv run pre-commit run --all-files
uv run coverage run -m pytest
uv run coverage report
uv run pip-audit
```

Add dependencies to `pyproject.toml`, run `uv lock`, and commit `uv.lock`.
Do not edit the lockfile by hand. Add focused tests for new behaviour; agree a
package-only coverage source and threshold once the package contains substantive
code.

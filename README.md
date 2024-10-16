# EECA Python Template

![Tests](https://github.com/EECA/eeca-python-template/actions/workflows/python-tests.yml/badge.svg)
![Linting](https://github.com/EECA/eeca-python-template/actions/workflows/pylint.yml/badge.svg)

This repository serves as a template for Python projects at EECA, including pre-configured GitHub Actions workflows for linting and testing.

## How to Use

1. Click on "Use this template" on the GitHub repository page.
1. Create a new repository using this template.
1. Update `setup.py` and `pyproject.toml` with your project's details.
1. Create a virtual environment for your project:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
1. Install the required dependencies:

   ```
   python -m pip install --upgrade pip
   python -m pip install -r requirements-dev.txt
   ```
1. Install the pre-commit hooks:
   ```
   pre-commit install
   ```
This installs the Git hooks specified in `.pre-commit-config.yaml` and ensures that code formatting and linting checks run before each commit.
1. Start developing your Python package in the `src/` directory.
1. Write tests in the `tests/` directory.
1. Running Tests Locally:
    ```
    python -m pytest
    ```
1. Running Linters and Formatters Locally:
* Black and Isort:
    ```
    python -m black src/ tests/
    python -m isort src/ tests/
    ```
* Pylint:
    ```
    python -m pylint src/ tests/
    ```
1. Ensure Code Quality Before Pushing:
Make sure all tests pass and code adheres to style guidelines before pushing changes.

## Features
* Code Formatting: Enforces consistent code style with Black and Isort.
* Linting: Analyzes code quality using Pylint.
* Testing: Runs tests using Pytest and reports coverage with Coverage.py.
* Pre-commit Hooks: Automates code formatting and linting before commits.
* Continuous Integration: GitHub Actions workflows automate linting and testing on each push and pull request.

## Notes on Pre-commit:
*  Configuration: The `.pre-commit-config.yaml` file contains the configuration for pre-commit hooks.
* Automatic Formatting: When you attempt to commit changes, pre-commit will automatically run Black and Isort. If they make changes, you'll need to add the changes and commit again.
* Skipping Hooks: If necessary, you can skip pre-commit hooks by committing with the --no-verify flag, but this is not recommended.

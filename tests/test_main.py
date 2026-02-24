"""Smoke tests for the template package."""

import python_package


def test_package_imports():
    """The template package should be importable."""
    assert python_package.__version__ == "0.1.0"

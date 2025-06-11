from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import toml
from pytest_cookies.plugin import Cookies, Result

from tests.config import (
    COOKIE_FULL_BAKE,
    COOKIE_MIN_BAKE,
)


def load_pyproject_toml(tmp_path: Path) -> dict[str, Any]:
    """Load and verify that the pyproject.toml file has valid TOML syntax."""
    pyproject_path = tmp_path / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist.")
    with open(pyproject_path, encoding="utf-8") as f:
        try:
            return toml.load(f)
        except Exception as e:
            pytest.fail(f"Invalid TOML syntax in pyproject.toml: {e}")


def verify_pyproject_bake(pyproject: dict[str, Any], recipe: dict[str, str]) -> None:
    """Verify the contents of the pyproject.toml file after baking."""
    if pyproject["project"]["name"] != recipe["project_slug"]:
        pytest.fail(f"Pyproject Error: {recipe['project_slug']} != {pyproject['project']['name']}")

    if pyproject["project"]["version"] != recipe["version"]:
        pytest.fail(f"Pyproject Error: {recipe['version']} != {pyproject['project']['version']}")

    if pyproject["project"]["description"] != recipe["project_description"]:
        pytest.fail(
            f"Pyproject Error: {recipe['project_description']} != {pyproject['project']['description']}"
        )


@pytest.mark.parametrize("recipe", [COOKIE_FULL_BAKE, COOKIE_MIN_BAKE])
def test_cookiecutter(cookies: Cookies, recipe: dict[str, str]) -> None:
    """Test the baking process with different recipes."""
    project_path = bake_recipe(cookies, recipe)
    pyproject = load_pyproject_toml(project_path)
    verify_pyproject_bake(pyproject, recipe)


def bake_recipe(cookies: Cookies, recipe: dict[str, str]) -> Path:
    """Bake a new project from a cookiecutter template.

    Args:
        cookies (Cookies): The pytest-cookies fixture for baking.
        recipe (dict[str, str]): The recipe containing project configuration.

    Returns:
        Path: The path to the baked project.
    """
    result: Result = cookies.bake(extra_context=recipe)
    if result.exit_code:
        pytest.fail(f"Baking failed with exit code {result.exit_code}")

    if result.exception:
        pytest.fail(f"Exception occurred during baking: {result.exception}")

    if result.project_path.name != recipe["project_name"]:
        pytest.fail(f"Unexpected project name: {result.project_path.name}")

    if not result.project_path.is_dir():
        pytest.fail(f"Project path {result.project_path} is not a directory.")

    return result.project_path

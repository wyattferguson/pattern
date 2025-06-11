from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import toml
from pytest_cookies.plugin import Cookies, Result  # type: ignore[import-untyped]

from tests.config import (
    cookie_full_bake,
    cookie_min_bake,
    required_files,
)


@pytest.mark.parametrize("recipe", [cookie_full_bake, cookie_min_bake])
def test_cookiecutter(cookies: Cookies, recipe: dict[str, Any]) -> None:
    """Test the baking process with different recipes."""
    project_path = bake_recipe(cookies, recipe)
    pyproject = load_pyproject_toml(project_path)
    verify_pyproject_bake(pyproject, recipe)
    verify_excluded_files(project_path, recipe["excluded_files"])
    verify_required_files(project_path, recipe["project_slug"])


def verify_excluded_files(project_path: Path, files: list[str]) -> None:
    """Verify that the given files do not exist in the project path."""
    for file in files:
        file_path = project_path / file
        if file_path.exists():
            pytest.fail(f"File should not exist: {file_path}")


def verify_required_files(project_path: Path, project_slug: str) -> None:
    """Verify that the given files exist in the project path."""
    project_files: list[str] = [
        f"src/{project_slug}",
        f"src/{project_slug}/{project_slug}.py",
    ] + required_files
    for file in project_files:
        file_path = project_path / file
        if not file_path.exists():
            pytest.fail(f"File should exist: {file_path}")


def load_pyproject_toml(tmp_path: Path) -> dict[str, Any]:
    """Load and verify that the pyproject.toml file has valid TOML syntax."""
    pyproject_path = tmp_path / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist.")
    with Path.open(pyproject_path, encoding="utf-8") as f:
        try:
            return toml.load(f)
        except Exception as e:
            pytest.fail(f"Invalid TOML syntax in pyproject.toml: {e}")


def verify_pyproject_bake(pyproject: dict[str, Any], recipe: dict[str, Any]) -> None:
    """Verify the contents of the pyproject.toml file after baking."""
    if pyproject["project"]["name"] != recipe["project_slug"]:
        pytest.fail(f"Pyproject Error: {recipe['project_slug']} != {pyproject['project']['name']}")

    if pyproject["project"]["version"] != recipe["version"]:
        pytest.fail(f"Pyproject Error: {recipe['version']} != {pyproject['project']['version']}")

    if pyproject["project"]["description"] != recipe["project_description"]:
        pytest.fail(
            f"Pyproject Error: {recipe['project_description']} "
            f"!= {pyproject['project']['description']}",
        )


def bake_recipe(cookies: Cookies, recipe: dict[str, Any]) -> Path:
    """Bake a new project from a cookiecutter template.

    Args:
        cookies (Cookies): The pytest-cookies fixture for baking.
        recipe (dict[str, Any]): The recipe containing project configuration.

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

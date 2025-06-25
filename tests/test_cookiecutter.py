from __future__ import annotations

import typing
from dataclasses import dataclass
from pathlib import Path

import pytest
import toml
from pytest_cookies.plugin import Cookies, Result  # type: ignore[import-untyped]

from tests.config import (
    Recipe,
    recipes,
    required_files,
)


@dataclass(frozen=True)
class Bake:
    """Represents a baked cookiecutter project."""

    path: Path
    recipe: Recipe


@typing.no_type_check
@pytest.fixture(params=recipes, name="bake")
def cookiecutter_bake(cookies: Cookies, request: pytest.FixtureRequest) -> Bake:
    """Bake a new project from a cookiecutter template.

    Args:
        cookies (Cookies): The pytest-cookies fixture for baking.
        request (pytest.FixtureRequest): The request object for the fixture.

    Returns:
        Bake: A dataclass containing the baked project path and recipe.
    """
    recipe = request.param
    try:
        result: Result = cookies.bake(extra_context=recipe)

        if result.exit_code:
            pytest.fail(f"Baking failed with exit code {result.exit_code}")

        if result.exception:
            pytest.fail(f"Exception occurred during baking: {result.exception}")

        if result.project_path.name != recipe["__clean_name"]:
            pytest.fail(f"Unexpected project name: {result.project_path.name}")

        if not result.project_path.is_dir():
            pytest.fail(f"Project path {result.project_path} is not a directory.")

    except Exception as e:
        pytest.fail(f"Failed to bake project: {e}")

    return Bake(result.project_path, recipe)


def test_excluded_files(bake: Bake) -> None:
    """Verify that the given files do not exist in the project path."""
    excluded_files = bake.recipe["excluded_files"]
    for file in excluded_files:
        file_path = bake.path / file
        if file_path.exists():
            pytest.fail(f"File should not exist: {file_path}")


def test_required_files(bake: Bake) -> None:
    """Verify that the given files exist in the project path."""
    slug = bake.recipe["__clean_slug"]
    files: list[str] = [
        f"src/{slug}",
        f"src/{slug}/{slug}.py",
        *required_files,
    ]
    for file in files:
        file_path = bake.path / file
        if not file_path.exists():
            pytest.fail(f"File should exist: {file_path}")


def test_verify_pyproject(bake: Bake) -> None:
    """Verify the contents of the pyproject.toml file after baking."""
    pyproject_path = bake.path / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist.")
    with Path.open(pyproject_path, encoding="utf-8") as f:
        try:
            pyproject = toml.load(f)

            if pyproject["project"]["name"] != bake.recipe["__clean_slug"]:
                pytest.fail(
                    f"Pyproject Error: {bake.recipe['__clean_slug']} "
                    f"!= {pyproject['project']['name']}",
                )

            if pyproject["project"]["description"] != bake.recipe["project_description"]:
                pytest.fail(
                    f"Pyproject Error: {bake.recipe['project_description']} "
                    f"!= {pyproject['project']['description']}",
                )

        except Exception as e:
            pytest.fail(f"Invalid TOML syntax in pyproject.toml: {e}")

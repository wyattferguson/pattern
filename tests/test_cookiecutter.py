from __future__ import annotations

from pathlib import Path

import pytest
import toml
from pytest_cookies.plugin import Cookies, Result  # type: ignore[import-untyped]

from tests.config import (
    Recipe,
    recipes,
    required_files,
)


@pytest.fixture(params=recipes)
def cookiecutter_bake(cookies: Cookies, request: pytest.FixtureRequest) -> dict[str, Path | Recipe]:
    """Bake a new project from a cookiecutter template.

    Args:
        cookies (Cookies): The pytest-cookies fixture for baking.
        request (pytest.FixtureRequest): The request object for the fixture.

    Returns:
        dict[str, Any]: A dictionary containing the path to the baked project and the recipe.
    """
    recipe = request.param
    result: Result = cookies.bake(extra_context=recipe)

    if not result:
        pytest.fail("Baking failed with no result.")

    if result.exit_code:
        pytest.fail(f"Baking failed with exit code {result.exit_code}")

    if result.exception:
        pytest.fail(f"Exception occurred during baking: {result.exception}")

    if result.project_path.name != recipe["project_name"]:
        pytest.fail(f"Unexpected project name: {result.project_path.name}")

    if not result.project_path.is_dir():
        pytest.fail(f"Project path {result.project_path} is not a directory.")

    return {"path": result.project_path, "recipe": recipe}


def test_excluded_files(
    cookiecutter_bake: dict[str, Path | Recipe],
) -> None:
    """Verify that the given files do not exist in the project path."""
    project_path = cookiecutter_bake["path"]
    excluded_files = cookiecutter_bake["recipe"]["excluded_files"]
    for file in excluded_files:
        file_path = project_path / file
        if file_path.exists():
            pytest.fail(f"File should not exist: {file_path}")


def test_required_files(
    cookiecutter_bake: dict[str, Path | Recipe],
) -> None:
    """Verify that the given files exist in the project path."""
    project_path = cookiecutter_bake["path"]
    project_slug = cookiecutter_bake["recipe"]["project_slug"]
    project_files: list[str] = [
        f"src/{project_slug}",
        f"src/{project_slug}/{project_slug}.py",
        *required_files,
    ]
    for file in project_files:
        file_path = project_path / file
        if not file_path.exists():
            pytest.fail(f"File should exist: {file_path}")


def test_verify_pyproject(
    cookiecutter_bake: dict[str, Path | Recipe],
) -> None:
    """Verify the contents of the pyproject.toml file after baking."""
    pyproject_path = cookiecutter_bake["path"] / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist.")
    with Path.open(pyproject_path, encoding="utf-8") as f:
        try:
            pyproject = toml.load(f)

            if pyproject["project"]["name"] != cookiecutter_bake["recipe"]["project_slug"]:
                pytest.fail(
                    f"Pyproject Error: {cookiecutter_bake['recipe']['project_slug']} "
                    f"!= {pyproject['project']['name']}",
                )

            if pyproject["project"]["version"] != cookiecutter_bake["recipe"]["version"]:
                pytest.fail(
                    f"Pyproject Error: {cookiecutter_bake['recipe']['version']} "
                    f"!= {pyproject['project']['version']}",
                )

            if (
                pyproject["project"]["description"]
                != cookiecutter_bake["recipe"]["project_description"]
            ):
                pytest.fail(
                    f"Pyproject Error: {cookiecutter_bake['recipe']['project_description']} "
                    f"!= {pyproject['project']['description']}",
                )

        except Exception as e:
            pytest.fail(f"Invalid TOML syntax in pyproject.toml: {e}")

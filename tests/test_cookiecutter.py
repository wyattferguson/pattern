from __future__ import annotations

import pytest
import toml

from config import OPTIONAL_FILES, REQUIRED_FILES
from utils import run_within_dir


def test_pyproject_syntax(tmp_path) -> None:
    """Verify that the pyproject.toml file has valid TOML syntax."""
    pyproject_path = tmp_path / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist.")
    with open(pyproject_path, encoding="utf-8") as f:
        try:
            toml.load(f)
        except Exception as e:
            pytest.fail(f"Invalid TOML syntax in pyproject.toml: {e}")


def test_full_bake(cookies, tmp_path: str) -> None:
    """Test the full baking process with a combined set of files.

    Args:
        cookies (_type_): _description_
        tmp_path (str): _description_
    """
    file_list: list[str] = REQUIRED_FILES + OPTIONAL_FILES
    verify_files(cookies, tmp_path, file_list)


def test_minimum_bake(cookies, tmp_path: str) -> None:
    """Test the baking with only the required files.

    Args:
        cookies (_type_): _description_
        tmp_path (str): _description_
    """
    verify_files(cookies, tmp_path, REQUIRED_FILES, OPTIONAL_FILES)


def verify_files(
    cookies, tmp_path: str, files: list[str], excluded_files: list[str] | None = None
) -> None:
    """Verify the presence of given files and folders.

    Args:
        cookies (_type_): _description_
        tmp_path (str): _description_
        file_list (list[str]): _description_
    """
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Verify given files and folders exists
        for file in files:
            file_path = result.project_path / file
            if not file_path.exists():
                pytest.fail(f"Missing required file or folder: {file_path}")

        # Verify that excluded files and folders do not exist
        if excluded_files:
            for file in excluded_files:
                file_path = result.project_path / file
                if file_path.exists():
                    pytest.fail(f"Unexpected file or folder found: {file_path}")

        assert result.exit_code == 0
        assert result.exception is None

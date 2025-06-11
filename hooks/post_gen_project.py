"""Run after cookiecutter to finish environment setup and remove excluded files."""

import os
import shutil
import subprocess
from pathlib import Path


def setup_uv_enviroment() -> None:
    """Set up the UV environment and install dependencies for the project."""
    try:
        subprocess.run(["cd", "{{cookiecutter.project_slug}}"], shell=True, check=False)
        subprocess.run(["uv", "venv"], check=False)
        subprocess.run(["uv", "sync"], check=False)
    except Exception as e:
        print(f"UV Setup Error: {e}")


def remove(filepath: str) -> None:
    """Remove a file or directory.

    Args:
        filepath (str): The path to the file or directory to remove.
    """
    try:
        path = Path(filepath)
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(filepath)
        else:
            print(f"Warning: {filepath} does not exist or is in another directory.")
    except Exception as e:
        print(f"Remove Error ({filepath}): {e}")


def prune_unwanted_files() -> None:
    """Remove unwanted files and directories from the project."""
    if "{{cookiecutter.include_docs}}" != "y":
        remove("docs")
        remove("mkdocs.yml")
        remove(".github/workflows/gh-pages.yml")

    if "{{cookiecutter.include_nox}}" != "y":
        remove("noxfile.py")

    if "{{cookiecutter.include_docker}}" != "y":
        remove("Dockerfile")
        remove(".dockerignore")

    if "{{cookiecutter.include_changelog}}" != "y":
        remove("CHANGELOG.md")

    if "{{cookiecutter.include_contributing_guide}}" != "y":
        remove("CONTRIBUTING.md")

    if "{{cookiecutter.include_code_of_conduct}}" != "y":
        remove("CODE_OF_CONDUCT.md")

    if "{{cookiecutter.pypi_deploy}}" != "y":
        remove(".github/workflows/pypi-publish.yml")


def setup_git() -> None:
    """Initialize a git repository and set up the initial commit."""
    try:
        subprocess.run(["git", "init", "-b", "main"], check=False)
        subprocess.run(["git", "add", "."], check=False)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=False)
    except Exception as e:
        print(f"Git Setup Error: {e}")


if __name__ == "__main__":
    setup_uv_enviroment()
    prune_unwanted_files()
    setup_git()

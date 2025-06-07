"""post_gen_project - Run after cookiecutter project generation."""

import os
import shutil
import subprocess


def setup_uv_enviroment() -> None:
    """Set up the UV environment and install dependencies for the project."""
    try:
        subprocess.run(["cd", "{{cookiecutter.project_slug}}"], shell=True)
        subprocess.run(["uv", "venv"])
        subprocess.run(["uv", "sync"])
    except Exception as e:
        print(f"UV Setup Error: {e}")


def remove(filepath: str) -> None:
    """Remove a file or directory.

    Args:
        filepath (str): The path to the file or directory to remove.
    """
    try:
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
    except Exception as e:
        print(f"Remove Error ({filepath}): {e}")


if __name__ == "__main__":
    if "{{cookiecutter.include_docs}}" != "y":
        remove("docs")
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

    setup_uv_enviroment()

    subprocess.run(["git", "init"])

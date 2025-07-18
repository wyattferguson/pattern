"""Run after cookiecutter to finish environment setup and remove excluded files."""

import shutil
import subprocess
from enum import StrEnum
from pathlib import Path


class Colors(StrEnum):
    """ANSI color codes for terminal output."""

    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def setup_uv_environment() -> None:
    """Set up the UV environment and install dependencies for the project."""
    try:
        subprocess.run(["cd", "{{cookiecutter.project_name}}"], shell=True, check=False)
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

    if "{{cookiecutter.include_nox}}" != "y":
        remove("noxfile.py")

    if "{{cookiecutter.include_docker}}" != "y":
        remove("Dockerfile")
        remove(".dockerignore")

    if "{{cookiecutter.include_changelog}}" != "y":
        remove("CHANGELOG.md")

    if "{{cookiecutter.include_citation}}" != "y":
        remove("CITATION.cff")

    if "{{cookiecutter.include_contributing_guide}}" != "y":
        remove("CONTRIBUTING.md")

    if "{{cookiecutter.include_code_of_conduct}}" != "y":
        remove("CODE_OF_CONDUCT.md")

    if "{{cookiecutter.pypi_deploy}}" != "y":
        remove(".github/workflows/pypi-publish.yml")

    if "{{cookiecutter.include_dbot}}" != "y":
        remove(".github/dependabot.yml")

    if "{{cookiecutter.include_dbot}}" != "y":
        remove(".github/release-drafter.yml")
        remove(".github/workflows/release-publish.yml")
        remove(".github/workflows/release-drafter.yml")


def setup_git() -> None:
    """Initialize a git repository and set up the initial commit."""
    try:
        subprocess.run(["git", "init", "-b", "main"], check=False)
        subprocess.run(["git", "add", "."], check=False)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=False)
    except Exception as e:
        print(f"Git Setup Error: {e}")


def display_project_details() -> None:
    """Display the project details after setup."""
    project_path = Path.cwd()
    print(
        "\n\n###################################################################\n",
    )
    print(f"{Colors.GREEN}Project Setup Complete!{Colors.ENDC}\n")
    print(f"Project Name: {Colors.CYAN}{{cookiecutter.project_name}}{Colors.ENDC}")
    print(
        f"Author: {Colors.CYAN}{{cookiecutter.author}} ({{cookiecutter.email}}){Colors.ENDC}",
    )
    print(f"Project Path: {Colors.CYAN}{project_path}{Colors.ENDC}")
    print(
        f"Git URL: {Colors.CYAN}https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}{Colors.ENDC}",
    )
    if "{{cookiecutter.include_docs}}" == "y":
        print(
            f"Documentation: {Colors.CYAN}https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.repository_name}}{Colors.ENDC}",
        )
    print(f"License: {Colors.CYAN}{{cookiecutter.license}}{Colors.ENDC}")
    print(f"Git Status: {Colors.CYAN}Init Commit{Colors.ENDC}")
    print(f"UV Setup: {Colors.CYAN}Complete{Colors.ENDC}")
    print("\nFor more information, refer to the README.md")
    print("\nHappy coding!")
    print("\n####################################################################\n")


if __name__ == "__main__":
    setup_uv_environment()
    prune_unwanted_files()
    setup_git()
    display_project_details()

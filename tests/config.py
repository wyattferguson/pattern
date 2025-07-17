from random import randint
from typing import TypedDict


class Recipe(TypedDict, total=True):
    """A TypedDict to represent the recipe for a cookiecutter project."""

    project_name: str
    project_slug: str
    __clean_name: str
    __clean_slug: str
    repository_name: str
    project_description: str
    author: str
    github_username: str
    email: str
    license: str
    development_status: str
    typechecker: str
    include_docs: str
    include_nox: str
    include_dbot: str
    include_changelog: str
    include_citation: str
    include_contributing_guide: str
    include_code_of_conduct: str
    include_docker: str
    pypi_deploy: str
    excluded_files: list[str]


cookie_full_bake: Recipe = {
    "project_name": f"test_full_bake ID{randint(1000, 9999)}",
    "project_slug": "test_full_bake",
    "__clean_name": "test-full-bake",
    "__clean_slug": "test_full_bake",
    "repository_name": "test-full-bake",
    "project_description": "A great project that does cool things.",
    "author": "Wyatt Ferguson",
    "github_username": "wyattferguson",
    "email": "wyattxdev@duck.com",
    "license": "MIT",
    "development_status": "Development Status :: 4 - Beta",
    "typechecker": "mypy",
    "include_docs": "y",
    "include_nox": "y",
    "include_dbot": "y",
    "include_changelog": "y",
    "include_citation": "y",
    "include_contributing_guide": "y",
    "include_code_of_conduct": "y",
    "include_docker": "y",
    "pypi_deploy": "y",
    "excluded_files": [],
}

cookie_min_bake: Recipe = {
    "project_name": f"Test Minimum Bake ID{randint(1000, 9999)}",
    "project_slug": "test_min_bake",
    "__clean_name": "test-min-bake",
    "__clean_slug": "test_min_bake",
    "repository_name": "test-min-bake",
    "project_description": "A great project that does cool things.",
    "author": "Wyatt Ferguson",
    "github_username": "wyattferguson",
    "email": "wyattxdev@duck.com",
    "license": "MIT",
    "development_status": "Development Status :: 2 - Pre-Alpha",
    "typechecker": "ty",
    "include_docs": "n",
    "include_nox": "n",
    "include_dbot": "n",
    "include_changelog": "n",
    "include_citation": "n",
    "include_contributing_guide": "n",
    "include_code_of_conduct": "n",
    "include_docker": "n",
    "pypi_deploy": "n",
    "excluded_files": [
        "docs",
        "noxfile.py",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "Dockerfile",
        ".dockerignore",
        ".github/dependabot.yml",
        ".github/workflows/pypi-deploy.yml",
        ".github/workflows/gh-pages.yml",
        ".github/workflows/release-drafter.yml",
        ".github/release-drafter.yml",
        ".github/workflows/release-publish.yml",
    ],
}

recipes: list[Recipe] = [cookie_full_bake, cookie_min_bake]

required_files: list[str] = [
    "pyproject.toml",
    "README.md",
    "src",
    "LICENSE",
    ".vscode/settings.json",
    ".vscode/extensions.json",
    ".gitignore",
    ".pre-commit-hooks.yaml",
]

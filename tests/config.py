from random import randint
from typing import Any

cookie_full_bake: dict[str, Any] = {
    "project_name": f"test_full_bake ID{randint(1000, 9999)}",
    "project_slug": "test_full_bake",
    "project_description": "A great project that does cool things.",
    "author": "Wyatt Ferguson",
    "github_username": "wyattferguson",
    "email": "wyattxdev@duck.com",
    "license": "MIT license",
    "version": "0.1.2",
    "development_status": "Development Status :: 4 - Beta",
    "typechecker": "mypy",
    "include_docs": "y",
    "include_nox": "y",
    "include_changelog": "y",
    "include_contributing_guide": "y",
    "include_code_of_conduct": "y",
    "include_docker": "y",
    "pypi_deploy": "y",
    "excluded_files": [],
}

cookie_min_bake: dict[str, Any] = {
    "project_name": f"Test Minimum Bake ID{randint(1000, 9999)}",
    "project_slug": "test_min_bake",
    "project_description": "A great project that does cool things.",
    "author": "Wyatt Ferguson",
    "github_username": "wyattferguson",
    "email": "wyattxdev@duck.com",
    "license": "Mozilla Public License v2.0",
    "version": "3.14.15",
    "development_status": "Development Status :: 2 - Pre-Alpha",
    "typechecker": "ty",
    "include_docs": "n",
    "include_nox": "n",
    "include_changelog": "n",
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
        ".github/workflows/pypi-deploy.yml",
    ],
}

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

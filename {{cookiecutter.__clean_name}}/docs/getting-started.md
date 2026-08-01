# Getting Started

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) 0.11+ (Python is managed automatically by uv)

## Installation

```bash
uv sync
```

This creates a virtual environment (`.venv`) and installs the package in editable mode along with all dev dependencies.

## Available Tasks

Tasks are managed with [taskipy](https://github.com/illBeRoy/taskipy):

| Task            | Description                                  |
| --------------- | -------------------------------------------- |
| `task format`   | Format code with Ruff                        |
| `task lint`     | Lint and auto-fix with Ruff                  |
| `task type`     | Typecheck with ty                            |
| `task tests`    | Run the test suite with pytest               |
| `task coverage` | Run tests and report coverage (100% gate)    |
| `task docs`     | Build documentation with Zensical            |
| `task serve`    | Serve documentation locally                  |
| `task upgrade`  | Upgrade all dependencies with uv             |
| `task release`  | Create a release with python-semantic-release |

## Project Layout

```text
src/
  {{ cookiecutter.__clean_slug }}/
    __init__.py
    {{ cookiecutter.__clean_slug }}.py
tests/
  test_{{ cookiecutter.__clean_slug }}.py
.github/
  workflows/       # CI, docs, and release automation
```

## Quality Gates

Every pull request runs CI that checks, in order:

1. PR title follows [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, ...)
2. Ruff lint (`ruff check`) and format (`ruff format --check`)
3. Type checking (`ty check`)
4. Tests (`pytest -n auto`) and coverage (`coverage report` with `fail_under = 100`)
5. Dependency vulnerability audit (`uv audit`)

## Releasing

Pushes to `main` with conventional commit messages trigger [python-semantic-release](https://python-semantic-release.readthedocs.io/), which:

1. Bumps the version in `pyproject.toml` based on commit history
2. Updates `CHANGELOG.md`
3. Creates and pushes a `v*.*.*` tag

The tag then triggers the release workflow, which builds the package, generates [PEP 740 attestations](https://peps.python.org/pep-0740/), and publishes to PyPI via Trusted Publishing — no API tokens required.

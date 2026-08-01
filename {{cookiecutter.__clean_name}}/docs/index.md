# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- Modern Python packaging with [uv](https://docs.astral.sh/uv/) and the `uv_build` backend
- Fully typed with [ty](https://docs.astral.sh/ty/) (strict)
- Ruff for linting and formatting (all rules enabled)
- 100% test coverage enforcement with [coverage.py](https://coverage.readthedocs.io/)
- Parallel, randomized, property-based tests (pytest-xdist, pytest-randomly, Hypothesis)
- Pre-commit hooks including `actionlint`, `zizmor`, and `codespell`
- Automated releases with [python-semantic-release](https://python-semantic-release.readthedocs.io/)
- PyPI publishing with Trusted Publishing + PEP 740 attestations
- Documentation built with [Zensical](https://zensical.org/docs/) and deployed to GitHub Pages
- Docker multi-stage build, optional Nox matrix, and a full GitHub issue template suite

## Quick Start

```bash
uv sync            # install dependencies
task tests         # run the test suite
task coverage      # run tests with coverage
task type          # typecheck with ty
task docs          # build documentation
```

See [Getting Started](getting-started.md) for details.

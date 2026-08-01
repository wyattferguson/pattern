# :rocket: {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup Dev Environment

Installation is using [UV](https://docs.astral.sh/uv/) to manage everything.

**Step 1**: Create a virtual environment

```bash
uv venv
```

**Step 2**: Activate your new environment

```bash
# on windows
.venv\Scripts\activate

# on mac / linux
source .venv/bin/activate
```

**Step 3**: Install all the cool dependencies

```bash
uv sync
```

## Github Repo Setup

To add your new project to its Github repository, firstly make sure you have created a project named **{{cookiecutter.repository_name}}** on Github.
Follow these steps to push your new project.

```bash
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}.git
git branch -M main
git push -u origin main
```

## Built-in CLI Commands

We've included a bunch of useful CLI commands for common project tasks using [taskipy](https://github.com/taskipy/taskipy).

```bash
# run src/{{cookiecutter.__clean_slug}}/{{cookiecutter.__clean_slug}}.py
task run

# run all tests
task tests

# run test coverage and generate report
task coverage

# typechecking with Ty
task type

# ruff linting
task lint

# format with ruff
task format

# build/serve docs
task docs
task serve
```

{%- if cookiecutter.include_docker == 'y' %}

## Docker Setup

A Dockerfile optimized to reduce the image size has been included. To get it up and running follow these steps.

**Step 1**: Build your Docker image.

```bash
task dbuild
```

**Step 2**: Run your new image.

```bash
task drun
```

{%- endif %}

{%- if cookiecutter.pypi_deploy == 'y' %}

## PyPI Deployment

This project uses [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) — no API tokens required.

1. On [PyPI](https://pypi.org/), open your project's settings and add a trusted publisher for this repository:
   - Workflow name: `pypi-publish.yml`
   - Environment: `pypi`
   - Repository: `<owner>/{{cookiecutter.repository_name}}`
2. Push commits to `main` — [python-semantic-release](https://python-semantic-release.readthedocs.io/) bumps the version, updates the changelog, and creates a `v*.*.*` tag automatically.
3. The tag triggers the publish workflow, which builds the package, generates [PEP 740 attestations](https://peps.python.org/pep-0740/), and uploads to PyPI.

{%- endif %}

{%- if cookiecutter.include_docs== 'y' %}

## Docs Generation + Publishing

Documentation is built with [Zensical](https://zensical.org/docs/) — a modern, actively maintained drop-in replacement for MkDocs Material.

Doc generation scans everything inside `/src`, files with a prefix `_` will be ignored. Basic doc functions for generating and serving can be done through these CLI commands:

```bash
# build docs (outputs to ./site/)
task docs

# serve docs locally
 task serve
```

Publishing to GitHub Pages is automatic: every push to `main` runs the `.github/workflows/docs.yml` workflow, which builds and deploys the site.

Note: Your repo must be public or have an upgraded account to deploy docs to Github Pages.

{%- endif %}

{%- if cookiecutter.include_dbot == 'y' %}

## Dependabot Setup

1. Go to the "Settings -> Advanced Security" tab in your repository.
2. Under the "Dependabot" section enable the options you want to monitor, we recommend the "Dependabot security updates" at the minimum.

Dependabot is configured to do _weekly_ scans of your dependencies, and pull requests will be prefixed with "DBOT". These settings can be adjusted in the `./.github/dependabot.yml` file.

{%- endif %}

## References

- [Pattern](https://github.com/wyattferguson/pattern) - A modern cookiecutter template for your next Python project.

## License

{{cookiecutter.license}}

## Contact

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github_username}})

# :rocket: {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup Dev Enviroment

Installation is using [UV](https://docs.astral.sh/uv/) to manage everything.

**Step 1**: Create a virtual enviroment

```
uv venv
```

**Step 2**: Activate your new enviroment

```
# on windows
.venv\Scripts\activate

# on mac / linux
source .venv/bin/activate
```

**Step 3**: Install all the cool dependancies

```
uv sync
```

## Github Repo Setup

To add your new project to its Github repository, firstly make sure you have created a project named **{{cookiecutter.repository_name}}** on Github.
Follow these steps to push your new project.

```
cd {{cookiecutter.__clean_name}}
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}.git
git branch -M main
git push -u origin main
```

## CLI Commands

We've included a bunch of useful CLI commands for common project tasks using [taskipy](https://github.com/taskipy/taskipy).

```
# run src/{{cookiecutter.__clean_slug}}/{{cookiecutter.__clean_slug}}.py
task run

# run all tests
task tests

{%- if cookiecutter.include_nox == 'y' %}
# run tests with multiple python versions (3.13,3.12,3.11,3.10)
task nox
{%- endif %}

# run test coverage and generate report
task coverage

# typechecking with Ty or Mypy
task type

# ruff linting
task lint

# format with ruff
task format
```

{%- if cookiecutter.pypi_deploy == 'y' %}

## PyPI Deployment

- Register your project and create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN`
- Create a new release on Github.
- Create a new tag in the form `*.*.*`.

{%- endif %}

{%- if cookiecutter.include_docs== 'y' %}

## Docs Build + Publishing

Your basic doc functions for creating, serving, and deploying can be done through these CLI commands:

```
# generate docs & serve
task docs

# serve docs
task serve

# generate static HTML docs (outputs to ./site/)
task html

# deploy docks to github.io
task doc_deploy
```

Note: Your repo must be public or have an upgraded account to deploy docs to Github Pages.

{%- endif %}

## License

{{cookiecutter.license}}

## Contact

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github_username}})

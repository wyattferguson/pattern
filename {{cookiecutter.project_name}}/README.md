# :rocket: {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup Dev Enviroment

Installation is using [UV](https://docs.astral.sh/uv/) to manage everything.

To get it all running from scratch:

```
# create a virtual enviroment
uv venv

# install all the cool dependancies
uv sync
```

## Github Repo Setup

To add your new project to its Github repository, firstly make sure you have created a project named _{{cookiecutter.project_slug}}_ on Github.
Follow these steps to push your new project.

```
cd "{{cookiecutter.project_name}}"
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
git push -u origin main
```

## CLI Commands

We've included a bunch of useful CLI commands for common project tasks using [taskipy](https://github.com/taskipy/taskipy).

```
# run src/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py
task run

# run all tests
task tests

# run test coverage and generate report
task coverage

# typechecking with Ty or Mypy
task type

# ruff linting
task lint

# format with ruff
task format
```

{% if cookiecutter.include_nox == 'y' %}

## Nox

```
# run tests with multiple python versions (3.13,3.12,3.11,3.10)
nox -s vtests
```

{%- endif %}

{% if cookiecutter.pypi_deploy == 'y' %}

## PyPI Deployment

- Register your project and create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN`
- Create a new release on Github.
- Create a new tag in the form `*.*.*`.

{%- endif %}

{% if cookiecutter.include_docs== 'y' -%}

## Docs Build + Publishing

Your basic doc functions for creating, serving, and deploying can be done through these CLI commands:

```
# generate docs & serve
task docs

# serve docs
task serve

# deploy docks to github.io
task doc_deploy
```

{%- endif %}

## License

{{cookiecutter.license}}

## Contact + Support

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github_username}})

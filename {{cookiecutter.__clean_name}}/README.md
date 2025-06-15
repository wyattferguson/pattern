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
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}.git
git branch -M main
git push -u origin main
```

## Built-in CLI Commands

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

{%- if cookiecutter.include_docker == 'y' %}

## Docker Setup

A Dockerfile optimized to reduce the image size has been included. To get it up and running follow these steps.

**Step 1**: Build your Docker image.

```
docker build -t "{{cookiecutter.__clean_slug}}:Dockerfile" .
```

**Step 2**: Run your new image.

```
docker run -d {{cookiecutter.__clean_slug}}
```

{%- endif %}

{%- if cookiecutter.pypi_deploy == 'y' %}

## PyPI Deployment

1. Register your project and create an API Token on [PyPI](https://pypi.org/).
2. Add the API Token to your projects secrets with the name `PYPI_TOKEN`
3. Create a new release on Github.
4. Create a new tag in the form `*.*.*`.

{%- endif %}

{%- if cookiecutter.include_docs== 'y' %}

## Docs Generation + Publishing

Your basic doc functions for creating, serving, and deploying can be done through these CLI commands:

```
# generate docs & serve
task docs

# serve docs
task serve

# generate static HTML docs (outputs to ./site/)
task html

# publish docs to Github Pages
task publish
```

Note: Your repo must be public or have an upgraded account to deploy docs to Github Pages.

{%- endif %}

## License

{{cookiecutter.license}}

## Contact

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github_username}})

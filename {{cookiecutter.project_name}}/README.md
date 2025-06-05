# :rocket: {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup Dev Enviroment

Installation is using [UV](https://docs.astral.sh/uv/) to manage everything.

To get it all running from scratch:

```
# create a virtual enviroment
uv venv

# activate virtual enviroment
.venv\Scripts\activate

# install all the cool dependancies
uv sync
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

# ty typechecking
task typecheck

# ruff linting
task lint

# format with ruff
task format

# generate docs & serve
task docs
```

{% if cookiecutter.pypi_deploy == 'y' %}

## PyPI Deployment

- Register your project and create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN`
- Create a new release on Github.
- Create a new tag in the form `*.*.*`.

{%- endif %}

{% if cookiecutter.include_docs== 'y' -%}

## Docs Build + Publishing

{%- endif %}

## License

{{cookiecutter.license}}

## Contact + Support

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github}})

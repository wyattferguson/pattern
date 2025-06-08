# :rocket: {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

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

```
# run {{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.py
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

## License

{{cookiecutter.license}}

## Contact + Support

Created by [{{cookiecutter.author}}](https://github.com/{{cookiecutter.github_username}})

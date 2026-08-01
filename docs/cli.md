# 🍭 CLI

## Built-in Commands

Included with your setup is a comprehensive collection of built-in commands to cover your basic needs. All of these commands use [Taskipy] to simplify commands and give you one simple path to interacting with your app.

```bash
# run src/project_name/project_name.py
task run

# run all tests
task tests

# run tests with multiple python versions (3.13,3.14)
task nox

# run test coverage and generate report
task coverage

# typechecking with Ty
task type

# ruff linting
task lint

# format with ruff
task format

# build docs (outputs to ./site/)
task docs

# serve docs
task serve

# create a release (version bump + changelog + tag)
task release

# upgrade all dependencies to latest versions
task upgrade

# build Docker image
task dbuild

# run Docker image
task drun
```

Also you can use the command `task --list` to see a complete list with helper text.

## Adding Your Own Commands

To add your own commands goto the `[tool.taskipy.tasks]` section in your `pyproject.toml` file. Heres an example of adding a task to run Black:

```toml
[tool.taskipy.tasks]
black = "black path/to/my_module"

# Alternatively you can add some helper text but its optional
black = { cmd = "black path/to/my_module", help = "Format my_module with Black" }
```

To execute that command simply run:

```bash
task black
```

## References

- [Taskipy Documentation](https://github.com/taskipy/taskipy)

[Taskipy]: https://github.com/taskipy/taskipy

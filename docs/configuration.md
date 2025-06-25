# 🍧 Configuration

All of your config settings can be found in the `pyproject.toml` file.

## Ruff Rules

[Ruff] is included by default with your setup to cover all your linting and formatting needs. We've tried to pick a reasonable set of rules to follow, and some to ignore. We try and walk the line between a good dev experience and keeping code quality high.

```toml
# pyproject.toml

[tool.ruff]
line-length = 100
indent-width = 4
format.indent-style = "space"
target-version = "py313"
src = ["src", "tests"]

[tool.ruff.lint]
pydocstyle.convention = "google"
fixable = ["ALL"]
select = ["ALL"]
ignore = [
    "FA102", # Flake8-future-annotations
    "F401", # Disable fix for unused imports
    "B904", # Allow raising exceptions without from e
    "PLR0913", # too many arguments
    "CPY", # Flake8-copyright
    "T201", # Debugging print statements
    "ERA", # Eradicate – detects commented-out code
    "BLE001", # Catch-all exceptions
    "D100", # missing docstring in public module
    "D105", # undocumented magic method
    "D107", # undocumented public init
    "D203", # incorrect-blank-line-before-class
    "D205", # line-between-summary-and-description
    "D212", # multi-line-summary-first-line
    "D400", # missing-trailing-period
    "D407", # missing-dashed-underline-after-section
    "S311", # rand-usage
]
```

Checkout the [Ruff Rules Docs] to see all the posible rules you have at your finger tips.

## Typechecking Rules

On setup you have a choice of two typecheckers the stable [Mypy] and the up and coming [Ty]. Whatever you choose the settings can be found in the `pyproject.toml` file.

[Ty] default settings:

```toml
[tool.ty]
src.root = "./src"
environment.python = "./.venv"
terminal.output-format = "concise"
```

[Mypy] default settings:

```toml
files = ["src", "tests"]
ignore_missing_imports = true
disallow_untyped_defs = true
disallow_any_unimported = false
no_implicit_optional = true
check_untyped_defs = true
warn_return_any = false
warn_unused_ignores = true
show_error_codes = true
```

## References

- [Ruff Documentation](https://astral.sh/ruff)
- [Mypy Documentation](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [Ty Documentation](https://github.com/astral-sh/ty)

[Mypy]: https://mypy.readthedocs.io/en/stable/getting_started.html
[Ty]: https://github.com/astral-sh/ty
[Ruff]: https://astral.sh/ruff
[Ruff Rules Docs]: https://docs.astral.sh/ruff/rules/

# 🍧 Configuration

All of your config settings can be found in the `pyproject.toml` file.

## Ruff Rules

[Ruff] is included by default with your setup to cover all your linting and formatting needs. We've tried to pick a reasonable set of rules to follow, and some to ignore. We try and walk the line between a good dev experience and keeping code quality high.

```toml
# pyproject.toml

[tool.ruff]
line-length = 100
indent-width = 4
target-version = "py313"
exclude = [
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "build",
    "dist",
    "*.egg-info",
    "htmlcov",
    ".cache",
]
src = ["src", "tests"]

[tool.ruff.lint]
pydocstyle.convention = "google"
fixable = ["ALL"]
select = ["ALL"]
ignore = [
    "FA102",    # Flake8-future-annotations
    "F401",     # Disable fix for unused imports
    "B904",     # Allow raising exceptions without from e
    "PLR0913",  # too many arguments
    "CPY",      # Flake8-copyright
    "T201",     # Debugging print statements
    "ERA",      # Eradicate – detects commented-out code
    "BLE001",   # Catch-all exceptions
    "D100",     # missing docstring in public module
    "D105",     # undocumented magic method
    "D107",     # undocumented public init
    "D203",     # incorrect-blank-line-before-class
    "D205",     # line-between-summary-and-description
    "D212",     # multi-line-summary-first-line
    "D400",     # missing-trailing-period
    "D407",     # missing-dashed-underline-after-section
    "S311",     # rand-usage
    "EM102",    # f-string-exception
    "TRY003",   # long-exception-messages
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = [
    "PLC0415",  # Import outside top-level (tests often need scoped imports)
    "PLR2004",  # Magic values
    "F841",     # Unused variable (fixtures, etc.)
    "PT001",    # Use @pytest.fixture() over @pytest.fixture
    "S101",     # Use of assert detected
    "D101",     # Missing docstring in public class
    "D103",     # Missing docstring in public function
    "E741",     # Ambiguous variable name 'l', 'O', or 'I'
]
```

Checkout the [Ruff Rules Docs] to see all the possible rules you have at your finger tips.

## Typechecking Rules

On setup [Ty] is used for typechecking. Settings can be found in the `pyproject.toml` file.

[Ty] default settings:

```toml
[tool.ty]
terminal.output-format = "full"

[tool.ty.environment]
python = ".venv"

[tool.ty.src]
include = ["src/**/*.py"]

```

## Dependency Auditing

Supply-chain safety is handled with `uv audit`, which scans the resolved dependency tree for known vulnerabilities and is wired into the CI pipeline and the release workflow.

```bash
uv audit
```

## References

- [Ruff Documentation](https://astral.sh/ruff)
- [Ty Documentation](https://github.com/astral-sh/ty)

[Ty]: https://github.com/astral-sh/ty
[Ruff]: https://astral.sh/ruff
[Ruff Rules Docs]: https://docs.astral.sh/ruff/rules/

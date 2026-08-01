# 🧪 Testing

We've included [PyTest] and [Coverage] to give you a good base to build your testing from.

## PyTest

[PyTest] is the gold standard for testing your code in Python and is included by default in your install. A starter test file is generated for you on install, along with a few batteries-included plugins:

- [pytest-xdist] - runs your tests in parallel (`-n auto`)
- [pytest-randomly] - shuffles test order to catch hidden interdependencies
- [hypothesis] - property-based testing
- [pytest-timeout] - fails tests that exceed the 60s per-test limit

To run all your tests we have included this handy command:

```bash
task tests
```

[PyTest] has a huge number of options and integrations, we highly recommend you check out [PyTest Documentation](https://docs.pytest.org/en/stable/).

## Coverage

[Coverage] is included by default for every install. It works hand-in-hand with [PyTest] and measures how much of code is covered by your tests.

All settings for [Coverage] are located in your `pyproject.toml`. Here are the included defaults:

```toml
[tool.coverage.report]
# Skip files that have no executable code
skip_empty = true

# Show line numbers of code that wasn't executed.
show_missing = true

# Show test failure, when coverage is under 100%
fail_under = 100

# Don't count the ``if __name__ == "__main__"`` guard against coverage
# (it's never exercised by tests, and excluding it keeps 100% reachable)
exclude_also = [
    "if __name__ == .__main__.:",
]

[tool.coverage.run]
# Measure branch coverage as well as statement coverage
branch = true

# Only measure coverage of the src/ package
source = ["src"]
```

To run a coverage test we have a built-in command to generate your report:

```bash
task coverage
```

[Coverage] has a huge amount of config options and types of reports it can generate. Visit the [Coverage Documentation](https://coverage.readthedocs.io/en/7.9.1/) for more information.

> [!note]
> Multi-version testing is handled by the CI pipeline, which runs the test
> suite on Python 3.13 and 3.14 (see `.github/workflows/pull-request.yml`).
> Locally you can test a specific version with `uv run --python 3.14 pytest`.

## References

- [PyTest Documentation](https://docs.pytest.org/en/stable/)
- [Coverage Documentation](https://coverage.readthedocs.io/en)
- [pytest-xdist](https://pytest-xdist.readthedocs.io/)
- [pytest-randomly](https://pypi.org/project/pytest-randomly/)
- [Hypothesis](https://hypothesis.readthedocs.io/)
- [pytest-timeout](https://pypi.org/project/pytest-timeout/)

[PyTest]: https://docs.pytest.org/en/stable/
[Coverage]: https://coverage.readthedocs.io/en

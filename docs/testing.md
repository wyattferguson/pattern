# 🧪 Testing

We've included [PyTest], [Coverage], and [Nox] to give you a good base to build your testing from.

## PyTest

[PyTest] is the gold standard for testing your code in Python and is included by default in your install. A empty test file is generated for you on install.

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
```

To run a coverage test we have a built-in command to generate your report:

```bash
task coverage
```

[Coverage] has a huge amount of config options and types of reports it can generate. Visit the [Coverage Documentation](https://coverage.readthedocs.io/en/7.9.1/) for more information.

## Nox

[Nox] is a very useful tool for running any array of tests across different Python environments and is included as an optional install.

Include in our project `noxfile.py` is a basic script to run all your pytest tests against the most modern versions of Python. If you want to modify what versions it runs against you will find the list below in the file and simply tack it on to the list.

```toml
python_versions = ["3.10", "3.11", "3.12", "3.13"]
```

To run all your [Nox] scripts at once use the command:

```bash
task nox
```

## References

- [Nox Documentation](https://nox.thea.codes/en/stable/config.html)
- [PyTest Documentation](https://docs.pytest.org/en/stable/)
- [Coverage Documentation](https://coverage.readthedocs.io/en)

[Nox]: https://nox.thea.codes/en/stable/index.html
[PyTest]: https://docs.pytest.org/en/stable/
[Coverage]: https://coverage.readthedocs.io/en

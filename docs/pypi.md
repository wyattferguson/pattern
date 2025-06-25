# 📡 PyPI

A GitHub Action for publishing your package to [PyPI] it can be found at `.github/workflows/pypi-publish.yml`.

## Package Publishing

1. Register your project and create an API Token on [PyPI].
2. Add the API Token to your projects secrets with the name `PYPI_TOKEN`
3. Create a new release on Github.
4. Create a new tag in the form `*.*.*`.

## PyPI Testing

PyPI has a [test package publishing index](https://test.pypi.org/) for you to work through any kinks before you go live.

## References

- [PyPI]
- [PyPI Testing](https://test.pypi.org/)
- [GitHub Actions Guide](https://docs.github.com/en/actions/writing-workflows/quickstart)

[PyPI]: https://pypi.org
[GitHub Action]: https://docs.github.com/en/actions/writing-workflows/quickstart

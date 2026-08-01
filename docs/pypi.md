# 📡 PyPI

Publishing your package to [PyPI] is handled by `.github/workflows/pypi-publish.yml`,
which combines automated release management with Trusted Publishing — no API tokens required.

## How Releases Work

1. Push commits to `main` with [Conventional Commits](https://www.conventionalcommits.org/)
   messages (`feat:`, `fix:`, ...).
2. [python-semantic-release](https://python-semantic-release.readthedocs.io/)
   determines the next version, updates `pyproject.toml` and `CHANGELOG.md`, and
   creates a `v*.*.*` tag.
3. The tag triggers the publish workflow, which builds the package, generates
   [PEP 740 attestations](https://peps.python.org/pep-0740/), and uploads it to
   PyPI via Trusted Publishing. A GitHub Release with the built artifacts is
   created automatically.

## One-Time Setup: Trusted Publishing

1. On [PyPI], open your project and go to **Publishing**.
2. Click **Add a new trusted publisher** and fill in:
   - Workflow name: `pypi-publish.yml`
   - Environment: `pypi`
   - Repository: `<owner>/<repository>`
3. Done — no `PYPI_TOKEN` secret needed. OIDC handles authentication.

> [!note]
> If you prefer an API token instead, set the `PYPI_TOKEN` secret and it will
> be used as a fallback by `uv publish`.

## PyPI Testing

PyPI has a [test package publishing index](https://test.pypi.org/) for you to work through any kinks before you go live. Point the publish job at it with:

```bash
uv publish --publish-url https://test.pypi.org/legacy/
```

## References

- [PyPI]
- [Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [PyPI Testing](https://test.pypi.org/)
- [python-semantic-release](https://python-semantic-release.readthedocs.io/)
- [GitHub Actions Guide](https://docs.github.com/en/actions/writing-workflows/quickstart)

[PyPI]: https://pypi.org

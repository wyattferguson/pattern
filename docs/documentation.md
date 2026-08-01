# 📼 Documentation

All your documentation needs are handled by [Zensical] — a modern, actively
maintained drop-in replacement for the MkDocs Material stack.

## Generating Docs

The content of your docs comes from the Markdown files in `/docs` plus the
docstrings inside your `.py` files. Here is an example function:

```python
def divide(a:int, b:int) -> float:
    """Divide two numbers.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Raises:
        ZeroDivisionError: If the denominator is zero.

    Returns:
        float: The result of the division.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return result
```

Doc generation scans everything inside `/src`; files with a prefix `_` are
ignored. So `_config.py` would be skipped when generating the docs.

Built-in CLI commands are included for generating and previewing your docs:

```bash
# build docs (outputs to ./site/)
task docs

# serve docs locally with hot reload
task serve
```

## Publishing Docs

> [!note]
> Your repo must be public or have an upgraded account to deploy docs to Github Pages.

Publishing to GitHub Pages is fully automatic. Every push to `main` triggers
the `.github/workflows/docs.yml` workflow, which builds the site and deploys
it with the official Pages actions — no credentials or extra setup required.

## Adding Static Pages

Add a `.md` file to the `docs` directory and register it in the `nav` section
of `mkdocs.yml` at the project root. It will then be included in the build.

## Themes

The theme is configured in `mkdocs.yml` at the project root. The default
settings are:

```yaml
theme:
  name: material
  palette:
    scheme: slate
    primary: deep purple
    accent: purple
```

To add custom css, create a file like `docs/css/extra.css` and reference it:

```yaml
extra_css:
  - css/extra.css
```

> [!note]
> [Zensical] is compatible with all [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes).

## References

- [GitHub Pages]
- [Zensical Documentation](https://zensical.org/docs/)
- [MkDocs Guide](https://www.mkdocs.org/user-guide/configuration/)

[GitHub Pages]: https://pages.github.com/
[Zensical]: https://zensical.org/

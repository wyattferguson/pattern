# 📼 Documentation

All your documentation needs are handled by [Portray] it acts as a layer over entrenched docs tools like pdocs and MkDocs to simply a lot of the most common functions.

## Generating Docs

The content of your docs will be generated from the doc strings inside your `.py` files. Here is an example function:

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

[Portray] is setup to scan everything inside `/src`, files with a prefix `_` will be ignored. So `_config.py` would be skipped when generating the docs.

Built-in CLI commands are included for generating, and previewing your docs:

```bash
# generate docs & serve
task docs

# serve docs
task serve

# generate static HTML docs (outputs to ./site/)
task html
```

## Publishing Docs

> [!note]
> Your repo must be public or have an upgraded account to deploy docs to Github Pages.

Using [Portray] publishing your docs to [GitHub Pages] couldn't be any easier. Make sure all your changes are synced to your repo and run the provided command:

```bash
task publish
```

## Adding Static Pages

To add a static page to your docs, create a `.md` file in the `docs` directory and it will be automatically included. If you want to add folders, or organize your docs in a certain way take a look at the [Portray Examples](https://timothycrosley.github.io/portray/docs/quick_start/4.-configuration/).

## Themes

You can modify the color scheme, primary, and accent color inside your `pyproject.toml`. The default settings are:

```toml
[tool.portray.mkdocs.theme]
name = "material"
custom_dir = "docs"
palette = {scheme= "slate", primary="deep purple", accent="purple"}
```

To add custom css to your docs, add the `extra_css` field to your `pyproject.toml` settings. Note that `extra_css` bases out of the `docs` folder. Heres an example

```toml
[tool.portray.mkdocs]
# points to /docs/css/extra.css
extra_css = ["css/extra.css"]
```

> [!note]
> [Portray] is compatible with all [Mkdocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes).

## References

- [GitHub Pages]
- [Portray Documentation](https://timothycrosley.github.io/portray/)
- [MKDocs Guide](https://www.mkdocs.org/user-guide/configuration/)

[GitHub Pages]: https://pages.github.com/
[Portray]: https://timothycrosley.github.io/portray/

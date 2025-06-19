# 📼 Documentation

All your documentation needs are handled by [Portray] it acts as a layer over entrenched docs tools like pdocs and MkDocs to simply alot of the most common functions.

## Generating Docs

[Portray] is setup to scan everything inside `/src`, files with a prefix `_` will be ignored.

Basic functions for generating, and previewing are included:

```
# generate docs & serve
task docs

# serve docs
task serve

# generate static HTML docs (outputs to ./site/)
task html
```

## Publishing Docs

Using [Portray] publishing your docs to [GitHub Pages] couldnt be any easier. Make sure all your changes are synced to your repo and run the provided command:

```
task publish
```

**_Note: Your repo must be public or have an upgraded account to deploy docs to Github Pages._**

## Adding Static Pages

To add a static page to your docs, create a `.md` file in the `docs` directory and it will be automatically included. If you want to add folders, or organize your docs in a certain way take a look at the [Portray Examples](https://timothycrosley.github.io/portray/docs/quick_start/4.-configuration/).

## Theming

You can modify the color scheme, primary, and accent color inside your `pyprojec.toml`. The default settings are:

```
[tool.portray.mkdocs.theme]
name = "material"
custom_dir = "docs"
palette = {scheme= "slate", primary="deep purple", accent="purple"}
```

To add custom css to your docs, add the `extra_css` field to your `pyproject.toml` settings. Note that `extra_css` bases out of the `docs` folder. Heres an example

```
[tool.portray.mkdocs]
# points to /docs/css/extra.css
extra_css = ["css/extra.css"]
```

[Portray] is compatible with all [Mkdocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes).

[GitHub Pages]: (https://pages.github.com/)
[Portray]: (https://timothycrosley.github.io/portray/)

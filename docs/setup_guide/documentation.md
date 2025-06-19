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

## Themeing

[GitHub Pages]: (https://pages.github.com/)
[Portray]: (https://timothycrosley.github.io/portray/)

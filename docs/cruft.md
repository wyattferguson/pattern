# 🚚 Cruft

[Cruft] allows you to maintain all the necessary boilerplate for packaging and building projects separate from the code you intentionally write. As fixes, updates, and changes are pushed to the underlying Cookiecutter project, [Cruft] makes is super easy to keep you up to date.

## Setup a New Project

Creating a new project with [Cruft] is super simple:

```bash
uvx cruft create gh:wyattferguson/pattern
```

Then just follow the prompts, pick the tools you want to install, and watch the magic happen.

## Installation

To install [Cruft] globally on your system use this command:

```bash
uv tool install cruft
```

## Linking Existing Project

If you have a project that you created without [Cruft] and now want to get updates. Run this command to link your project:

```bash
cruft link gh:wyattferguson/pattern
```

## Updating a Project

Updating your project is a breeze with these commands:

```bash

# Check if update is needed
cruft check

# Run update
cruft update
```

## References

- [Cruft Documentation](https://cruft.github.io/cruft/)
- [Cookiecutter](https://www.cookiecutter.io/)

[Cruft]: https://cruft.github.io/cruft/

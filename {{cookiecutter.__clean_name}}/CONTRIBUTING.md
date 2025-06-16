# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the {{cookiecutter.license}} and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the [Issue Tracker].

## How to set up your development environment

You need Python 3.12+ and [uv](https://docs.astral.sh/uv/):

Create a new virtual enviroment:

```
uv venv
```

Activate your new enviroment:

```
# on windows
.venv\Scripts\activate

# on mac / linux
source .venv/bin/activate
```

Install the package with development requirements:

```
$ uv sync
```

To run the project from the main entry point:

```
$ task run
```

## How to test the project

Run the full test suite:

```
$ task tests
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest](https://pytest.readthedocs.io/) testing framework.

## How to submit changes

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

[source code]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}

{%- if cookiecutter.include_docs == 'y' %}
[documentation]: "https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.repository_name}}"
{%- else %}
[documentation]: "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}"
{%- endif %}
[issue tracker]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/issues
[pull request]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}/pulls
[code of conduct]: CODE_OF_CONDUCT.md

# 🤖 Github

## Issue Templates

Form templates have been included for common GitHub issues: _Bug Reports, Feature Requests, General Feedback, and Documentation_.
All of these can be found in the `.github/ISSUE_TEMPLATE/` folder. They use the modern [YAML form format](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms), so contributors get structured forms with required fields out of the box. A pull request template is also included at `.github/pull_request_template.md`.

## Dependabot

[Dependabot] provides automatic security and version updates, along with dependency alerts, to keep your app secure and up-to-date.
Dependabot is configured to do _weekly_ scans of your Python dependencies (via the uv ecosystem) and your Docker base images. PRs are grouped and prefixed with `deps` / `docker`. These settings can be adjusted in the `.github/dependabot.yml` file.

### Setup Guide

To setup [Dependabot] scans for your project follow these steps:

1. Go to the "Settings -> Code security and analysis" tab in your repository.
2. Under the "Dependabot" section enable the options you want to monitor, we recommend "Dependabot security updates" at the minimum.

## Pull Request Title Enforcement

[action-semantic-pull-request] makes sure every pull request to your repo is prefixed with a proper type: _feat, fix, docs, style, refactor, perf, test, build, ci, revert, deps_ — the same convention [python-semantic-release](https://python-semantic-release.readthedocs.io/) uses to derive versions. The settings for this action can be found in `.github/workflows/pull-request.yml`.

## CI Pipeline

Every push and pull request runs the CI workflow (`.github/workflows/pull-request.yml`), which checks:

1. PR title follows [Conventional Commits](https://www.conventionalcommits.org/)
2. Ruff linting (`ruff check`) and formatting (`ruff format --check`)
3. Type checking with ty
4. Tests with pytest across Python 3.13 and 3.14, plus a 100% coverage gate
5. Dependency vulnerability scan with `uv audit`
6. Workflow security audit with [zizmor](https://zizmor.sh/)

## Pre Commit Hooks

Pre commit hooks are included in the `.pre-commit-config.yaml` file, these are scripts that run before your git commit to ensure code quality, security, and standards are enforced before they get committed to your repo.

### GitHub

The included [GitHub Pre Commit Hooks](https://github.com/pre-commit/pre-commit-hooks) ensure valid config files, some simple formatting clean up, and any potential conflicts.

```yaml
hooks:
  - id: check-case-conflict
  - id: check-merge-conflict
  - id: end-of-file-fixer
  - id: trailing-whitespace
  - id: check-yaml
  - id: check-toml
  - id: check-json
```

### Ruff

Ruff has their own [pre commit hooks](https://github.com/astral-sh/ruff-pre-commit) we've included, to enforce formatting consistency on every commit.

```yaml
hooks:
  - id: ruff-check
    args: [--fix, --config, pyproject.toml]
  - id: ruff-format
    args: [--config, pyproject.toml]
```

### Codespell

[codespell] catches common spelling mistakes in your code, comments, and docs before they land.

```yaml
hooks:
  - id: codespell
    args: ["--skip=uv.lock,CHANGELOG.md"]
```

### uv-lock

The [uv pre-commit hooks](https://github.com/astral-sh/uv-pre-commit) keep your `uv.lock` file in sync with `pyproject.toml` by failing the commit if the lockfile is out of date.

```yaml
hooks:
  - id: uv-lock
```

### actionlint

[actionlint] lints your GitHub Actions workflows, catching misconfigurations and expression errors.

```yaml
hooks:
  - id: actionlint
```

## References

- [GitHub Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Dependabot Quickstart Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pre Commit Hooks](https://github.com/pre-commit/pre-commit-hooks)
- [actionlint](https://github.com/rhysd/actionlint)
- [codespell](https://github.com/codespell-project/codespell)
- [zizmor](https://zizmor.sh/)

[Dependabot]: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide
[action-semantic-pull-request]: https://github.com/amannn/action-semantic-pull-request
[actionlint]: https://github.com/rhysd/actionlint
[codespell]: https://github.com/codespell-project/codespell

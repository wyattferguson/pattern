# 🤖 Github

## Issues Templates

Templates have been included for common GitHub issues: _Bug Reports, Feature Requests, General Feedback, Documentation, and Pull Requests_.
All of these can be found in the `.github/` folder. All these templates are good to go out of the box and should cover most usecases but can be easily customized. Check out the [GitHub Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests) for more details.

## Dependabot

[Dependabot] provides automatic security and version updates, along with dependency alerts, to keep your app secure and up-to-date.
Dependabot is configured to do _weekly_ scans of your dependencies, and pull requests will be prefixed with "DBOT". These settings can be adjusted in the `.github/dependabot.yml` file.

### Setup Guide

To setup [Dependabot] scans for your project follow these steps:

1. Go to the "Settings -> Advanced Security" tab in your repository.
2. Under the "Dependabot" section enable the options you want to monitor, we recommend the "Dependabot security updates" at the minimum.

## Pull Request Title Enforcer

[Pull Request Title Enforcer] makes sure every pull request to your repo is prefixed with a proper type: _feat, fix, docs, style, refactor, perf, test, build, ci, revert, deps_. The settings for this action can be found `.github/workflows/pull-requests.yml`

## Pre Commit Hooks

Pre commit hooks are included in the `.pre-commit-hooks.yaml` file, these are scripts that run before your git commit to ensure code quality, security, and standards are enforced before they get committed to your repo.

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

Ruff has there own [pre commit hooks](https://github.com/astral-sh/ruff-pre-commit) we've included, to enforce formatting consitency on every commit.

```yaml
hooks:
  - id: ruff-check
    args: [--fix --config=pyproject.toml]
  - id: ruff-format
    args: [--config=pyproject.toml]
```

## References

- [GitHub Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Dependabot Quickstart Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pre Commit Hooks](https://github.com/pre-commit/pre-commit-hooks)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

[Dependabot]: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide
[GitHub Actions]: https://docs.github.com/en/actions
[Release Drafter]: https://github.com/release-drafter/release-drafter
[Pull Request Title Enforcer]: https://github.com/marketplace/actions/pull-request-title-naming-rules

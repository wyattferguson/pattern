# 🤖 Github

## Issues Templates

Templates have been included for common GitHub issues: _Bug Reports, Feature Requests, General Feedback, Documentation, and Pull Requests_.
All of these can be found in the `.github/` folder. All these templates are good to go out of the box and should cover most usecases but can be easily customized. Check out the [GitHub Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests) for more details.

## Dependabot Setup

[Dependabot] provides automatic security and version updates, along with dependency alerts, to keep your app secure and up-to-date.

To setup [Dependabot] scans for your project follow these steps:

1. Go to the "Settings -> Advanced Security" tab in your repository.
2. Under the "Dependabot" section enable the options you want to monitor, we recommend the "Dependabot security updates" at the minimum.

Dependabot is configured to do _weekly_ scans of your dependencies, and pull requests will be prefixed with "DBOT". These settings can be adjusted in the `.github/dependabot.yml` file.

## Github Actions

### Release Drafter

### Pull Request Title Enforcer

## Pre Commit Hooks

## References

- [GitHub Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [Dependabot Quickstart Guide](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

[Dependabot]: https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide

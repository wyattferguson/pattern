import os
import platform
import subprocess
from pathlib import Path

import pytest
import toml
import yaml

# dependencies
# pyyaml
# cookiecutter
# pytest
# toml

COOKIECUTTER_DIR = Path(__file__).parent.parent
CONFIG_FILENAME = COOKIECUTTER_DIR / "tests" / "cookiecutter_test_configs.yaml"


def create_test_configs(create_docs):
    """
    Dynamically create the config file for each test,
    to test different settings.

    NOTE:
        Need to be very careful with input to lists.
        If the option is not one of default options in the
        cookiecutter list, it will silently fail and just
        use the defaults.
    """
    test_dict = {
        "default_context": {
            "full_name": "Test Cookiecutter",
            "email": "testing@cookiecutter.com",
            "github_username_or_organization": "test_cookiecutter_username",
            "package_name": "test-cookiecutter",
            "github_repository_url": "https://github.com/"
            "{{cookiecutter.github_username_or_organization}}/"
            "{{cookiecutter.package_name}}",
            "module_name": "test_cookiecutter_module",
            "short_description": "Lets Test CookieCutter",
            "license": "MIT",
            "create_docs": "yes" if create_docs else "no",
        },
    }
    with open(CONFIG_FILENAME, "w") as config_file:
        yaml.dump(test_dict, config_file, sort_keys=False)

    return test_dict["default_context"]


def load_pyproject_toml(package_path):
    """
    Load the pyproject.toml file from the
    created cookiecutter to check.
    """
    pyproject_path = package_path / "pyproject.toml"
    project_toml = toml.load(pyproject_path.as_posix())
    return project_toml


def run_cookiecutter():
    """
    Run the cookiecutter to create the test
    project folder
    """
    subprocess.run(
        f"cookiecutter {COOKIECUTTER_DIR} --config-file {CONFIG_FILENAME} --no-input",
        shell=True,
    )


@pytest.fixture(scope="function")
def package_path_config_dict(tmp_path):
    """
    Fixture to build a cookiecutter project
    """
    config_dict = create_test_configs(create_docs=False)

    os.chdir(tmp_path)

    run_cookiecutter()

    package_path = tmp_path / config_dict["package_name"]

    return package_path, config_dict


@pytest.fixture(scope="function")
def pip_install(package_path_config_dict):
    """
    Fixture to build a cookiecutter project and
    install with pip
    """
    package_path, config_dict = package_path_config_dict

    uninstall_cmd = f"pip uninstall -y {config_dict['package_name']}"
    dev_formatting = ".[dev]" if platform.system() == "Windows" else "'.[dev]'"
    install_cmd = f"pip install -e {dev_formatting}"

    # Installs the package using pip
    os.chdir(package_path)

    # Uninstall and check package not installed
    subprocess.run("git init", shell=True)

    subprocess.run(uninstall_cmd, shell=True)
    result = subprocess.Popen(
        f"pip show {config_dict['package_name']}",
        shell=True,
        stderr=subprocess.PIPE,
    )
    __, stderr = result.communicate()
    assert f"WARNING: Package(s) not found: {config_dict['package_name']}" in stderr.decode("utf8")

    # Install package
    subprocess.run(install_cmd, shell=True)
    yield config_dict

    # Uninstall package
    subprocess.run(uninstall_cmd, shell=True)


def test_directory_names(package_path_config_dict):
    """
    Check that all expected directories are present
    in the created cookiecutter project
    """
    package_path = package_path_config_dict[0]

    assert package_path.exists()

    expected = [
        # Files
        ".github",
        ".gitignore",
        ".pre-commit-config.yaml",
        "LICENSE",
        "MANIFEST.in",
        "pyproject.toml",
        "README.md",
        Path("test_cookiecutter_module") / "__init__.py",
        # Directories
        "test_cookiecutter_module",
        "tests",
    ]

    for f in expected:
        assert (package_path / f).exists()


def test_docs(package_path_config_dict):
    """
    Test that all files and configurations related
    to creating docs in the cookiecutter are
    set properly. First, check they are
    not set when docs are not created.
    Then, make a new cookiecutter project
    with docs and check all expected configs are there.

    NOTE:
        This assumes docs are not created by
        default in the fixture. So, the tests
        to check when creating a project
        with docs must come second.
    """
    package_path, config_dict = package_path_config_dict

    for true_if_create_docs in [False, True]:
        import shutil

        if true_if_create_docs:
            config_dict = create_test_configs(create_docs=True)
            shutil.rmtree(package_path)
            run_cookiecutter()

        assert (
            package_path / ".github/workflows/docs_build_and_deploy.yml"
        ).exists() is true_if_create_docs
        assert (package_path / "docs").exists() is true_if_create_docs
        assert (
            package_path / f"{config_dict['module_name']}/greetings.py"
        ).exists() is true_if_create_docs
        assert (
            package_path / f"{config_dict['module_name']}/math.py"
        ).exists() is true_if_create_docs

        with open(package_path / ".pre-commit-config.yaml") as file:
            line = file.read().splitlines()[0]

        assert line == "exclude: 'conf.py'" if true_if_create_docs else line == ""

        project_toml = load_pyproject_toml(package_path)

        assert (
            "github.io" in project_toml["project"]["urls"]["Documentation"]
        ) is true_if_create_docs


def test_pyproject_toml(package_path_config_dict):
    """
    Check that all entries in the pyproject.toml
    of the created cookiecutter project match
    these settings specified (in --config-file)
    """
    package_path, config_dict = package_path_config_dict

    project_toml = load_pyproject_toml(package_path)

    assert project_toml["project"]["name"] == config_dict["package_name"]

    # some of these are hard coded from the cookiecutter
    # pyproject.toml has not asked user for
    assert project_toml["project"]["authors"][0]["name"] == config_dict["full_name"]
    assert project_toml["project"]["authors"][0]["email"] == config_dict["email"]
    assert project_toml["project"]["description"] == "Lets Test CookieCutter"
    assert project_toml["project"]["readme"] == "README.md"
    assert project_toml["project"]["requires-python"] == ">=3.11.0"
    assert (
        project_toml["project"]["license"]["text"] == "MIT"
    )  # parameterize this? test if url not given?

    assert project_toml["project"]["classifiers"] == [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]

    test_repo_url = (
        f"https://github.com/"
        f"{config_dict['github_username_or_organization']}/"
        f"{config_dict['package_name']}"
    )

    assert project_toml["project"]["urls"]["Homepage"] == test_repo_url

    assert project_toml["project"]["urls"]["Bug Tracker"] == test_repo_url + "/issues"

    assert project_toml["project"]["urls"]["Source Code"] == test_repo_url
    assert project_toml["project"]["urls"]["User Support"] == test_repo_url + "/issues"

    assert len(project_toml["project"]["optional-dependencies"].keys()) == 1

    assert project_toml["project"]["optional-dependencies"]["dev"] == [
        "pytest",
        "pytest-cov",
        "coverage",
        "tox",
        "mypy",
        "pre-commit",
        "ruff",
        "setuptools-scm",
    ]

    assert project_toml["build-system"]["requires"] == [
        "setuptools>=64",
        "wheel",
        "setuptools-scm[toml]>=8",
    ]

    assert project_toml["build-system"]["build-backend"] == "setuptools.build_meta"

    assert project_toml["tool"]["setuptools"]["packages"]["find"]["include"] == [
        config_dict["module_name"] + "*"
    ]

    assert (
        project_toml["tool"]["pytest"]["ini_options"]["addopts"]
        == f"--cov={config_dict['module_name']}"
    )
    assert project_toml["tool"]["ruff"]

    assert "legacy_tox_ini" in project_toml["tool"]["tox"]

    assert project_toml["tool"]["codespell"]["skip"] == ".git"
    assert project_toml["tool"]["codespell"]["check-hidden"] is True


def test_pip_install(pip_install):
    config_dict = pip_install

    result = subprocess.Popen(
        f"pip show {config_dict['package_name']}",
        shell=True,
        stdout=subprocess.PIPE,
    )
    stdout, __ = result.communicate()

    # Home-page is not in pip show output...
    show_details = stdout.decode("utf8")
    assert "Name: test-cookiecutter" in show_details
    assert "Version: 0.1.dev0" in show_details
    assert "Summary: Lets Test CookieCutter" in show_details
    assert "Author-email: Test Cookiecutter <testing@cookiecutter.com>" in show_details
    assert "License: MIT" in show_details

"""
post_gen_project - Run after project generation.
- Setup UV venv and install dependencies.
- Remove docs and tests folders if not needed.
"""

import os
import shutil
import subprocess


def setup_uv_enviroment() -> bool:
    step: int = 0
    try:
        # (Step: 0) change directory to project folder
        subprocess.run(["cd", "{{cookiecutter.project_slug}}"], shell=True)

        # (Step: 1) create enviroment
        subprocess.run(["uv", "venv"])
        step += 1

        # (Step: 2) activate enviroment with bash shortcut
        subprocess.run(".venv\\Scripts\\activate", shell=True)
        step += 1

        # (Step: 3) install dependencies
        subprocess.run(["uv", "sync"])
        return True
    except Exception as e:
        print(f"ERROR (Step:{step}): {e}")
        return False


def remove(filepath: str) -> None:
    try:
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
    except Exception as e:
        print(f"ERROR (Remove {filepath}): {e}")


if __name__ == "__main__":
    create_docs = "{{cookiecutter.include_docs}}" == "y"
    create_tests = "{{cookiecutter.include_tests}}" == "y"
    uv_setup = "{{cookiecutter.uv_setup}}" == "y"
    pypi_deploy = "{{cookiecutter.pypi_deploy}}" == "y"

    if not create_docs:
        remove("docs")
        remove(".github/workflows/gh-pages.yml")

    if not create_tests:
        remove("tests")

    if uv_setup:
        setup_uv_enviroment()

    if not pypi_deploy:
        remove(".github/workflows/pypi-publish.yml")

    subprocess.run(["git", "init"])

import nox

nox.options.default_venv_backend = "uv"

python_versions = ["3.13", "3.14"]


@nox.session(name="tests", python=python_versions, reuse_venv=False)
def run_tests(session: nox.Session) -> None:
    """Run all pytest tests in the /tests/ folder."""
    session.run("uv", "sync", "--active")
    session.run("pytest", "-s", "tests/")

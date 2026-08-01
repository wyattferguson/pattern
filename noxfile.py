import nox

nox.options.default_venv_backend = "uv"


@nox.session(name="tests", python=["3.13", "3.14"], reuse_venv=False)
def run_tests(session: nox.Session) -> None:
    """Run all pytest tests."""
    session.run("uv", "sync", "--active")
    session.run("pytest", "-s", "tests/")

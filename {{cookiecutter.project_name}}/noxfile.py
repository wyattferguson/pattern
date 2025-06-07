import nox

nox.options.default_venv_backend = "uv"


@nox.session(
    name="vtests",
    python=["3.13", "3.12", "3.11", "3.10"],
    reuse_venv=True,
)
def version_test(session):
    """Run python version tests.

    Args:
        session (nox.Session): The nox session object.
    """
    session.install("pytest")
    session.run("pytest")

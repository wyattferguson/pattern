import nox


# nox -s test
@nox.session(
    python=["3.13", "3.12", "3.11", "3.10"],
    venv_backend="uv",
    reuse_venv=True,
)
def test(session):
    session.run("pytest")

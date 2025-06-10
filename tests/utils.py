import os
from contextlib import contextmanager


@contextmanager
def run_within_dir(path: str):
    """Run a block of code within a specific directory.

    Args:
        path (str): The directory path to change to.
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

"""Tests for {{cookiecutter.__clean_slug}}."""

import pytest

from {{cookiecutter.__clean_slug}}.{{cookiecutter.__clean_slug}} import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify the main entry point prints a greeting."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out

import os
from pathlib import Path
import pytest

from modules.frontend_path import FrontendPath


def test_get_frontend_path_when_path_is_empty_then_returns_cwd_plus_frontend():
    # Arrange
    expected_path = Path(
        "{0}/{1}".format(os.getcwd(), FrontendPath.PROJECT_DIR))

    # Act
    result = FrontendPath().get_frontend_path()

    # Assert
    assert result == expected_path


def test_get_frontend_path_when_path_is_not_empty_then_returns_path_plus_frontend(tmp_path: Path):
    # Arrange
    expected_path = tmp_path / FrontendPath.PROJECT_DIR

    # Act
    result = FrontendPath().get_frontend_path(tmp_path)

    # Assert
    assert result == expected_path

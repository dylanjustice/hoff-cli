from distutils import file_util
import os
from pathlib import Path
import subprocess
from unittest import mock
from unittest.mock import MagicMock
from models.result import Result
from modules.webpack_publish import WebpackPublish

_sut = WebpackPublish()


def test_run_when_restore_is_false_and_build_succeeds_then_returns_success(tmp_path: Path):
    # Arrange
    frontend_path: Path = tmp_path / "frontend"
    package_json: Path = frontend_path / "package.json"
    frontend_path.mkdir(parents=True, exist_ok=True)
    package_json.touch()

    os.chdir(tmp_path)
    # Mock npm run build
    subprocess.run = MagicMock(
        return_value=subprocess.CompletedProcess(mock.ANY, 0))

    # Act
    result = _sut.run(restore=False)

    # Assert
    assert result.hasError() == False


def test_run_when_restore_is_false_and_package_json_not_found_then_returns_error(tmp_path: Path):
    # Arrange
    frontend_path: Path = tmp_path / "frontend"
    package_json: Path = frontend_path / "package.json"
    frontend_path.mkdir(parents=True, exist_ok=True)
    package_json.touch()
    os.chdir(tmp_path)
    subprocess.run = MagicMock(
        return_value=subprocess.CompletedProcess(mock.ANY, 1))

    # Act
    result = _sut.run(restore=False)

    # Assert
    assert result.hasError() == True

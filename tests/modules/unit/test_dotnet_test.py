import os
from pathlib import Path
from subprocess import CompletedProcess
import subprocess
from unittest import mock
from unittest.mock import MagicMock
import pytest
from modules.dotnet_test import DotnetTest


def test_dotnet_test_when_solution_file_not_found_then_returns_error():
    # Arrange and Act
    result = DotnetTest().run(filter=None, coverage=False)

    # Assert
    assert result.hasError() == True
    assert result.message == DotnetTest.ERR_NOT_FOUND


def test_when_solution_file_exists_given_no_options_then_calls_dotnet_cli(tmp_path: Path):
    # Arrange
    sln_file_path = tmp_path / "My.sln"
    sln_file_path.touch()
    os.chdir(tmp_path)
    subprocess.run = MagicMock(
        return_value=CompletedProcess(mock.ANY, returncode=0))

    # Act
    result = DotnetTest().run(filter=None, coverage=False)

    # Assert
    assert result.hasError() == False
    subprocess.run.assert_called_once()


def test_when_subprocess_fails_then_returns_basic_error(tmp_path: Path):
    # Arrange
    sln_file_path = tmp_path / "My.sln"
    sln_file_path.touch()
    os.chdir(tmp_path)
    subprocess.run = MagicMock(
        return_value=CompletedProcess(mock.ANY, returncode=1))

    # Act
    result = DotnetTest().run(filter=None, coverage=False)

    # Assert
    assert result.hasError() == True
    assert result.message == DotnetTest.ERR_TEST_FAILED

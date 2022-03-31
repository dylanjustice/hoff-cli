import os
from pathlib import Path
import subprocess
from unittest import mock
from unittest.mock import MagicMock
from modules.webpack_run import WebpackRun


def test_run_given_defaults_then_npm_run_start_called(tmp_path: Path):
    # Arrange:
    frontend_path = tmp_path / "frontend"
    frontend_path.mkdir(parents=True, exist_ok=True)
    os.chdir(tmp_path)
    subprocess.run = MagicMock(
        return_value=subprocess.CompletedProcess(mock.ANY, returncode=0))
    # Act:
    result = WebpackRun().run(clean=False, restore=False)

    # Assert:
    assert result.hasError() == False

def test_run_given_defaults_when_path_not_found_then_returns_error():
    # Arrange:

    # Act:
    result = WebpackRun().run(clean=False, restore=False)

    # Assert:
    assert result.hasError() == True
    assert isinstance(result.error, FileNotFoundError)

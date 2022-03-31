import os
from pathlib import Path
import subprocess
from unittest import mock
from unittest.mock import MagicMock
from modules.node_restore import NodeRestore


def test_run_when_path_exists_then_returns_without_error(tmp_path: Path):
    # Arrange

    subprocess.run = MagicMock(
        return_value=subprocess.CompletedProcess(mock.ANY, returncode=0))

    # Act
    result = NodeRestore().run(path=tmp_path.as_posix())

    # Assert
    assert result.hasError() == False


def test_run_when_subprocess_returns_error_then_returns_error(tmp_path: Path):
    # Arrange

    subprocess.run = MagicMock(
        return_value=subprocess.CompletedProcess(mock.ANY, returncode=1))

    # Act
    result = NodeRestore().run(path=tmp_path.as_posix())

    # Assert
    assert result.hasError() == True
    assert result.message == NodeRestore.ERR_UNEXPECTED

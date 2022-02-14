from click.testing import CliRunner
from commands.dotnet import dotnet
from models.result import Result
from pytest import MonkeyPatch

from modules.dotnet_run import DotnetRun


def test_when_dotnet_called_given_no_arguments_then_returns_help():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(dotnet)

    # Assert
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_when_dotnet_called_given_info_arg_then_returns_0():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(dotnet, ["info"])

    # Assert
    assert result.exit_code == 0


def test_when_dotnet_called_given_sdks_arg_then_returns_0():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(dotnet, ["sdks"])

    # Assert
    assert result.exit_code == 0


def test_when_dotnet_called_given_runtimes_arg_then_returns_0():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(dotnet, ["runtimes"])

    # Assert
    assert result.exit_code == 0


def test_when_dotnet_called_given_run_arg_then_runs_dotnet_project(monkeypatch: MonkeyPatch):
    # Arrange
    runner = CliRunner()

    monkeypatch.setattr(DotnetRun, "run", lambda: Result(status_code=0))

    # Act
    result = runner.invoke(dotnet, ["run"])

    # Assert
    assert result.exit_code == 0

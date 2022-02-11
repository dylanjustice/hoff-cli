import hoff
from click.testing import CliRunner


def test_when_hoff_called_given_no_arguments_then_returns_help():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(hoff.main)

    # Assert
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_when_hoff_called_given_version_arg_then_returns_version():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(hoff.main, ["version"])

    # Assert
    assert result.exit_code == 0
    assert "version" in result.output

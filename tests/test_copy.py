from click.testing import CliRunner
from commands.copy import copy



def test_when_copy_called_given_no_arguments_then_returns_error():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(copy)

    # Assert
    assert result.exit_code == 2
    assert "Usage" in result.output
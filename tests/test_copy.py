from genericpath import exists
from pathlib import Path
from click.testing import CliRunner
from faker import Faker
from commands.copy import copy

def test_when_copy_called_given_no_arguments_then_returns_error():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(copy)

    # Assert
    assert result.exit_code == 2
    assert "Usage" in result.output

def test_when_copy_called_with_missing_argument_then_returns_destination_error():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(copy, ["temp"])

    # Assert
    assert result.exit_code == 2
    assert "Missing argument 'DESTINATION'" in result.output

def test_when_source_and_destination_exist_then_copy_succesful(tmp_path: Path, faker: Faker):
    # Arrange
    runner = CliRunner()

    source_depth = faker.random_digit()
    dest_depth = faker.random_digit()

    source: Path = tmp_path / faker.file_path(depth=source_depth)
    dest: Path = tmp_path / faker.file_path(depth=dest_depth)

    source.mkdir(parents=True, exist_ok=True)
    dest.mkdir(parents=True, exist_ok=True)

    source_file_name = faker.file_name()
    source_file_path: Path = source / source_file_name
    source_file_path.touch()


    # Act
    result = runner.invoke(copy, [source_file_path.as_posix(), dest.as_posix()])

    # Assert
    assert result.exit_code == 0
    assert exists(dest / source_file_name) == True
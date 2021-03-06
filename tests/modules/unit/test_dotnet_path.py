# region Setup

# endregion Setup

from os import chdir
from pathlib import Path

import pytest
from faker import Faker
from faker.providers import file
from modules.dotnet_path import DotnetPath

# region Setup

Faker.seed()
fake = Faker()

_sut = DotnetPath()

# endregion Setup

# region solution_path


@pytest.mark.parametrize(
    argnames=["path", "file"],
    argvalues=[
        ["dotnet", "Api.sln"],
        ["dotnet/api", "Api.sln"],
        ["", "Api.sln"],
        ["dotnet/Cli", "Cli.sln"]
    ])
def test_solution_path_when_sln_file_exists_then_returns_file_path(tmp_path: Path, path: str, file: str):
    # Arrange
    dotnet_path = tmp_path / path
    dotnet_path.mkdir(parents=True, exist_ok=True)
    sln_file_path = dotnet_path / file
    sln_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.solution_path()

    # Assert
    assert result == str(sln_file_path.relative_to(tmp_path))


def test_solution_path_when_files_is_empty_then_returns_None(tmp_path: Path):
    # Arrange
    dotnet_path = tmp_path / fake.file_path(depth=2)
    dotnet_path.mkdir(parents=True, exist_ok=True)
    sln_file_path = dotnet_path / fake.file_name()
    sln_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.solution_path()

    # Assert
    assert result is None

# endregion solution_path

# region solution_dir


@pytest.mark.parametrize(
    argnames=["path", "file"],
    argvalues=[
        ["dotnet", "Api.sln"],
        ["dotnet/api", "Api.sln"],
        ["", "Api.sln"],
        ["dotnet/Cli", "Cli.sln"]
    ])
def test_solution_dir_when_sln_file_exists_then_returns_file_path(tmp_path: Path, path: str, file: str):
    # Arrange
    dotnet_path = tmp_path / path
    dotnet_path.mkdir(parents=True, exist_ok=True)
    sln_file_path = dotnet_path / file
    sln_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.solution_dir()

    # Assert
    assert result == str(Path(path)).replace(
        ".", "")  # Replace relative annotation


def test_solution_dir_when_files_is_empty_then_returns_None(tmp_path: Path):
    # Arrange
    dotnet_path = tmp_path / fake.file_path(depth=2)
    dotnet_path.mkdir(parents=True, exist_ok=True)
    sln_file_path = dotnet_path / fake.file_name()
    sln_file_path.touch()
    chdir(dotnet_path)

    # Act
    result = _sut.solution_dir()

    # Assert
    assert result is None

# endregion solution_dir

# region web_project_file_path


@pytest.mark.parametrize(
    argnames=["path", "file"],
    argvalues=[
        ["dotnet", "Web.csproj"],
        ["dotnet/api/Presentation/Web", "Web.csproj"],
        ["", "Random.csproj"],
        ["random", "Web.csproj"]
    ])
def test_web_project_file_path_when_sln_file_exists_then_returns_file_path(tmp_path: Path, path: str, file: str):
    # Arrange
    dotnet_path = tmp_path / path
    dotnet_path.mkdir(parents=True, exist_ok=True)
    proj_file_path = dotnet_path / file
    proj_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.web_project_file_path()

    # Assert
    assert result == str(proj_file_path.relative_to(tmp_path))


def test_web_project_file_path_when_files_is_empty_then_returns_None(tmp_path: Path):
    # Arrange
    dotnet_path = tmp_path / fake.file_path(depth=2)
    dotnet_path.mkdir(parents=True, exist_ok=True)
    proj_file_path = dotnet_path / fake.file_name()
    proj_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.web_project_file_path()

    # Assert
    assert result is None

# endregion web_project_file_path

# region web_project_dir


@pytest.mark.parametrize(
    argnames=["path", "file"],
    argvalues=[
        ["dotnet", "Web.csproj"],
        ["dotnet/api/Presentation/Web", "Web.csproj"],
        ["", "Random.csproj"],
        ["random", "Web.csproj"]
    ])
def test_web_project_file_path_when_sln_file_exists_then_returns_file_path(tmp_path: Path, path: str, file: str):
    # Arrange
    dotnet_path = tmp_path / path
    dotnet_path.mkdir(parents=True, exist_ok=True)
    proj_file_path = dotnet_path / file
    proj_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.web_project_dir()

    # Assert
    assert result == str(dotnet_path.relative_to(tmp_path)).replace(".", "")


def test_web_project_file_path_when_files_is_empty_then_returns_None(tmp_path: Path):
    # Arrange
    dotnet_path = tmp_path / fake.file_path(depth=2)
    dotnet_path.mkdir(parents=True, exist_ok=True)
    proj_file_path = dotnet_path / fake.file_name()
    proj_file_path.touch()
    chdir(tmp_path)

    # Act
    result = _sut.web_project_dir()

    # Assert
    assert result is None

# endregion web_project_dir

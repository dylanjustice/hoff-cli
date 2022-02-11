# import subprocess
# from unicodedata import name
# import pytest
# from pathlib import Path
# from modules.dotnet_clean import dotnet_clean
# from faker import Faker

# from modules.echo import success

# #region Private Properties

# path = "dotnet_test"
# fake = Faker()

# #endregion Private Properties

# #region Setup


# @pytest.fixture
# def dotnet_sln_directory(tmp_path: Path) -> str:
#     tmp_path = Path(tmp_path.as_posix())
#     dotnet_dir = tmp_path.joinpath(path)
#     proj_dir = dotnet_dir.joinpath("Core")
#     bin_dir = proj_dir.joinpath("bin")
#     obj_dir = proj_dir.joinpath("obj")

#     directories: list(Path) = [
#         dotnet_dir,
#         proj_dir,
#         bin_dir,
#         obj_dir
#     ]

#     for directory in directories:
#         directory.mkdir()

#     sln_file = dotnet_dir / "MySln.sln"
#     bin_file = bin_dir / "Mydll.dll"
#     obj_file = obj_dir / "MyObj.dll"

#     files = [sln_file, bin_file, obj_file]
#     for file in files:
#         file.touch()
#         file.write_text(fake.text())

#     return dotnet_dir.as_posix()

# class MockCompletedProcess:
#     @staticmethod
#     def success():
#         return subprocess.CompletedProcess(["dotnet", "clean"], 0)

# #endregion Setup

# #region Tests

# def test_dotnet_clean_when_solution_file_exists_then_returns_0(dotnet_sln_directory, monkeypatch:pytest.MonkeyPatch):
#     # Arrange
#     monkeypatch.setattr(target=subprocess, name="run", value=success)

#     # Act
#     result = dotnet_clean(dotnet_sln_directory)

#     # Assert
#     assert result == 0

# #endregion Tests

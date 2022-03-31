from genericpath import exists
import os
from pathlib import Path
from re import sub
import shutil
from tkinter.tix import Tree

from faker import Faker

from modules.node_clean import NodeClean

tmp_path = Path("tmp")


def test_run_when_node_modules_does_not_exist_then_returns_without_error(tmp_path: Path):
    # Arrange & Act
    result = NodeClean().run(path=tmp_path)

    # Assert
    assert result.hasError() == False

def test_run_removes_directory_and_returns_without_error(tmp_path: Path):
    # Arrange
    fake = Faker()
    Faker.seed(20)
    node_modules = tmp_path / "node_modules"
    node_modules.mkdir()
    count = fake.random_int(min=2, max=10)
    for i in range(count):
        print(i)
        depth = fake.random_int(min=1, max=10)
        path = fake.file_path(depth)
        submodule =  Path(node_modules.as_posix() + path)
        dir_name = Path(os.path.dirname(submodule.as_posix()))
        dir_name.mkdir(parents=True, exist_ok=True)
        submodule.touch()
    # Act
    result = NodeClean().run(path=tmp_path)

    # Assert
    assert result.hasError() == False
    assert exists(node_modules) == False

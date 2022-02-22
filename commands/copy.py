import pathlib
import shutil
import click

from models.result import Result


@click.command()
@click.argument("source")
@click.argument("destination")
def copy(source: str, destination: str):
    """
    Copy files and/or directories

    SOURCE the file or directory path to be copied
    DESTINATION the destination directory path
    """
    try:
        shutil.copy(source, destination)
    except:
        return Result(1, "There was an error copying the file or directory")

    return Result(0, "Copy successful!")

import click


@click.command()
@click.argument("source")
@click.argument("destination")
def copy(source: str, destination: str):
    """
    Copy files and/or directories

    SOURCE the file or directory path to be copied
    DESTINATION the destination directory path
    """

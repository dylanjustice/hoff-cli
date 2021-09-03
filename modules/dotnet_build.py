from modules.dotnet_path import solution_path
import click

path = solution_path()
cmd = ["dotnet", "build", path if path else "", "--no-restore"]
@click.command()
@click.option("-r", "--restore", is_flag=True)
@click.option("-c", "--clean", is_flag=True)
def dotnet_build():
    """Builds the dotnet project via """


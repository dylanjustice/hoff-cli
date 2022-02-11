
import click
import subprocess
from modules.dotnet_run import dotnet_run
from options.dotnet_run_options import DotnetRunOptions

run_cmd = ["dotnet", "run", "--no-restore"]
build_cmd = ["dotnet", "build", "--no-restore"]


@click.group()
def dotnet():
    """Run various dotnet commands for the project"""


@dotnet.command(name="info")
def info():
    """Display .NET information"""
    subprocess.run("dotnet --info")


@dotnet.command(name="sdks")
def list_sdks():
    """Display install SDKs"""
    subprocess.run("dotnet --list-sdks")


@dotnet.command(name="runtimes")
def list_runtimes():
    """Display installed runtimes"""
    subprocess.run("dotnet --list-runtimes")


@click.option("-b", "--build", is_flag=True)
@click.option("-c", "--clean", is_flag=True)
@click.option("-R", "--restore", is_flag=True)
@click.option("-w", "--watch", is_flag=True)
@click.argument("path", required=False)
@dotnet.command()
def run(restore, clean, build, path, watch):
    options = DotnetRunOptions(
        restore=restore,
        clean=clean,
        path=path,
        watch=watch,
        build=build
    )
    dotnet_run(options)

import subprocess

import click
from models.options.dotnet_run_options import DotnetRunOptions
from models.result import Result
from modules.dotnet_run import DotnetRun
from modules.dotnet_test import DotnetTest
from modules.echo import error


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


@click.option("-b", "--build", is_flag=True, help="Build the solution before running")
@click.option("-c", "--clean", is_flag=True, help="Clean the solution before building")
@click.option("-R", "--restore", is_flag=True, help="Restore nuget packages before running")
@click.option("-w", "--watch", is_flag=True, help="Run in watch mode")
@click.argument("path", required=False)
@dotnet.command()
def run(restore, clean, build, path, watch):
    """Run dotnet project or solution

    PATH is the relative path to  a solution or project
    """
    options = DotnetRunOptions(
        build=build,
        clean=clean,
        path=path,
        restore=restore,
        watch=watch
    )
    result = DotnetRun.run(options)
    if result.hasError():
        error(message=result.message)
        exit(result.status_code)


@click.option("--ci", is_flag=True, help="")
@click.option("--coverage", is_flag=True)
@click.option("--filter")
@dotnet.command()
def test(ci, filter, coverage):
    result: Result = DotnetTest.run(ci, filter, coverage)
    if result.hasError():
        error(result.message)
        exit(result.status_code)

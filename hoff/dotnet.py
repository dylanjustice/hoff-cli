from modules.echo import error
from modules.dotnet_restore import dotnet_restore
from modules.dotnet_clean import dotnet_clean
from modules.dotnet_path import solution_path, web_project_dir
import click
import subprocess
import os


run_cmd = ["dotnet", "run", "--no-restore"]
build_cmd = ["dotnet", "build", "--no-restore"]


@click.group(invoke_without_command=True)
@click.option("-b", "--build", is_flag=True)
@click.option("-c", "--clean", is_flag=True)
@click.option("-R", "--restore", is_flag=True)
@click.option("-w", "--watch", is_flag=True)
@click.argument("path", required=False)
@click.pass_context
def dotnet(ctx, restore, clean, build, watch, path):
  """Run various dotnet commands for the project"""
  if ctx.invoked_subcommand is None:
    run(restore, clean, build, path)
  pass


@dotnet.command()
def info():
  """Display .NET information"""
  subprocess.run("dotnet --info")


@dotnet.command(name="list-sdks")
def list_sdks():
  """Display install SDKs"""
  subprocess.run("dotnet --list-sdks")


@dotnet.command(name="list-runtimes")
def list_runtimes():
    """Display installed runtimes"""
    subprocess.run("dotnet --list-runtimes")


def run(restore, clean, build, path):
  cwd = os.getcwd()
  if path:
    os.chdir(path)

  solution_file = solution_path()
  path = solution_path()


  if solution_file is None:
    error("Solution file not found")
    exit(1)

  if clean:
    result = dotnet_clean(path)
    if not build and not restore:
      exit(result)
  if restore:
    dotnet_restore(path)

  path = web_project_dir()

  cmd = run_cmd if not build else build_cmd

  if path:
    os.chdir(path)

  subprocess.run(cmd)

  os.chdir(cwd)

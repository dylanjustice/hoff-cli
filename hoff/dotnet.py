from click.exceptions import UsageError
from modules.dotnet_path import solution_path, web_project_dir
from modules.dotnet_build import dotnet_build
import click
import subprocess
import os

cmd = ["dotnet"]

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
  if path:
    os.chdir(path)

  solution_file = solution_path()
  if solution_file is None:
    exit(1)
  if clean:
    print("clean")
  if restore:
    print("restore")
  
  web_dir = web_project_dir()
  if web_dir is None:
    click.echo("Web project not found", err=True, color=True)
    exit(1)

  os.chdir(web_dir)

  if build:
    cmd.append("build")
    subprocess.run(cmd)
  else:
    cmd.append("run")
    subprocess.run(cmd)


dotnet.add_command(dotnet_build, "build")

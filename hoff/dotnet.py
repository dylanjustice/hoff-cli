
import click
import subprocess
@click.group()
def dotnet():
  """Run various dotnet commands for the project"""
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



    

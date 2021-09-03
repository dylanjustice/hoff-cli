from glob import has_magic
import os
import subprocess
import click
from modules.dotnet_path import solution_dir
cmd = ["dotnet", "restore"]

def dotnet_restore(path=""):
    """Restore the dotnet solution from the root of the project via dotnet restore """
    if path:
        cmd.append(path)
    click.echo("Restoring nuget packages (via %s" % " ".join(cmd))


    result = subprocess.run(cmd)
    status = result.returncode

    if status != 0:
        click.echo("Solution failed to restore. See output for details.")
        return status

    click.echo("DOtnet solution restored!")
    return status



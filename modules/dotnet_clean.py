
from modules.echo import error, info
import os
import shutil
import subprocess
import click

from modules.dotnet_path import solution_dir


cmd = ["dotnet", "clean"]

def dotnet_clean(path=""):
    if path:
        cmd.append(path)
    click.echo("Recursively deleting bin directory")
    shutil.rmtree("bin", ignore_errors=True)
    shutil.rmtree("obj", ignore_errors=True)

    info("Running dotnet clean (via %s on the solution)" % " ".join(cmd))

    result = subprocess.run(cmd)
    status = result.returncode

    if status != 0:
        error("Solution failed to clean. See output for details")
        return status

    return status


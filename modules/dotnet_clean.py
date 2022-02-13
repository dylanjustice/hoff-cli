
import shutil
import subprocess
from subprocess import CompletedProcess

import click

from modules.echo import error, info

cmd = ["dotnet", "clean"]


class DotnetClean:
    def run(path=""):
        if path:
            cmd.append(path)
        click.echo("Recursively deleting bin directory")
        shutil.rmtree("bin", ignore_errors=True)
        shutil.rmtree("obj", ignore_errors=True)

        info("Running dotnet clean (via %s on the solution)" % " ".join(cmd))

        result: CompletedProcess = subprocess.run(cmd)
        status = result.returncode

        if status != 0:
            error("Solution failed to clean. See output for details")
            return status

        return status

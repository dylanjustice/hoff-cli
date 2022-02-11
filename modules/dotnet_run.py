import subprocess
from modules.echo import error
from modules.dotnet_restore import dotnet_restore
from modules.dotnet_clean import dotnet_clean
from modules.dotnet_path import solution_path, web_project_dir
import os

from options.dotnet_run_options import DotnetRunOptions

run_cmd = ["dotnet", "run", "--no-restore"]
build_cmd = ["dotnet", "build", "--no-restore"]


def dotnet_run(options: DotnetRunOptions):
    """Run a .NET project"""
    cwd = os.getcwd()

    if options.path:
        os.chdir(options.path)

    solution_file = solution_path()
    path = solution_path()

    if solution_file is None:
        error("Solution file not found")
        exit(1)

    if options.clean:
        result = dotnet_clean(path)

        if not options.build and not options.restore:
            exit(result)

    if options.restore:
        dotnet_restore(path)

    path = web_project_dir()

    cmd = run_cmd if not options.build else build_cmd

    if path:
        os.chdir(path)

    subprocess.run(cmd)

    os.chdir(cwd)

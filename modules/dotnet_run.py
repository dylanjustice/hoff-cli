import os
import subprocess

from models.options.dotnet_run_options import DotnetRunOptions
from models.result import Result

from modules.dotnet_clean import DotnetClean
from modules.dotnet_path import solution_path, web_project_dir
from modules.dotnet_restore import DotnetRestore

run_cmd = ["dotnet", "run", "--no-restore"]
build_cmd = ["dotnet", "build", "--no-restore"]


class DotnetRun:
    # region Constants

    ERR_SLN_NOT_FOUND: str = "Solution file not found."

    # endregion Constants

    def run(self, options: DotnetRunOptions) -> Result:
        """Run a .NET project"""
        cwd = os.getcwd()

        if options.path:
            os.chdir(options.path)

        path = solution_path()

        if path is None:
            return Result(1, self.ERR_SLN_NOT_FOUND)

        if options.clean:
            result = DotnetClean.run(path)
            if not options.build and not options.restore:
                exit(result)
        if options.restore:
            DotnetRestore.run(path)

        path = web_project_dir()

        cmd = run_cmd if not options.build else build_cmd

        if path:
            os.chdir(path)

        subprocess.run(cmd)

        os.chdir(cwd)

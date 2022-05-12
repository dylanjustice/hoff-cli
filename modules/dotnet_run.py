import os
import subprocess

from models.options.dotnet_run_options import DotnetRunOptions
from models.result import Result

from modules.dotnet_clean import DotnetClean
from modules.dotnet_path import DotnetPath
from modules.dotnet_restore import DotnetRestore

run_cmd = ["dotnet", "run", "--no-restore"]
build_cmd = ["dotnet", "build", "--no-restore"]


class DotnetRun:
    # region Constants

    ERR_SLN_NOT_FOUND: str = "Solution file not found."

    # endregion Constants

    def __init__(self, dotnet_clean: DotnetClean = None, dotnet_path: DotnetPath = None, _dotnet_restore: DotnetRestore = None) -> None:
        self._dotnet_path = dotnet_path or DotnetPath()
        self._dotnet_clean = dotnet_clean or DotnetClean()
        self._dotnet_restore = _dotnet_restore or DotnetRestore()

    def run(self, options: DotnetRunOptions) -> Result:
        """Run a .NET project"""
        cwd = os.getcwd()

        if options.path:
            os.chdir(options.path)

        path = self._dotnet_path.solution_path()

        if path is None:
            return Result(1, self.ERR_SLN_NOT_FOUND)

        if options.clean:
            result = self._dotnet_clean.run(path)
            if not options.build and not options.restore:
                exit(result)
        if options.restore:
            self._dotnet_restore.run(path)

        path = self._dotnet_path.web_project_dir()

        cmd = run_cmd if not options.build else build_cmd

        if path:
            os.chdir(path)

        subprocess.run(cmd)

        os.chdir(cwd)

        return Result(0)

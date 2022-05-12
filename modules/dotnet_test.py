import os
import subprocess
from models.result import Result

from modules.dotnet_path import DotnetPath


class DotnetTest:
    ERR_NOT_FOUND = "Solution file not found"
    ERR_TEST_FAILED = "Test run failed. Check output for more information"
    SUCCESS = "Test suite completed successfully"
    CMD = ["dotnet", "test", "--no-restore"]
    COVERAGE_OPTIONS = "--collect:'XPlat Code Coverage' -- DataCollectionRunSettings.DataCollectors.DataCollector.Configuration.Format=cobertura"

    def __init__(self, dotnet_path: DotnetPath = None) -> None:
        self._dotnet_path = dotnet_path or DotnetPath()

    def run(self, filter: str, coverage: bool, path: str = "") -> Result:
        """Runs dotnet test runner on the undefined solution (via dotnet test --no-build --no-restore)"""
        if path:
            os.chdir(path)
        sln_path = self._dotnet_path.solution_path()
        if sln_path is None:
            return Result(1, "Solution file not found")

        self.CMD.append(sln_path)

        if filter is not None:
            self.CMD.append("--filter" + filter)

        if coverage == True:
            self.CMD.append(self.COVERAGE_OPTIONS)

        test_result: subprocess.CompletedProcess = subprocess.run(
            self.CMD, text=True
        )

        if (test_result.returncode != 0):
            return Result(1, self.ERR_TEST_FAILED)

        return Result(0, self.SUCCESS)

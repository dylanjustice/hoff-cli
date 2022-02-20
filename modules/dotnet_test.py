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

    @classmethod
    def run(this, filter: str, coverage: bool, path: str=None) -> Result:
        """Runs dotnet test runner on the undefined solution (via dotnet test --no-build --no-restore)"""
        if path is not None:
            os.chdir(path)
        sln_path = DotnetPath.solution_path()
        if sln_path is None:
            return Result(1, "Solution file not found")

        this.CMD.append(sln_path)

        if filter is not None:
            this.CMD.append("--filter" + filter)

        if coverage == True:
            this.CMD.append(this.COVERAGE_OPTIONS)

        test_result: subprocess.CompletedProcess = subprocess.run(
            this.CMD, text=True
        )

        if (test_result.returncode != 0):
            return Result(1, this.ERR_TEST_FAILED)

        return Result(0, this.SUCCESS)

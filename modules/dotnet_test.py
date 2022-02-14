from models.result import Result

from modules.dotnet_path import DotnetPath


class DotnetTest:
    def run(ci, filter, coverage) -> Result:
        """Runs dotnet test runner on the undefined solution (via dotnet test --no-build --no-restore)"""
        path = DotnetPath.solution_path()
        if path is None:
            return Result(1, "Solution not found")

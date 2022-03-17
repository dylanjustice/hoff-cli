from os import chdir
import shutil
import subprocess
from models.result import Result
from modules.echo import info
from modules.frontend_path import FrontendPath
from modules.node_clean import NodeClean
from modules.node_restore import NodeRestore


class WebpackRun:
    # region Constants
    ERR_NOT_FOUND = "The system could not find the path specified. {0}"
    ERR_UNEXPECTED = "There was an unexpected error. Please review the output and try again."
    CMD = ["npm", "run", "start"]

    # endregion Constants
    @classmethod
    def run(self, clean: bool, restore: bool, path: str = "") -> Result:
        frontend_path = FrontendPath.get_frontend_path(path)
        try:
            chdir(frontend_path)
        except FileNotFoundError as ex:
            return Result(1, self.ERR_NOT_FOUND.format(frontend_path), ex)

        if clean:
            clean_result: Result = NodeClean.run(frontend_path)
            if clean_result.hasError():
                return clean_result
        if restore:
            restore_result = NodeRestore.run(frontend_path)
            if restore_result.hasError():
                return restore_result

        info("Running frontend via {}".format(' '.join(self.CMD)))
        result: subprocess.CompletedProcess = subprocess.run(
            self.CMD, shell=True)

        if result.returncode > 0:
            return Result(result.returncode, self.ERR_UNEXPECTED)

        return Result(0)

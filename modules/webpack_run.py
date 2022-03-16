from os import chdir
import shutil
import subprocess
from models.result import Result
from modules.echo import info
from modules.node_clean import NodeClean

class WebpackRun:
    #region Constants
    ERR_NOT_FOUND = "The system could not find the path specified. {0}"
    ERR_UNEXPECTED = "There was an unexpected error. Please review the output and try again."
    CMD = ["npm", "run", "start"]

    #endregion Constants
    @classmethod
    def run(self, clean: bool, restore: bool, path: str = "frontend") -> Result:
        if clean:
            clean_result: Result = NodeClean.run(path)
            if clean_result.hasError():
                return clean_result
        if restore:
            print("Webpack restore")

        try:
            chdir(path)
        except FileNotFoundError as ex:
            return Result(1, self.ERR_NOT_FOUND.format(path), ex)

        info("Running frontend via {}".format(self.CMD))
        result: subprocess.CompletedProcess = subprocess.run(self.CMD, shell=True)

        if result.returncode > 0:
            return Result(result.returncode, self.ERR_UNEXPECTED)

        return Result(0)


import os
import subprocess
from models.result import Result
from modules.echo import info, success


class NodeRestore:
    CMD = ["npm", "install"]
    CI_CMD = ["npm", "ci", "--no-optional"]
    ERR_UNEXPECTED = "There was an unexpected error. Please review the output and try again."
    MSG_SUCCESS = "npm packages restored"

    def __init__(self) -> None:
        pass

    def run(self, path: str, ci_mode: bool = False) -> Result:
        cmd = self.CI_CMD if ci_mode else self.CMD
        os.chdir(path)
        info("Restore npm dependencies via ({0}) in the {1}".format(
            ' '.join(cmd), path))
        result: subprocess.CompletedProcess = subprocess.run(
            cmd, shell=True)

        if result.returncode > 0:
            return Result(result.returncode, self.ERR_UNEXPECTED)

        success(self.MSG_SUCCESS)

        return Result(0)

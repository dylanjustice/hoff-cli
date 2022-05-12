import os
from pathlib import Path
import shutil
import subprocess
from models.result import Result
from modules.echo import error, info
from modules.frontend_path import FrontendPath
from modules.node_restore import NodeRestore


class WebpackPublish:

    ERR_UNABLE_TO_DELETE = "Error deleting node_modules"
    ERR_UNEXPECTED = "There was an unexpected error in the subprocess. Please review the output and try again"
    ERR_FAILED_BUILD = "An error occurred while building the production bundle"
    SUCCESS_MSG = "Frontend build successful!"
    BUILD_CMD = ["npm", "run", "build"]

    def __init__(self, frontend_path: FrontendPath = None, node_restore: NodeRestore = None) -> None:
        self._frontend_path = frontend_path or FrontendPath()
        self._node_restore = node_restore or NodeRestore()

    def run(self, restore: bool, path: str = "") -> Result:
        publish_dir = self._frontend_path.get_frontend_path(path)
        info("Cleaning publish directory: {0}".format(path))
        clean_result = self.clean_publish_directory(path=path)
        if clean_result.hasError():
            return clean_result

        if restore:
            restore_result = self._node_restore.run(ci_mode=True, path=path)
            if restore_result.hasError():
                return restore_result

        return self.build(publish_dir)

    def clean_publish_directory(self, path) -> Result:
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as ex:
            error("Exited with error")
            return Result(1, self.ERR_UNABLE_TO_DELETE, ex)

        return Result(0, "Cleaned successfully")

    def build(self, path: Path) -> Result:
        try:
            os.chdir(path)
            info("Building frontend (via {0}".format(self.BUILD_CMD))
            result: subprocess.CompletedProcess = subprocess.run(
                self.BUILD_CMD, shell=True)

            if result.returncode > 0:
                return Result(result.returncode, self.ERR_UNEXPECTED)

        except Exception as ex:
            error("Exited with errors")
            return Result(1, self.ERR_FAILED_BUILD, ex)

        return Result(0, self.SUCCESS_MSG)

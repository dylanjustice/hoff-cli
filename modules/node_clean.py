from os import rmdir
import shutil
from models.result import Result
from modules.echo import error, info


class NodeClean:
    ERR_UNABLE_TO_DELETE = "Error deleting node_modules"

    @classmethod
    def run(self, path: str) -> Result:
        node_modules = path / "node_modules"

        info("Recursively deleting {0}".format(node_modules))
        try:
            shutil.rmtree(node_modules, ignore_errors=True)
        except Exception as ex:
            error("Exited with error")
            return Result(1, self.ERR_UNABLE_TO_DELETE, ex)

        return Result(0)



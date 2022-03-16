from os import rmdir
from models.result import Result
from modules.echo import error, info


class NodeClean:
    @classmethod
    def run(path: str) -> Result:
        node_modules = path / "node_modules"

        info("Recursively deleting {node_modules}".format(node_modules))
        try:
            rmdir(node_modules)
        except:
            error("Exited with error")
            return Result(1, "Error deleting node_modules")

        return Result(0)



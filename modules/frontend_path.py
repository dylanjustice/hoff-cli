import os
from pathlib import Path


class FrontendPath:
    PROJECT_DIR = "frontend"
    PUBLISH_DIR = "build"

    def __init__(self) -> None:
        pass

    def get_frontend_path(self, path: str = "") -> Path:
        if not path:
            return Path("{0}/{1}".format(os.getcwd(), self.PROJECT_DIR))
        return Path("{0}/{1}".format(path, self.PROJECT_DIR))

    def get_publish_dir(self, path: str = "") -> Path:
        return self.get_frontend_path(path) / self.PUBLISH_DIR

import os
from pathlib import Path


class FrontendPath:
    PROJECT_DIR = "frontend"
    PUBLISH_DIR = "frontend/build"

    @classmethod
    def get_frontend_path(self, path: str = "") -> Path:
        if not path:
            return Path("{0}/{1}".format(os.getcwd(), self.PROJECT_DIR))
        return Path("{0}/{1}".format(path, self.PROJECT_DIR))

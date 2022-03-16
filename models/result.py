from dataclasses import dataclass


@dataclass
class Result:
    status_code: int
    message: str = None
    error: Exception = None

    def hasError(self):
        return self.status_code != 0

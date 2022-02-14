from dataclasses import dataclass
from logging import exception


@dataclass
class Error:
    message: str
    ex: Exception

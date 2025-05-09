from io import *
from .console_message import *


class FileManager:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def lines(self) -> list[str]:
        try:
            with open(self._name, "r") as f:
                return f.readlines()
        except:
            print(ConsoleMessage(f"Failed to open {self._name}.").error())
            return []

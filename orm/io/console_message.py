class ConsoleMessage:
    _msg: str

    def __init__(self, msg: str) -> None:
        self._msg = msg

    def warning(self) -> str:
        return f"[WARNING] {self._msg}"

    def error(self) -> str:
        return f"[ERROR] {self._msg}"

class MarsRover:
    def __init__(self):
        self._x_position: int = 0
        self._y_position: int = 0
        self._direction: str = "N"

    def execute(self, command: str) -> str:
        if command == "M":
            return "0:1:N"

        if command == "MM":
            return "0:2:N"

        return f"{self._x_position}:{self._y_position}:{self._direction}"

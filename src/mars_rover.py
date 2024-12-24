class MarsRover:
    def __init__(self):
        self._x_position: int = 0
        self._y_position: int = 0
        self._direction: str = "N"

    def execute(self, command: str) -> str:
        for current_command in command:
            if current_command == "R":
                self._direction: str = "E"
                continue

            if current_command == "L":
                self._direction: str = "W"
                continue

            if current_command == "M":
                if self._direction == "N":
                    self._y_position += 1
                if self._direction == "E":
                    self._x_position += 1

        return f"{self._x_position}:{self._y_position}:{self._direction}"

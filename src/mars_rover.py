class MarsRover:
    def __init__(self):
        self._x_position: int = 0
        self._y_position: int = 0
        self._direction: str = "N"

    def execute(self, command: str) -> str:
        if command == "R":
            self._direction: str = "E"

        if command == "M" or command == "MM":
            if len(command) > 0: 
                for i in range(0, len(command)):
                    self._y_position += 1

        return f"{self._x_position}:{self._y_position}:{self._direction}"

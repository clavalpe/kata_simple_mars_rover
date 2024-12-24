class MarsRover:
    def __init__(self):
        self._x_position: int = 0
        self._y_position: int = 0
        self._direction: str = "N"

    def execute(self, command: str) -> str:
        for current_command in command:
            if current_command == "R":
                self._turn_right()
                continue

            if current_command == "L":
                self._turn_left()
                continue

            if current_command == "M":
                self._move_forward()

        return f"{self._x_position}:{self._y_position}:{self._direction}"

    def _turn_right(self):
        self._direction = "E"

    def _turn_left(self):
        if self._direction == "E":
            self._direction = "N"
            return

        self._direction = "W"

    def _move_forward(self):
        if self._direction == "N":
            self._y_position += 1
        if self._direction == "E":
            self._x_position += 1

from mars_rover import MarsRover


class TestMarsRover:
    def test_it_starts_in_position_0_0_N(self):
        rover_position = MarsRover().execute("")

        assert rover_position == "0:0:N"

    def test_it_moves_one_position_when_receives_command_M(self):
        rover_position = MarsRover().execute("M")

        assert rover_position == "0:1:N"

    def test_it_moves_two_positions_when_receives_command_MM(self):
        rover_position = MarsRover().execute("MM")

        assert rover_position == "0:2:N"

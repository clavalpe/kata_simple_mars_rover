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

    def test_it_rotates_to_the_rigth_when_receives_command_R(self):
        rover_position = MarsRover().execute("R")

        assert rover_position == "0:0:E"

    def test_it_rotates_to_the_left_when_receives_command_L(self):
        rover_position = MarsRover().execute("L")

        assert rover_position == "0:0:W"

    def test_it_moves_to_position_1_2_E_when_receives_command_MMRM(self):
        rover_position = MarsRover().execute("MMRM")

        assert rover_position == "1:2:E"

    def test_it_moves_to_position_2_3_N_when_receives_command_MMRMMLM(self):
        rover_position = MarsRover().execute("MMRMMLM")

        assert rover_position == "2:3:N"

from mars_rover import MarsRover


class TestMarsRover:
    def test_it_starts_in_position_0_0_N(self):
        rover_position = MarsRover().execute('')

        assert rover_position == '0:0:N'
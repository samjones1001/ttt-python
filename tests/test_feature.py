import tic_tac_toe as app
import ttt.interface as interface


class Runner:
    def __init__(self):
        self._current_index = 0

    def fake_input(self):
        values = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        current_value = values[self._current_index]
        self._current_index += 1
        return current_value


def test_can_play_a_full_game():
    runner = Runner()
    interface.input = lambda: runner.fake_input()
    assert app.main() == ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
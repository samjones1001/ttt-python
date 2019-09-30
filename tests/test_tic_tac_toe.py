import pytest
import tic_tac_toe as app
from ttt.game_runner import GameRunner
from ttt.console import Console


class MockConsoleIO:
    def __init__(self, values):
        self._values = values
        self.last_output = None

    def get_input(self, message=""):
        return self._values.pop(0)

    def print_output(self, output):
        self.last_output = output

@pytest.fixture
def filled_board_output():
    return ' O | X | O \n-----------\n X | O | X \n-----------\n O | X | O '


def test_can_play_a_full_game(filled_board_output):
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    mock_console_io = MockConsoleIO(values)
    console = Console(io=mock_console_io)
    runner = GameRunner(console=console)
    app.main(runner)
    assert mock_console_io.last_output == filled_board_output


def test_gracefully_handles_invalid_user_input(filled_board_output):
    values = ['-1' '0', '1', '2', '3', 'not a number' '4', '5', '3000' '6', '7', '8']
    mock_console_io = MockConsoleIO(values)
    console = Console(io=mock_console_io)
    runner = GameRunner(console=console)
    app.main(runner)
    assert mock_console_io.last_output == filled_board_output


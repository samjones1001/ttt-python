import tic_tac_toe as app
from ttt.game_runner import GameRunner
from ttt.console import Console


class MockConsoleIO:
    def __init__(self):
        self._values = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.last_output = None

    def get_input(self, message=""):
        return self._values.pop(0)

    def print_output(self, output):
        self.last_output = output


def test_can_play_a_full_game():
    mock_console_io = MockConsoleIO()
    console = Console(console_io=mock_console_io)
    runner = GameRunner(console=console)
    app.main(runner)

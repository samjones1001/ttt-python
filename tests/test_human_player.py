import pytest
from ttt.players.human_player import HumanPlayer
from ttt.console_ui.console import Console
from tests.mocks import MockConsole, MockGame, MockConsoleIO


class TestRunner:
    def set_player_marker(self, inputs):
        io = MockConsoleIO(inputs)
        console = Console(io)
        player = HumanPlayer('Player 1', 'X', console)
        player.set_marker()

        return player.get_marker()


@pytest.fixture
def runner():
    return TestRunner()


def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    player = HumanPlayer('player 1', 'X', console)

    player.get_move(MockGame(available_spaces=[]))

    assert console.get_valid_input_call_count == 1

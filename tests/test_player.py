from ttt.player import Player
from tests.mocks import MockConsole


def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    player = Player('player 1', 'X')

    player.get_move([], console)

    assert console.get_valid_input_call_count == 1

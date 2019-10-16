from ttt.players.human_player import HumanPlayer
from tests.mocks import MockConsole, MockGame


def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    player = HumanPlayer('player 1', 'X', console)

    player.get_move(MockGame(available_spaces=[0]))

    assert console.get_valid_input_call_count == 1

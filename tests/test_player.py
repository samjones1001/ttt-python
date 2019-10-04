from ttt.players.player import Player
from tests.mocks import MockConsole, MockGame

def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    game = MockGame(available_spaces=[1,2,3])
    player = Player('player 1', 'X')

    player.get_move(game, console)

    assert console.get_valid_input_call_count == 1

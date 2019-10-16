from ttt.players.simple_computer_player import SimpleComputerPlayer
from tests.mocks import MockGame


def test_simple_computer_player_move_returns_the_index_of_an_available_space():
    spaces = [1,5,7]
    game = MockGame(available_spaces=[1,5,7])
    computer_player = SimpleComputerPlayer('player 2', 'X')

    assert computer_player.get_move(game) in spaces

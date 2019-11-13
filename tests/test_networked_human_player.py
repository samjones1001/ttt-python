from tests.mocks import MockServer
from ttt.game.game import Game
from ttt.players.networked_human_player import NetworkedHumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer


def test_accepts_data_from_networked_connection_then_converts_to_computer_readable_index():
    server = MockServer(input='1')
    player_1 = NetworkedHumanPlayer('Player 1', 'X', server)
    player_2 = SimpleComputerPlayer('Player 2', 'O')
    game = Game(player_1, player_2)

    assert player_1.get_move(game) == 0
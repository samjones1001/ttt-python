from tests.mocks import MockPlayer
from ttt.game.board import Board
from ttt.game.game import Game
from ttt.persister.persister import Persister


def test_creates_a_json_object_representing_current_game_state():
    board = Board(['X', 'O', 'X', 'O', '5', '6', '7', '8', '9'])
    player_1 = MockPlayer('Player 1', 'O')
    player_2 = MockPlayer('Player 2', 'X')
    game = Game(player_1, player_2, board)

    persister = Persister()
    json_game = persister.game_to_json(game)

    assert json_game == '{"board": ["X", "O", "X", "O", "5", "6", "7", "8", "9"], "current_player": "Player 1", "opponent": "Player 2"}'

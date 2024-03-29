from tests.mocks import MockPlayer, MockConsole
from ttt import constants
from ttt.game.board import Board
from ttt.game.game_config import GameConfig


def test_creates_a_config_object_with_passed_attributes():
    console = MockConsole()
    game_config = GameConfig(console)

    player_1 = MockPlayer('player 1', 'O')
    player_2 = MockPlayer('player 2', 'X')
    board = Board()

    config_obj = game_config.create_config_object(player_1, player_2, board)

    assert config_obj.first_player == player_1
    assert config_obj.second_player == player_2
    assert config_obj.board == board


def test_sets_the_colour_of_a_players_marker():
    console = MockConsole()
    game_config = GameConfig(console)
    player = MockPlayer('Player 1', 'O')

    expected_colour_code = constants.COLOURS['1']
    game_config.set_marker_colour(player, '1')

    assert player.get_marker_colour() == expected_colour_code

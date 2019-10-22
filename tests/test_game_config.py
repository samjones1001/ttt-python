from tests.mocks import MockPlayer, MockConsole
from ttt import constants
from ttt.game.game import Game
from ttt.game.game_config import GameConfig


def test_creates_a_cofig_object_with_passed_attributes():
    console = MockConsole()
    game_config = GameConfig(console)

    player_1 = MockPlayer('player 1', 'O')
    player_2 = MockPlayer('player 2', 'X')
    game = Game

    config_obj = game_config.create_config_object(player_1, player_2, game)

    assert config_obj.first_player == player_1
    assert config_obj.second_player == player_2
    assert config_obj.game == game


def test_sets_a_marker_to_be_displayed_in_colour():
    console = MockConsole()
    game_config = GameConfig(console)
    player = MockPlayer('Player 1', 'O')

    game_config.set_marker_colour(player, constants.RED)

    assert player.get_marker() == f"{constants.RED}O{constants.END_COLOUR}"

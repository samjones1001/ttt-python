from tests.mocks import MockPlayer, MockConsole
from ttt.game.game import Game
from ttt.game.game_config import GameConfig


def test_creates_a_cofig_object_with_passed_attributes():
    console = MockConsole()
    game_config = GameConfig(console)

    player_1 = MockPlayer('player 1', '0')
    player_2 = MockPlayer('player 2', 'X')
    game = Game

    config_obj = game_config.create_config_object(player_1, player_2, game)

    assert config_obj.first_player == player_1
    assert config_obj.second_player == player_2
    assert config_obj.game == game

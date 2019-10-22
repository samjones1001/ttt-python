from collections.abc import Callable
from attr import dataclass

from ttt import constants
from ttt.players.player import Player
from ttt.players.player_factory import PlayerFactory
from ttt.messages import invalid_marker_message


@dataclass
class Config:
    first_player: Player
    second_player: Player
    game: Callable


class GameConfig:
    def __init__(self, console):
        self._console = console

    def create_config_object(self, first_player, second_player, game):
        return Config(first_player, second_player, game)

    def select_player_type(self, user_choice, name, marker, factory=None):
        if factory is None:
            factory = PlayerFactory()

        choices = {'1': constants.HUMAN_PLAYER_STRING,
                   '2': constants.SIMPLE_COMPUTER_STRING,
                   '3': constants.SMART_COMPUTER_STRING}

        return factory.create(choices[user_choice], name, marker, self._console)

    def select_default_marker(self, taken_marker):
        return constants.PLAYER_1_MARKER if taken_marker == constants.PLAYER_2_MARKER else constants.PLAYER_2_MARKER

    def set_player_marker(self, player, taken_marker, marker_choice):
        if not self._is_marker_availabile(marker_choice, taken_marker):
            self._console.output_message(invalid_marker_message())
            return None
        elif marker_choice != '':
            player.set_marker(marker_choice)
        return player

    def set_marker_colour(self, player, colour_choice):
        player.set_marker_colour(constants.COLOURS[colour_choice])

    def _is_marker_availabile(self, selected_marker, taken_marker):
        return selected_marker != taken_marker

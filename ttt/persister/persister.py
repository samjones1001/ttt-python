import json

from ttt import constants
from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game_config import GameConfig, Config
from ttt.persister.persister_io import PersisterIO


class Persister():
    def __init__(self, io=PersisterIO(), game_config=GameConfig(Console())):
        self._io = io
        self._game_config = game_config

    def save(self, filename, game):
        json_data = self._io.read(filename)
        games_dictionary = json.loads(json_data) if json_data else {}
        save_id = str(len(games_dictionary) + 1)
        games_dictionary[save_id] = self._game_state_to_save_data(game)

        self._io.write(filename, json.dumps(games_dictionary))
        return save_id

    def load(self, filename, save_id):
        return self._json_to_game_config(self._io.read(filename), save_id)

    def _game_state_to_save_data(self, game):
        return {constants.BOARD_KEY: game.get_board().get_spaces(),
                constants.CURRENT_PLAYER_KEY: {
                   constants.NAME_KEY: game.get_current_player_name(),
                   constants.TYPE_KEY: type(game._current_player).__name__,
                   constants.MARKER_KEY: game.get_current_player_marker(),
                   constants.COLOUR_KEY: game._current_player.get_marker_colour()
                },
                constants.OPPONENT_KEY: {
                   constants.NAME_KEY: game.get_opponent_name(),
                   constants.TYPE_KEY: type(game._opponent).__name__,
                   constants.MARKER_KEY: game.get_opponent_marker(),
                   constants.COLOUR_KEY: game._opponent.get_marker_colour()
                }}

    def _json_to_game_config(self, json_data, save_id):
        data = json.loads(json_data)[save_id]
        first_player = self._setup_player(data[constants.CURRENT_PLAYER_KEY])
        second_player = self._setup_player(data[constants.OPPONENT_KEY])

        return Config(first_player, second_player, Board(data[constants.BOARD_KEY]))

    def _setup_player(self, json_player):
        player = self._game_config.create_player(json_player[constants.TYPE_KEY], json_player[constants.NAME_KEY], json_player[constants.MARKER_KEY])
        player.set_marker_colour(json_player[constants.COLOUR_KEY])
        return player

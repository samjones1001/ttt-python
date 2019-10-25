import json

from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game import Game
from ttt.game.game_config import GameConfig, Config
from ttt.persister.persister_io import PersisterIO


class Persister():
    def __init__(self, io=PersisterIO, game_config=GameConfig(Console())):
        self._io = io
        self._game_config = game_config

    def save(self, filename, game):
        self._io.write(filename, self._game_to_json(game))

    def load(self, filename):
        return self._json_to_game_config(self._io.read(filename))

    def _game_to_json(self, game):
        return json.dumps({'board': game.get_board().get_spaces(),
                           'current_player': {
                               'name': game.get_current_player_name(),
                               'type': type(game._current_player).__name__,
                               'marker': game.get_current_player_marker(),
                               'colour': game._current_player.get_marker_colour()
                           },
                           'opponent': {
                               'name': game.get_opponent_name(),
                               'type': type(game._opponent).__name__,
                               'marker': game.get_opponent_marker(),
                               'colour': game._opponent.get_marker_colour()
                           }
                           })

    def _json_to_game_config(self, json_data):
        data = json.loads(json_data)
        first_player = self._game_config.create_player(data['current_player']['type'], data['current_player']['name'], data['current_player']['marker'])
        self._game_config.set_marker_colour(first_player, data['current_player']['colour'])

        second_player = self._game_config.create_player(data['opponent']['type'], data['opponent']['name'], data['opponent']['marker'])
        self._game_config.set_marker_colour(second_player, data['opponent']['colour'])

        return Config(first_player, second_player, Board(data['board']))



import json

from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game_config import GameConfig, Config
from ttt.persister.persister_io import PersisterIO


class Persister():
    def __init__(self, io=PersisterIO, game_config=GameConfig(Console())):
        self._io = io
        self._game_config = game_config

    def save(self, filename, game):
        existing_data = self._io.read(filename)
        save_id = str(len(json.loads(existing_data) + 1)) if existing_data else '1'
        self._io.write(filename, self._game_to_json(game, save_id))

    def load(self, filename, save_id):
        return self._json_to_game_config(self._io.read(filename), save_id)

    def _game_to_json(self, game, save_id):
        return json.dumps({save_id: {'board': game.get_board().get_spaces(),
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
                           }})

    def _json_to_game_config(self, json_data, save_id):
        data = json.loads(json_data)[save_id]
        first_player = self._setup_player(data['current_player'])
        second_player = self._setup_player(data['opponent'])

        return Config(first_player, second_player, Board(data['board']))

    def _setup_player(self, json_player):
        player = self._game_config.create_player(json_player['type'], json_player['name'], json_player['marker'])
        self._game_config.set_marker_colour(player, json_player['colour'])
        return player

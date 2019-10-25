import json

from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game_config import GameConfig, Config
from ttt.persister.persister_io import PersisterIO


class Persister():
    def __init__(self, io=PersisterIO(), game_config=GameConfig(Console())):
        self._io = io
        self._game_config = game_config

    def save(self, filename, game):
        existing_data = self._io.read(filename)
        self._io.write(filename, self._save_data_to_json(existing_data, game))

    def load(self, filename, save_id):
        return self._json_to_game_config(self._io.read(filename), save_id)

    def _save_data_to_json(self, existing_data, game):
        data = json.loads(existing_data) if existing_data else {}
        save_id = str(len(data) + 1)
        data[save_id] = self._game_state_to_save_data(game)
        return json.dumps(data)

    def _game_state_to_save_data(self, game):
        return {'board': game.get_board().get_spaces(),
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
                }

    def _json_to_game_config(self, json_data, save_id):
        data = json.loads(json_data)[save_id]
        first_player = self._setup_player(data['current_player'])
        second_player = self._setup_player(data['opponent'])

        return Config(first_player, second_player, Board(data['board']))

    def _setup_player(self, json_player):
        player = self._game_config.create_player(json_player['type'], json_player['name'], json_player['marker'])
        self._game_config.set_marker_colour(player, json_player['colour'])
        return player

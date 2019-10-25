import json


class Persister:
    def save(self, game):
        pass

    def game_to_json(self, game):
        return json.dumps({'board': game.get_board().get_spaces(),
                           'current_player': {
                               'name': game.get_current_player_name(),
                               'marker': game.get_current_player_marker(),
                               'colour': game._current_player.get_marker_colour()
                           },
                           'opponent': {
                               'name': game.get_opponent_name(),
                               'marker': game.get_opponent_marker(),
                               'colour': game._opponent.get_marker_colour()
                           }
                           })
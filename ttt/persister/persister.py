import json


class Persister:
    def save(self, game):
        pass

    def game_to_json(self, game):
        return json.dumps({'board': game.get_board().get_spaces(), 'current_player': game.get_current_player_name(), 'opponent': game.get_opponent_name()})
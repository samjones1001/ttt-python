class Game:
    def __init__(self, player_one='O', player_two='X'):
        self._player_one = player_one
        self._player_two = player_two

    def get_player_one(self):
        return self._player_one

    def get_player_two(self):
        return self._player_two


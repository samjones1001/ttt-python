class Game:
    def __init__(self, player_one='O', player_two='X'):
        self._player_one = player_one
        self._player_two = player_two
        self._current_player = player_one

    def get_player_one(self):
        return self._player_one

    def get_player_two(self):
        return self._player_two

    def get_current_player(self):
        return self._current_player

    def switch_current_player(self):
        if self._current_player == self._player_one:
            self._current_player = self._player_two
        else:
            self._current_player = self._player_one
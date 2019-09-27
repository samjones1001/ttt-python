from ttt.board import Board


class Game:
    def __init__(self, game_board=Board(), player_one='O', player_two='X'):
        self._board = game_board
        self._player_one = player_one
        self._player_two = player_two
        self._current_player = player_one

    def get_player_one(self):
        return self._player_one

    def get_player_two(self):
        return self._player_two

    def get_current_player(self):
        return self._current_player

    def get_board(self):
        return self._board

    def get_board_state(self):
        return self.get_board().get_spaces()

    def switch_current_player(self):
        if self._current_player == self._player_one:
            self._current_player = self._player_two
        else:
            self._current_player = self._player_one

    def game_over(self):
        return self.get_board().is_full()

    def play_turn(self, space_index):
        self.get_board().place_symbol(
            space_index=space_index,
            symbol=self.get_current_player()
        )

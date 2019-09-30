from ttt.board import Board


class Game:
    def __init__(self, game_board=Board(), player_one='O', player_two='X'):
        self._board = game_board
        self._player_one = player_one
        self._player_two = player_two
        self._current_player = player_one
        self._win_conditions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    def get_player_one(self):
        return self._player_one

    def get_player_two(self):
        return self._player_two

    def get_current_player(self):
        return self._current_player

    def get_board_state(self):
        return self._board.get_spaces()

    def play_turn(self, space):
        self._place_marker(space)
        self._switch_current_player()

    def game_over(self):
        return self._board.is_full() or self._is_won()

    def _place_marker(self, space):
        if not self._is_valid_move(int(space)):
            raise Exception('Invalid Move!')
        self._board.place_marker(
            space=space,
            marker=self._current_player
        )

    def _switch_current_player(self):
        if self._current_player == self._player_one:
            self._current_player = self._player_two
        else:
            self._current_player = self._player_one

    def _is_valid_move(self, space):
        return self._board.is_available_space(space)

    def _is_won(self):
        for condition in self._win_conditions:
            if self._board.is_winning_line(condition):
                return True
        else:
            return False


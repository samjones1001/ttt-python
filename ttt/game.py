from ttt.board import Board
from ttt.player import Player


class Game:
    def __init__(self,
                 player_one=Player(name="Player 1", marker="O"),
                 player_two=Player(name="Player 2", marker="X"),
                 game_board=Board()):
        self._board = game_board
        self._player_one = player_one
        self._player_two = player_two
        self._current_player = player_one
        self._opponent = player_two
        self._win_conditions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    def get_current_player(self):
        return self._current_player

    def get_current_player_name(self):
        return self._current_player.get_name()

    def get_opponent(self):
        return self._opponent

    def get_opponent_name(self):
        return self._opponent.get_name()

    def get_board(self):
        return self._board

    def get_board_state(self):
        return self._board.get_spaces()

    def available_spaces(self):
        return self._board.available_spaces()

    def play_turn(self, console):
        space = self._current_player.get_move(self.get_board_state(), console)
        self._place_marker(space)
        self._switch_current_player()

    def game_over(self):
        return self.is_tie() or self.is_won()

    def is_won(self):
        for condition in self._win_conditions:
            if self._board.is_winning_line(condition):
                return True
        return False

    def is_tie(self):
        return self._board.is_full()

    def _place_marker(self, space):
        if not self._is_valid_move(int(space)):
            raise Exception('Invalid Move!')
        self._board.place_marker(
            space=space,
            marker=self._current_player.get_marker()
        )

    def _switch_current_player(self):
        self._current_player, self._opponent = self._opponent, self._current_player

    def _is_valid_move(self, space):
        return self._board.is_available_space(space)


from ttt.board import Board
from ttt.players.player import Player


class Game:
    def __init__(self,
                 player_one=Player(name="Player 1", marker="O"),
                 player_two=Player(name="Player 2", marker="X"),
                 game_board=Board()):
        self._player_one = player_one
        self._player_two = player_two
        self._board = game_board
        self._current_player = player_one
        self._opponent = player_two
        self._win_conditions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    def get_current_player(self):
        return self._current_player

    def get_current_player_name(self):
        return self._current_player.get_name()

    def get_opponent_name(self):
        return self._opponent.get_name()

    def get_board(self):
        return self._board

    def get_board_state(self):
        return self._board.get_spaces()

    def available_spaces(self):
        return self._board.available_spaces()

    def play_turn(self, console):
        space = self._current_player.get_move(self, console)

        self._board.place_marker(space=space, marker=self._current_player.get_marker())
        self._switch_current_player()

    def game_over(self):
        return self.is_tie() or self.is_won()

    def is_tie(self):
        return self._board.is_full()

    def is_won(self):
        for condition in self._win_conditions:
            line = self._board.retrieve_line(condition)
            if len(set(line)) == 1 and line[0] != '-':
                return True
        return False

    def _switch_current_player(self):
        self._current_player, self._opponent = self._opponent, self._current_player


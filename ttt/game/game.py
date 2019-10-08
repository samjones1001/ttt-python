from ttt.game.board import Board
from ttt.messages import TURN_START_MESSAGE, GAME_WON_MESSAGE, GAME_TIED_MESSAGE


class Game:
    def __init__(self, player_one, player_two, game_board=Board()):
        self._player_one = player_one
        self._player_two = player_two
        self._board = game_board
        self._current_player = player_one
        self._opponent = player_two
        self._win_conditions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    def get_current_player_name(self):
        return self._current_player.get_name()

    def get_opponent_name(self):
        return self._opponent.get_name()

    def get_current_player_marker(self):
        return self._current_player.get_marker()

    def get_opponent_marker(self):
        return self._opponent.get_marker()

    def get_board(self):
        return self._board

    def available_spaces(self):
        return self._board.available_spaces()

    def play_turn(self, console):
        console.render_board(self._board.get_spaces())
        console.output_message(self._turn_start_message())

        space = self._current_player.get_move(self)
        self._board = self._board.place_marker(space=space, marker=self._current_player.get_marker())
        self._switch_current_player()

    def game_over(self, console):
        if self.is_tie(self._board) or self.is_won(self._board, self.get_opponent_marker()):
            self._game_over_screen(console)
            return True
        return False

    def is_tie(self, board):
        return board.is_full()

    def is_won(self, board, marker):
        for condition in self._win_conditions:
            line = board.retrieve_line(condition)
            if len(set(line)) == 1 and line[0] == marker:
                return True
        return False

    def _game_over_screen(self, console):
        console.render_board(self._board.get_spaces())
        message = f"{self.get_opponent_name()}{GAME_WON_MESSAGE}" if \
            self.is_won(self._board, self.get_opponent_marker()) else \
            f"{GAME_TIED_MESSAGE}"
        console.output_message(message)

    def _switch_current_player(self):
        self._current_player, self._opponent = self._opponent, self._current_player

    def _turn_start_message(self):
        return f'{self.get_current_player_name()}{TURN_START_MESSAGE}{self.available_spaces()}'
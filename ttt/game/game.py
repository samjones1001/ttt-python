from ttt.game.board import Board
from ttt.game.game_rules import GameRules
from ttt.messages import turn_start_message, game_won_message, game_tied_message


class Game:
    def __init__(self, first_player, second_player, game_board=Board(), server=None, rules=GameRules()):
        self._board = game_board
        self._current_player = first_player
        self._opponent = second_player
        self._server = server
        self._in_progress = True
        self._rules = rules
        self._previous_move = None

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

    def get_rules(self):
        return self._rules

    def available_spaces(self):
        return self._board.available_spaces()

    def in_progress(self):
        return self._in_progress

    def start_server(self, console):
        if self._server:
            console.output_message("awaiting connection...")
            self._server.start()
            console.output_message("connection received...")


    def play_turn(self, console):
        console.render_board(self._board.get_spaces(), self._current_player, self._opponent)
        console.output_message(turn_start_message(self.get_current_player_name(),
                                                  self.get_opponent_name(),
                                                  self._previous_move))

        space = self._current_player.get_move(self)
        self._previous_move = space + 1

        self._board = self._board.place_marker(space=space, marker=self._current_player.get_marker())
        self._switch_current_player()

    def game_over(self, console):
        if self._rules.game_over(self._board, self.get_opponent_marker()):
            self._game_over_screen(console)
            self._in_progress = False
            return True
        return False

    def _game_over_screen(self, console):
        console.render_board(self._board.get_spaces(), self._current_player, self._opponent)
        message = game_won_message(self.get_opponent_name()) if \
            self._rules.is_won(self._board, self.get_opponent_marker()) else \
            game_tied_message()
        console.output_message(message)

    def _switch_current_player(self):
        self._current_player, self._opponent = self._opponent, self._current_player

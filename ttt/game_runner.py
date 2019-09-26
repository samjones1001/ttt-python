from ttt.game import Game
import ttt.interface as interface


class GameRunner:
    def __init__(self, game=Game(), output=interface):
        self._game = game
        self._output = output

    def get_game(self):
        return self._game

    def get_output(self):
        return self._output

    def play_turn(self):
        self._render_board()
        self._place_marker()
        self._switch_players()

    def is_game_over(self):
        return self.get_game().game_over()

    def _render_board(self):
        current_state = self.get_game().get_board_state()
        self._output.render_board(current_state)

    def _place_marker(self):
        space_index = self._output.get_int()
        self.get_game().play_turn(space_index)

    def _switch_players(self):
        self.get_game().switch_current_player()

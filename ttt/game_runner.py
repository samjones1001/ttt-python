from ttt.game import Game
from ttt.console import Console


class GameRunner:
    def __init__(self, game=Game(), interface=Console()):
        self._game = game
        self._interface = interface

    def get_game(self):
        return self._game

    def get_interface(self):
        return self._interface

    def run(self):
        game_in_progress = True

        while game_in_progress:
            self._render_board()
            self._place_marker()
            if self._is_game_over():
                self._render_board()
                game_in_progress = False

    def _is_game_over(self):
        return self.get_game().game_over()

    def _render_board(self):
        current_state = self.get_game().get_board_state()
        self._interface.render_board(current_state)

    def _place_marker(self):
        space_index = self._interface.get_int()
        self.get_game().play_turn(space_index)


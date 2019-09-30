from ttt.game import Game
from ttt.console import Console


class GameRunner:
    def __init__(self, game=Game(), console=Console()):
        self._game = game
        self._console = console

    def get_game(self):
        return self._game

    def get_console(self):
        return self._console

    def run(self):
        game_in_progress = True

        while game_in_progress:
            self._render_board()
            self._place_marker()
            if self._is_game_over():
                self._render_board()
                game_in_progress = False

    def _is_game_over(self):
        return self._game.game_over()

    def _render_board(self):
        current_state = self._game.get_board_state()
        self._console.render_board(current_state)

    def _place_marker(self):
        try:
            space_index = self._console.get_int()
            self._game.play_turn(space_index)
        except Exception as ex:
            self._print_message(ex)

    def _print_message(self, string):
        self._console.output_message(string)


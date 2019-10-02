from ttt.game import Game
from ttt.board import Board
from ttt.console import Console


class GameRunner:
    def __init__(self, console=Console()):
        self._console = console
        self._game = None

    def get_game(self):
        return self._game

    def run(self, player_1, player_2, game=Game, board=Board):
        board = board()
        self._game = game(player_1, player_2, board)
        game_in_progress = True
        self._render_board()

        while game_in_progress:
            self._place_marker()
            self._render_board()
            if self._is_game_over():
                game_in_progress = False

    def _is_game_over(self):
        return self._game.game_over()

    def _render_board(self):
        current_state = self._game.get_board_state()
        self._console.render_board(current_state)

    def _place_marker(self):
        try:
            self._game.play_turn(self._console)
        except Exception as ex:
            self._print_message(ex)

    def _print_message(self, string):
        self._console.output_message(string)


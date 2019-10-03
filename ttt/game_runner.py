from ttt.game import Game
from ttt.board import Board
from ttt.console import Console
from ttt.messages import TURN_START_MESSAGE


class GameRunner:
    def __init__(self, console=Console()):
        self._console = console
        self._game = None

    def get_game(self):
        return self._game

    def run(self, player_1, player_2, game=Game, board=Board):
        board = board()
        self._game = game(player_1, player_2, board)

        self._console.render_board(self._game)
        while not self._game.game_over():
            self._run_turn()
        self._console.show_game_over_message(self._game)

    def _run_turn(self):
        self._console.output_message(self._turn_start_message())
        self._game.play_turn(self._console)
        self._console.render_board(self._game)

    def _turn_start_message(self):
        return f'{self._game.get_current_player_name()}{TURN_START_MESSAGE}{self._game.available_spaces()}'


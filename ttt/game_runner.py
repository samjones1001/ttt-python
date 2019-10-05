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

        while not self._game.game_over():
            self._game.play_turn(self._console)
        self._game.show_game_over_screen(self._console)



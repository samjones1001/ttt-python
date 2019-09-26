from ttt.game import Game
import ttt.interface as interface


class GameRunner:
    def __init__(self, game=Game(), output=interface):
        self._game = game
        self._output = output

    def get_game(self):
        return self._game


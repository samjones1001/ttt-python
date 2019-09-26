from ttt.game import Game


class GameRunner():
    def __init__(self, game=Game()):
        self._game = game

    def get_game(self):
        return self._game
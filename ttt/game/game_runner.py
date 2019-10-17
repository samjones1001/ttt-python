from ttt.game.game import Game
from ttt.console_ui.console import Console


class GameRunner:
    def __init__(self, console=Console()):
        self._console = console
        self._game = None

    def get_game(self):
        return self._game

    def run(self, first_player, second_player, game=Game):
        self._game = game(first_player, second_player)

        while not self._game.game_over(self._console):
            self._game.play_turn(self._console)



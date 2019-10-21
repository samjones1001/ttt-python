from ttt.console_ui.console import Console
from ttt.game.game_config import Config


class GameRunner:
    def __init__(self, console=Console()):
        self._console = console
        self._game = None

    def get_game(self):
        return self._game

    def run(self, game_config: Config):
        self._game = game_config.game(game_config.first_player, game_config.second_player)

        while not self._game.game_over(self._console):
            self._game.play_turn(self._console)

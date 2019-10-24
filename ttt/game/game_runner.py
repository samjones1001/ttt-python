from ttt.console_ui.console import Console
from ttt.game.game_config import Config
from ttt.persister.persister import Persister


class GameRunner:
    def __init__(self, console=Console(), persister=Persister()):
        self._console = console
        self._game = None
        self._persister = persister

    def get_game(self):
        return self._game

    def run(self, game_config: Config):
        self._game = game_config.game(game_config.first_player, game_config.second_player)

        while not self._game.game_over(self._console):
            self._game.play_turn(self._console)

    def stop(self):
        if self._game and self._game.in_progress():
            self._persister.save(self._game)
from ttt import constants
from ttt.console_ui.console import Console
from ttt.game.game import Game
from ttt.game.game_config import Config
from ttt.messages import game_saved_message
from ttt.persister.persister import Persister


class GameRunner:
    def __init__(self, console=Console(), persister=Persister(), game_class=Game):
        self._console = console
        self._persister = persister
        self._game_class = game_class
        self._game = None

    def get_game(self):
        return self._game

    def run(self, game_config: Config):
        self._game = self._game_class(game_config.first_player, game_config.second_player, game_config.board)
        while not self._game.game_over(self._console):
            self._game.play_turn(self._console)

    def stop(self):
        if self._game and self._game.in_progress():
            save_id = self._persister.save(constants.SAVE_GAME_REPO_PATH, self._game)
            self._console.output_message(game_saved_message(save_id))
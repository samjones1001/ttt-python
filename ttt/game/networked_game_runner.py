from ttt.console_ui.console import Console
from ttt.game.game import Game
from ttt.game.game_config import Config
from ttt.messages import turn_start_message, awaiting_connection_message


class NetworkedGameRunner:
    def __init__(self, console=Console(), game_class=Game):
        self._console = console
        self._game_class = game_class
        self._game = None
        self._server = None

    def get_game(self):
        return self._game

    def run(self, game_config: Config):
        self._server = game_config.server
        self._console.output_message(awaiting_connection_message())
        self._server.start()

        self._game = self._game_class(game_config.first_player, game_config.second_player, game_config.board)

        while not self._game.game_over(self._console):
            board_string = self._console.build_board_output(self._game.all_spaces(),
                                                            self._game.get_current_player(),
                                                            self._game.get_opponent())
            message = turn_start_message(self._game.get_current_player_name(),
                                         self._game.get_opponent_name(),
                                         self._game.get_previous_move())
            game_string = f'{board_string}\n\n{message}'

            self._server.send_data(game_string)
            self._game.play_turn(self._console)
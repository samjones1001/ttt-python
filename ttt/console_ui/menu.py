from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer
from ttt.game.game_runner import GameRunner
from ttt.messages import WELCOME_MESSAGE


class Menu:
    def __init__(self, console):
        self._console = console
        self._runner = None

    def start(self, game_runner=None):
        self._set_runner(game_runner)
        self._console.output_message(WELCOME_MESSAGE)
        player_1 = HumanPlayer('Player 1', 'O', self._console)
        player_2 = self._select_player_type('Player 2', 'X')

        self._runner.run(player_1, player_2)

    def _set_runner(self, game_runner):
        if game_runner is None:
            self._runner = GameRunner(self._console)
        else:
            self._runner = game_runner

    def _select_player_type(self, name, marker):
        user_input = self._console.get_valid_input(['1', '2', '3'], "Please select an option from the menu")
        if user_input == '1':
            return HumanPlayer(name, marker, self._console)
        elif user_input == '2':
            return SimpleComputerPlayer(name, marker)
        elif user_input == '3':
            return SmartComputerPlayer(name, marker)


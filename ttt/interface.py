from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.game_runner import GameRunner
from ttt.messages import WELCOME_MESSAGE


class Interface:
    def __init__(self, console):
        self._console = console
        self._runner = None

    def start(self, game_runner=GameRunner):
        self._console.output_message(WELCOME_MESSAGE)
        player_1 = HumanPlayer('Player 1', 'O', self._console)
        player_2 = self._select_player_type('Player 2', 'X')
        self._runner = game_runner(self._console)

        self._runner.run(player_1, player_2)

    def _select_player_type(self, name, marker):
        user_input = self._console.get_valid_input(['1', '2'], "Please select an option from the menu")
        if user_input == '1':
            return HumanPlayer(name, marker, self._console)
        elif user_input == '2':
            return SimpleComputerPlayer(name, marker)


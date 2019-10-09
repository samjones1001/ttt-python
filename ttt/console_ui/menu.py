from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer
from ttt.game.game_runner import GameRunner
from ttt.messages import welcome_message, player_type_message, marker_message, invalid_marker_message


class Menu:
    def __init__(self, console):
        self._console = console
        self._runner = None

    def start(self, game_runner=None):
        self._set_runner(game_runner)
        self._console.output_message(welcome_message())

        player_1 = self._setup_player('Player 1', 'O', None)
        player_2 = self._setup_player('Player 2',
                                      self._select_default_marker(player_1.get_marker()),
                                      player_1.get_marker())

        self._runner.run(player_1, player_2)

    def _set_runner(self, game_runner):
        if game_runner is None:
            self._runner = GameRunner(self._console)
        else:
            self._runner = game_runner

    def _setup_player(self, name, marker, unavailable_marker):
        self._console.output_message(player_type_message(name))
        player = self._select_player_type(name, marker)

        self._console.output_message(marker_message(name, marker))
        player.set_marker()
        player = self._check_marker_validity(player, unavailable_marker)

        return player

    def _select_player_type(self, name, marker):
        user_input = self._console.get_validated_input('^[/1/2/3]$', "Please select an option from the menu")

        if user_input == '1':
            return HumanPlayer(name, marker, self._console)
        elif user_input == '2':
            return SimpleComputerPlayer(name, marker, self._console)
        elif user_input == '3':
            return SmartComputerPlayer(name, marker, self._console)

    def _select_default_marker(self, taken_marker):
        return 'O' if taken_marker == 'X' else 'X'

    def _check_marker_validity(self, player, unavailable_marker):
        while player.get_marker() == unavailable_marker:
            self._console.output_message(invalid_marker_message())
            player.set_marker()
        return player



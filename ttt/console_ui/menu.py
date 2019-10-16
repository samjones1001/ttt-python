import ttt.constants as constants
from ttt.players.player_factory import PlayerFactory
from ttt.game.game_runner import GameRunner
from ttt.messages import welcome_message, player_type_message, marker_message, invalid_marker_message


class Menu:
    def __init__(self, console, runner=None):
        self._console = console
        self._runner = self._set_runner(runner)

    def start(self):
        self._console.clear_output()
        self._console.output_message(welcome_message())

        player_1 = self._setup_player(constants.PLAYER_1_NAME, constants.PLAYER_1_MARKER, None)
        player_2 = self._setup_player(constants.PLAYER_2_NAME,
                                      self._select_default_marker(player_1.get_marker()),
                                      player_1.get_marker())

        self._runner.run(player_1, player_2)
        self._play_again()

    def _set_runner(self, game_runner):
        if game_runner is None:
            return GameRunner(self._console)
        return game_runner

    def _setup_player(self, name, marker, taken_marker):
        self._console.output_message(player_type_message(name))
        player = self._select_player_type(name, marker)
        self._console.clear_output()

        self._select_marker(player, taken_marker)
        self._console.clear_output()

        return player

    def _select_player_type(self, name, marker, factory=None):
        if factory is None:
            factory = PlayerFactory()

        choices = {'1': constants.HUMAN_PLAYER_STRING,
                   '2': constants.SIMPLE_COMPUTER_STRING,
                   '3': constants.SMART_COMPUTER_STRING}

        user_input = self._console.get_validated_input(constants.PLAYER_SELECTION_REGEX, constants.MENU_ERROR)
        return factory.create(choices[user_input], name, marker, self._console)

    def _select_marker(self, player, taken_marker):
        self._console.output_message(marker_message(player.get_name(), player.get_marker()))
        marker_choice = self._console.get_validated_input(constants.NORMAL_MARKER_REGEX, constants.MARKER_ERROR)

        if not self._is_marker_availabile(marker_choice, taken_marker):
            self._console.output_message(invalid_marker_message())
            return self._select_marker(player, taken_marker)
        elif marker_choice != '':
            player.set_marker(marker_choice)
        return player

    def _select_default_marker(self, taken_marker):
        return constants.PLAYER_1_MARKER if taken_marker == constants.PLAYER_2_MARKER else constants.PLAYER_2_MARKER

    def _is_marker_availabile(self, selected_marker, taken_marker):
        return selected_marker != taken_marker

    def _play_again(self):
        user_choice = self._console.get_validated_input(constants.PLAY_AGAIN_REGEX, constants.MENU_ERROR)
        if user_choice.lower() == 'y':
            self.start()


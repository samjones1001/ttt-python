import re

import ttt.constants as constants
from ttt.game.board import Board
from ttt.game.game_config import GameConfig
from ttt.messages import welcome_message, player_type_message, marker_message, player_choice_message, end_game_message, \
    play_again_message, colour_message, load_game_message, load_game_error_message
from ttt.persister.persister import Persister


class Menu:
    def __init__(self, console, game_config=GameConfig, persister=Persister()):
        self._console = console
        self._game_config = game_config(console)
        self._persister = persister

    def start(self):
        self._console.clear_output()
        self._console.output_message(welcome_message())
        selection = self._console.get_validated_input(constants.TWO_OPTION_MENU_REGEX, constants.MENU_ERROR)
        self._console.clear_output()

        return self._configure_game() if selection is constants.PLAY_NEW_GAME_CHAR else self.load_game()

    def load_game(self):
        self._console.output_message(load_game_message())
        id = self._console.get_validated_input(constants.LOAD_GAME_ID_REGEX, constants.NUMBER_ERROR)

        try:
            return self._persister.load(constants.SAVE_GAME_REPO_PATH, id)
        except:
            self._console.clear_output()
            self._console.output_message(load_game_error_message(id))
            return self.load_game()

    def play_again(self):
        self._console.output_message(play_again_message())

        user_choice = self._console.get_validated_input(constants.PLAY_AGAIN_REGEX, constants.MENU_ERROR)
        if user_choice.lower() == constants.CONFIRMATION_CHAR:
            return True
        self.exit()
        return False

    def exit(self):
        self._console.clear_output()
        self._console.output_message(end_game_message())

    def _configure_game(self, board=Board()):
        player_1 = self._setup_player(constants.PLAYER_1_NAME, constants.PLAYER_1_MARKER, None)
        player_2 = self._setup_player(constants.PLAYER_2_NAME,
                                      self._game_config.select_default_marker(player_1.get_marker()),
                                      player_1.get_marker())

        player_order = self._select_player_order(player_1, player_2)
        return self._game_config.create_config_object(player_order[0], player_order[1], board)

    def _setup_player(self, name, marker, taken_marker):
        player = self._select_player_type(name, marker)
        self._select_marker(player, taken_marker)
        return player

    def _select_player_type(self, name, marker):
        self._console.output_message(player_type_message(name))
        user_choice = constants.PLAYER_CHOICES[self._console.get_validated_input(constants.THREE_OPTION_MENU_REGEX, constants.MENU_ERROR)]
        self._console.clear_output()

        return self._game_config.create_player(user_choice, name, marker)

    def _select_marker(self, player, taken_marker):
        self._console.output_message(marker_message(player.get_name(), player.get_marker()))
        marker_choice = self._console.get_validated_input(constants.MARKER_REGEX, constants.MARKER_ERROR)
        updated_player = self._game_config.set_player_marker(player, taken_marker, marker_choice)
        self._console.clear_output()

        if not updated_player:
            return self._select_marker(player, taken_marker)
        self._select_marker_colour(player)

    def _select_marker_colour(self, player):
        if not re.match(constants.EMOJI_REGEX, player.get_marker()):
            self._console.output_message(colour_message(player.get_name()))
            colour_choice = self._console.get_validated_input(constants.COLOUR_REGEX, constants.MENU_ERROR)
            self._game_config.set_marker_colour(player, colour_choice)
            self._console.clear_output()
        else:
            self._game_config.set_marker_colour(player, constants.NO_COLOUR)

    def _select_player_order(self, player_1, player_2):
        self._console.output_message(player_choice_message())

        user_choice = self._console.get_validated_input(constants.TWO_OPTION_MENU_REGEX, constants.MENU_ERROR)
        return [player_1, player_2] if user_choice == '1' else [player_2, player_1]

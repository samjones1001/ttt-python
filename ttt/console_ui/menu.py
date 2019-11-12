import re

import ttt.constants as constants
from ttt.game.board import Board
from ttt.game.game_config import GameConfig
from ttt.messages import welcome_message, player_type_message, marker_message, player_choice_message, end_game_message, \
    play_again_message, colour_message, load_game_message, load_game_error_message, new_or_load_message
from ttt.networking.ttt_server import TTTServer
from ttt.persister.persister import Persister


class Menu:
    def __init__(self, console, game_config=GameConfig, persister=Persister()):
        self._console = console
        self._game_config = game_config(console)
        self._persister = persister
        self._server = None

    def start(self):
        selection = self._select_game_type()
        if selection == constants.TWO_CHAR:
            self._server = TTTServer()
            return self._configure_game(is_networked=True)

        self._console.output_message(new_or_load_message())
        selection = self._console.get_validated_input(constants.TWO_OPTION_MENU_REGEX, constants.MENU_ERROR)
        return self._configure_game() if selection is constants.ONE_CHAR else self.load_game()

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

    def _select_game_type(self):
        self._console.clear_output()
        self._console.output_message(welcome_message())
        selection = self._console.get_validated_input(constants.TWO_OPTION_MENU_REGEX, constants.MENU_ERROR)
        self._console.clear_output()
        return selection

    def _configure_game(self, is_networked=False, board=Board()):
        player_1 = self._setup_player(constants.PLAYER_1_NAME, constants.PLAYER_1_MARKER)
        player_2 = self._setup_player(constants.PLAYER_2_NAME,
                                                self._game_config.select_default_marker(player_1.get_marker()),
                                                player_1.get_marker(),
                                                is_networked)

        player_order = self._select_player_order(player_1, player_2)
        return self._game_config.create_config_object(player_order[0], player_order[1], board, self._server)

    def _setup_player(self, name, marker, taken_marker=None, is_networked_player=False):
        player = self._select_player_type(name, marker, is_networked_player)
        self._select_marker(player, taken_marker)
        return player

    def _select_player_type(self, name, marker, is_networked_player):
        if not is_networked_player:
            self._console.output_message(player_type_message(name))
            type = constants.PLAYER_CHOICES[self._console.get_validated_input(constants.THREE_OPTION_MENU_REGEX, constants.MENU_ERROR)]
            self._console.clear_output()
            return self._game_config.create_player(type, name, marker)
        else:
            type = constants.NETWORKED_PLAYER_STRING
            return self._game_config.create_player(type, name, marker, self._server)

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
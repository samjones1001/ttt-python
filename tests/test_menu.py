import json

import pytest

from tests.mocks import MockConsole, MockConsoleIO, MockPersisterIO
from ttt import constants
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.messages import play_again_message, end_game_message
from ttt.persister.persister import Persister
from ttt.players.human_player import HumanPlayer
from ttt.players.networked_human_player import NetworkedHumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer


@pytest.fixture
def save_game_json_data():
    save_data = {'1': {
                    'board': ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9'],
                    'current_player': {
                        'name': 'Player 1',
                        'type': 'SimpleComputerPlayer',
                        'marker': 'O',
                        'colour': ''
                    },
                    'opponent': {
                        'name': 'Player 2',
                        'type': 'SimpleComputerPlayer',
                        'marker': 'O',
                        'colour': ''
                    }
                }}

    return json.dumps(save_data)


def test_if_user_selects_a_network_game_player_2_will_be_a_networked_human_player():
    menu = Menu(MockConsole(['2', '1', '', '', '', '', '1']))

    config = menu.start()

    assert isinstance(config.second_player, NetworkedHumanPlayer)


def test_config_object_for_a_local_game_does_not_hold_a_server():
    menu = Menu(MockConsole(['1', '1', '1', '', '', '1', '', '', '1']))

    config = menu.start()

    assert config.server is None


def test_config_object_for_a_networked_game_holds_a_server():
    menu = Menu(MockConsole(['2', '1', '', '', '', '', '1']))

    config = menu.start()

    assert config.server is not None


def test_user_can_select_player_types():
    menu = Menu(MockConsole(['1', '1', '1', '', '', '2', '', '', '1']))

    config = menu.start()

    assert isinstance(config.first_player, HumanPlayer)
    assert isinstance(config.second_player, SimpleComputerPlayer)


def test_user_can_select_a_custom_marker():
    menu = Menu(MockConsole(['1', '1', '1', '!', '', '2', '', '', '1']))

    config = menu.start()

    assert config.first_player.get_marker() == '!'


def test_user_can_select_a_colour_for_their_marker():
    menu = Menu(MockConsole(['1', '1', '1', '!', '1', '2', '', '', '1']))

    config = menu.start()

    assert config.first_player.get_marker_colour() == constants.COLOURS['1']


def test_users_are_not_prompted_to_select_a_colour_for_emoji_markers():
    menu = Menu(MockConsole(['1', '1', '1', '👍', '2', '😀', '1']))

    config = menu.start()

    assert config.first_player.get_marker_colour() == constants.COLOURS['']
    assert config.second_player.get_marker_colour() == constants.COLOURS['']


def test_user_can_select_a_custom_emoji_marker():
    menu = Menu(MockConsole(['1', '1', '1', '👍', '1', '', '', '1']))

    config = menu.start()

    assert config.first_player.get_marker() == '👍'


def test_a_user_will_continue_to_be_prompted_if_they_provide_an_integer_as_a_marker():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', '5', '2', '7', '!', '', '1', '', '', '1'])))

    config = menu.start()

    assert config.first_player.get_marker() == '!'


def test_a_player_will_continue_to_be_prompted_if_they_provide_whitespace_as_a_marker():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', ' ', ' ', '   ', '!', '', '1', '', '', '1'])))

    config = menu.start()

    assert config.first_player.get_marker() == '!'


def test_a_player_will_retain_their_default_marker_if_they_provide_an_empty_string():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', '', '', '1', '', '', '1'])))

    config = menu.start()

    assert config.first_player.get_marker() == 'O'


def test_if_player_one_selects_x_as_marker_player_two_default_marker_changes_to_o():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', 'X', '', '1', '', '', '1', 'n'])))

    config = menu.start()

    assert config.second_player.get_marker() == 'O'


def test_user_cannot_select_the_same_marker_as_their_opponent():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', 'X', '', '2', 'X', 'O', '', '1'])))

    config = menu.start()

    assert config.second_player.get_marker() == 'O'


def test_user_can_reverse_the_order_of_turns():
    menu = Menu(Console(MockConsoleIO(['1', '1', '1', 'X', '', '2', 'O', '', '2'])))

    config = menu.start()

    assert config.first_player.get_name() == 'Player 2'


def test_console_is_cleared_after_each_message_is_printed():
    inputs = ['1', '1', '1', 'X', '', '2', 'O', '', '2', 'n']
    console = MockConsole(inputs)
    menu = Menu(console)

    menu.start()

    assert console.clear_output_call_count == len(inputs) - 2


def test_user_can_choose_to_load_an_existing_game(save_game_json_data):
    inputs = ['1', '2', '1']
    persister_io = MockPersisterIO(save_game_json_data)
    persister = Persister(persister_io)
    console = MockConsole(inputs)
    menu = Menu(console, persister=persister)

    config = menu.start()

    assert config.first_player.get_name() == "Player 1"
    assert config.second_player.get_name() == "Player 2"
    assert config.board.get_spaces() == ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9']


def test_user_will_continue_to_be_prompted_if_they_provide_an_invalid_save_id(save_game_json_data):
    inputs = ['1', '2', '2', '5', '1']
    persister_io = MockPersisterIO(save_game_json_data)
    persister = Persister(persister_io)
    console = MockConsole(inputs)
    menu = Menu(console, persister=persister)

    config = menu.start()

    assert config.first_player.get_name() == "Player 1"
    assert config.second_player.get_name() == "Player 2"
    assert config.board.get_spaces() == ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9']


def test_user_has_the_option_to_play_again():
    io = MockConsoleIO(['y'])
    console = Console(io)
    menu = Menu(console)

    play_again = menu.play_again()

    assert io.last_output == play_again_message()
    assert play_again


def test_user_has_the_option_not_to_play_again():
    io = MockConsoleIO(['n'])
    console = Console(io)
    menu = Menu(console)

    play_again = menu.play_again()

    assert io.last_output == end_game_message()
    assert not play_again


def test_exits_the_game():
    io = MockConsoleIO([])
    console = Console(io)
    menu = Menu(console)

    menu.exit()

    assert io.last_output == end_game_message()

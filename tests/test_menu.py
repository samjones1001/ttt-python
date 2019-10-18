import pytest
from ttt.console_ui.menu import Menu
from ttt.console_ui.console import Console
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from tests.mocks import MockConsole, MockGameRunner, MockConsoleIO


class TestRunner:
    def start_menu(self, inputs, game_runner):
        menu = Menu(MockConsole(inputs), game_runner)
        menu.start()


@pytest.fixture
def test_runner():
    return TestRunner()


@pytest.fixture
def game_runner():
    return MockGameRunner('console')


def test_starting_a_game_requests_the_game_runner_to_run(test_runner, game_runner):
    test_runner.start_menu(['1', '', '1', '', 'y', 'n'], game_runner)

    assert game_runner.run_call_count == 1


def test_user_can_select_player_types(test_runner, game_runner):
    test_runner.start_menu(['1', '', '2', '', 'y', 'n'], game_runner)

    assert isinstance(game_runner.first_player, HumanPlayer)
    assert isinstance(game_runner.second_player, SimpleComputerPlayer)


def test_user_can_select_a_custom_marker(test_runner, game_runner):
    test_runner.start_menu(['1', '!', '2', '', 'y', 'n'], game_runner)

    assert game_runner.first_player.get_marker() == '!'


def test_user_can_select_a_custom_emoji_marker(test_runner, game_runner):
    test_runner.start_menu(['1', '👍', '1', '', 'y', 'n'], game_runner)

    assert game_runner.first_player.get_marker() == '👍'


def test_a_user_will_continue_to_be_prompted_if_they_provide_an_integer_as_a_marker(game_runner):
    console = Console(MockConsoleIO(['1', '1', '5', '2', '7', '!', '1', '1', '', 'y', 'n']))
    menu = Menu(console, game_runner)
    menu.start()

    assert game_runner.first_player.get_marker() == '!'


def test_a_player_will_continue_to_be_prompted_if_they_provide_whitespace_as_a_marker(game_runner):
    console = Console(MockConsoleIO(['1', ' ', ' ', '   ', '!', '1', '', 'y', 'n']))
    menu = Menu(console, game_runner)
    menu.start()

    assert game_runner.first_player.get_marker() == '!'


def test_a_player_will_retain_their_default_marker_if_they_provide_an_empty_string(game_runner):
    console = Console(MockConsoleIO(['1', '1', '', '1', '1', '', 'y', 'n']))
    menu = Menu(console, game_runner)
    menu.start()

    assert game_runner.first_player.get_marker() == 'O'


def test_if_player_one_selects_x_as_marker_player_two_default_marker_changes_to_o(test_runner, game_runner):
    test_runner.start_menu(['1', 'X', '1', '', 'y', 'n'], game_runner)

    assert game_runner.second_player.get_marker() == 'O'


def test_user_cannot_select_the_same_marker_as_their_opponent(test_runner, game_runner):
    test_runner.start_menu(['1', 'X', '2', 'X', 'O', 'y', 'n'], game_runner)

    assert game_runner.second_player.get_marker() == 'O'


def test_user_can_reverse_the_order_of_turns(test_runner, game_runner):
    test_runner.start_menu(['1', 'X', '2', 'O', 'n', 'n'], game_runner)
    assert game_runner.first_player.get_name() == 'Player 2'


def test_console_is_cleared_after_each_message_is_printed():
    number_of_messages = 5
    console = MockConsole(['1', '', '1', '', 'y', 'n'])
    runner = MockGameRunner('console')
    menu = Menu(console, runner)
    menu.start()

    assert console.clear_output_call_count == number_of_messages

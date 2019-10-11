import pytest
from ttt.console_ui.menu import Menu
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from tests.mocks import MockConsole, MockGameRunner


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
    test_runner.start_menu(['1', '', '1', '', 'n'], game_runner)

    assert game_runner.run_call_count == 1


def test_user_can_select_player_types(test_runner, game_runner):
    test_runner.start_menu(['1', '', '2', '', 'n'], game_runner)

    assert isinstance(game_runner.player_1, HumanPlayer)
    assert isinstance(game_runner.player_2, SimpleComputerPlayer)


def test_if_player_one_selects_x_as_marker_player_two_default_marker_changes_to_o(test_runner, game_runner):
    test_runner.start_menu(['1', 'X', '1', '', 'n'], game_runner)

    assert game_runner.player_2.get_marker() == 'O'


def test_user_cannot_select_the_same_marker_as_their_opponent(test_runner, game_runner):
    test_runner.start_menu(['1', 'X', '2', 'X', 'O', 'n'], game_runner)

    assert game_runner.player_2.get_marker() == 'O'


def test_console_is_cleared_after_each_message_is_printed():
    number_of_messages = 5
    console = MockConsole(['1', '', '1', '', 'n'])
    runner = MockGameRunner('console')
    menu = Menu(console, runner)
    menu.start()

    assert console.clear_output_call_count == number_of_messages

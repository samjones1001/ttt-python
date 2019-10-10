from ttt.console_ui.menu import Menu
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from tests.mocks import MockConsole, MockGameRunner


def test_starting_a_game_requests_the_game_runner_to_run():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', '', '1', '']), runner)
    menu.start()

    assert runner.run_call_count == 1


def test_user_can_select_player_types():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', '', '2', '']), runner)
    menu.start()

    assert isinstance(runner.player_1, HumanPlayer)
    assert isinstance(runner.player_2, SimpleComputerPlayer)


def test_if_player_one_selects_x_as_marker_player_two_default_marker_changes_to_o():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', 'X', '1', '']), runner)
    menu.start()

    assert runner.player_2.get_marker() == 'O'


def test_user_cannot_select_the_same_marker_as_their_opponent():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', 'X', '2', 'X', 'O']), runner)
    menu.start()

    assert runner.player_2.get_marker() == 'O'


def test_console_is_clearer_after_each_message_is_printed():
    number_of_messages = 4
    console = MockConsole(['1', '', '1', ''])
    runner = MockGameRunner('console')
    menu = Menu(console, runner)
    menu.start()

    assert console.clear_output_call_count == number_of_messages
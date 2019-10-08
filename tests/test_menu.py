from ttt.console_ui.menu import Menu
from ttt.console_ui.console import Console
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer
from tests.mocks import MockConsole, MockGameRunner, MockConsoleIO


def test_starting_a_game_requests_the_game_runner_to_run():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', '']))
    menu.start(runner)

    assert runner.run_call_count == 1


def test_user_can_select_a_human_opponent():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['1', '']))
    menu.start(runner)

    assert isinstance(runner.player_2, HumanPlayer)


def test_user_can_select_a_simple_computer_opponent():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['2', '']))
    menu.start(runner)

    assert isinstance(runner.player_2, SimpleComputerPlayer)


def test_user_can_select_a_smart_computer_opponent():
    runner = MockGameRunner('console')
    menu = Menu(MockConsole(inputs=['3', '']))
    menu.start(runner)

    assert isinstance(runner.player_2, SmartComputerPlayer)

from ttt.console_ui.interface import Interface
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer
from tests.mocks import MockConsole, MockGameRunner


def test_starting_a_game_requests_a_welcome_message_be_displayed():
    runner = MockGameRunner
    console = MockConsole(input_return='1')
    interface = Interface(console)
    interface.start(runner)

    assert console.output_message_call_count == 1


def test_starting_a_game_requests_the_game_runner_to_run():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return='1'))
    interface.start(runner)

    assert interface._runner.run_call_count == 1


def test_user_can_select_a_human_opponent():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return='1'))
    interface.start(runner)

    assert isinstance(interface._runner.player_2, HumanPlayer)


def test_user_can_select_a_simple_computer_opponent():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return='2'))
    interface.start(runner)

    assert isinstance(interface._runner.player_2, SimpleComputerPlayer)


def test_user_can_select_a_smart_computer_opponent():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return='3'))
    interface.start(runner)

    assert isinstance(interface._runner.player_2, SmartComputerPlayer)
from ttt.interface import Interface
from ttt.player import Player
from ttt.computer_player import ComputerPlayer

class MockGameRunner():
    def __init__(self, console):
        self.run_call_count = 0
        self.player_2 = None

    def run(self, player_1, player_2):
        self.run_call_count += 1
        self.player_2 = player_2


class MockConsole():
    def __init__(self, input_return):
        self.input_return = input_return

    def get_int(self):
       return self.input_return


def test_starting_a_game_requests_the_game_runner_to_run():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return=1))
    interface.start(runner)

    assert interface._runner.run_call_count == 1


def test_user_can_select_a_human_opponent():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return=1))
    interface.start(runner)

    assert isinstance(interface._runner.player_2, Player)


def test_user_can_select_a_computer_opponent():
    runner = MockGameRunner
    interface = Interface(MockConsole(input_return=2))
    interface.start(runner)

    assert isinstance(interface._runner.player_2, ComputerPlayer)
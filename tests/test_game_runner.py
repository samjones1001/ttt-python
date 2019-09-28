import pytest
from ttt.game_runner import GameRunner


class MockGame:
    def __init__(self):
        self.get_board_state_call_count = 0
        self.play_turn_call_count = 0
        self.switch_player_call_count = 0
        self.game_over_call_count = 0

    def get_board_state(self):
        self.get_board_state_call_count += 1

    def play_turn(self, _):
        self.play_turn_call_count += 1

    def game_over(self):
        self.game_over_call_count += 1
        if self.game_over_call_count >= 9:
            return True


class MockConsole:
    def __init__(self):
        self.render_board_call_count = 0
        self.get_int_call_count = 0

    def render_board(self, _):
        self.render_board_call_count += 1

    def get_int(self):
        self.get_int_call_count += 1


@pytest.fixture
def game_runner():
    return GameRunner(game=MockGame(), console=MockConsole())


def test_returns_a_game():
    game = MockGame()
    runner = GameRunner(game=game, console=MockConsole())
    assert runner.get_game() == game


def test_returns_the_interface():
    console = MockConsole()
    runner = GameRunner(game=MockGame(), console=console)
    assert runner.get_console() == console


def test_run_requests_current_board_state_each_turn_and_on_game_over(game_runner):
    number_of_turns_plus_game_over = 10
    game_runner.run()
    assert game_runner.get_game().get_board_state_call_count == number_of_turns_plus_game_over


def test_run_requests_board_to_be_printed_each_turn_and_on_game_over(game_runner):
    number_of_turns_plus_game_over = 10
    game_runner.run()
    assert game_runner.get_console().render_board_call_count == number_of_turns_plus_game_over


def test_run_requests_input_each_turn(game_runner):
    number_of_turns = 9
    game_runner.run()
    assert game_runner.get_console().get_int_call_count == number_of_turns


def test_run_requests_move_to_be_made_each_turn(game_runner):
    number_of_turns = 9
    game_runner.run()
    assert game_runner.get_game().play_turn_call_count == number_of_turns


def test__run_checks_game_for_game_over_state_each_turn(game_runner):
    number_of_turns = 9
    game_runner.run()
    assert game_runner.get_game().game_over_call_count == number_of_turns



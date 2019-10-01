import pytest
from ttt.game_runner import GameRunner
from ttt.game import Game


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
        self.last_output = None

    def render_board(self, _):
        self.render_board_call_count += 1

    def get_int(self):
        self.get_int_call_count += 1
        return '1'

    def output_message(self, message):
        self.last_output = message


class MockBoardGameOverState:
    def __init__(self):
        self.get_spaces_call_count = 0
        self.is_full_call_count = 0
        self.place_marker_call_count = 0
        self.is_winning_line_call_count = 0

    def get_spaces(self):
        self.get_spaces_call_count += 1

    def is_full(self):
        self.is_full_call_count += 1

    def place_marker(self, space, marker):
        self.place_marker_call_count += 1

    def is_valid_space(self, space):
        return True

    def is_winning_line(self, line):
        self.is_winning_line_call_count += 1
        return True


@pytest.fixture
def game_runner():
    return GameRunner(game=Game(game_board=MockBoardGameOverState()), console=MockConsole())


def test_run_requests_current_board_state_each_turn_and_on_game_over():
    board = MockBoardGameOverState()
    times_requested_on_final_turn_and_game_over = 2
    game_runner = GameRunner(game=Game(game_board=board), console=MockConsole())

    game_runner.run()

    assert board.get_spaces_call_count == times_requested_on_final_turn_and_game_over


def test_run_requests_board_to_be_printed_each_turn_and_on_game_over(game_runner):
    times_printed_on_final_turn_and_game_over = 2
    game_runner.run()

    assert game_runner.get_console().render_board_call_count == times_printed_on_final_turn_and_game_over


def test_run_requests_input_each_turn(game_runner):
    game_runner.run()

    assert game_runner.get_console().get_int_call_count == 1


def test_run_requests_move_to_be_made_each_turn():
    board = MockBoardGameOverState()
    game_runner = GameRunner(game=Game(game_board=board), console=MockConsole())

    game_runner.run()

    assert board.place_marker_call_count == 1


def test_run_checks_game_for_game_over_state_each_turn():
    board = MockBoardGameOverState()
    game_runner = GameRunner(game=Game(game_board=board), console=MockConsole())

    game_runner.run()

    assert board.is_full_call_count == 1
    assert board.is_winning_line_call_count == 1


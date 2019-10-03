import pytest
from ttt.game_runner import GameRunner
from ttt.game import Game
from ttt.player import Player


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
        self.get_valid_input_call_count = 0
        self.output_message_count = 0
        self.show_game_over_message_call_count = 0

    def render_board(self, _):
        self.render_board_call_count += 1

    def get_valid_input(self, valid_inputs, error_message):
        self.get_valid_input_call_count += 1
        return '1'

    def output_message(self, message):
        self.output_message_count += 1

    def show_game_over_message(self,game):
        self.show_game_over_message_call_count += 1


class MockBoard:
    def __init__(self, turns_remaining=1):
        self.get_spaces_call_count = 0
        self.is_full_call_count = 0
        self.place_marker_call_count = 0
        self.is_winning_line_call_count = 0
        self._turns_remaining = turns_remaining

    def get_spaces(self):
        self.get_spaces_call_count += 1
        return []

    def is_full(self):
        self.is_full_call_count += 1

    def place_marker(self, space, marker):
        self.place_marker_call_count += 1
        self._turns_remaining -= 1

    def is_available_space(self, space):
        return True

    def is_winning_line(self, line):
        self.is_winning_line_call_count += 1
        return True if self._turns_remaining == 0 else False


    def available_spaces(self):
       return None


@pytest.fixture
def game_runner():
    return GameRunner(console=MockConsole())


@pytest.fixture
def player_1():
    return Player('player 1', 'O')

@pytest.fixture
def player_2():
    return Player('player 2', 'X')


def test_run_instantiates_a_new_game(player_1, player_2, game_runner):
    game_runner.run(player_1, player_2, Game, MockBoard)

    assert game_runner.get_game() is not None


def test_run_requests_board_to_be_printed_each_turn_and_on_game_over(player_1, player_2):
    times_printed_on_final_turn_and_game_over = 2
    console = MockConsole()
    game_runner = GameRunner(console=console)
    game_runner.run(player_1, player_2, Game, MockBoard)

    assert console.render_board_call_count == times_printed_on_final_turn_and_game_over


def test_run_requests_a_message_be_displayed_on_each_turn(player_1, player_2):
    console = MockConsole()
    game_runner = GameRunner(console=console)
    game_runner.run(player_1, player_2, Game, MockBoard)

    assert console.output_message_count == 1


def test_run_requests_input_each_turn(player_1, player_2):
    console = MockConsole()
    game_runner = GameRunner(console=console)
    game_runner.run(player_1, player_2, Game, MockBoard)

    assert console.get_valid_input_call_count == 1


def test_run_requests_move_to_be_made_each_turn(player_1, player_2):
    game_runner = GameRunner(console=MockConsole())

    game_runner.run(player_1, player_2, Game, MockBoard)

    assert game_runner.get_game().get_board().place_marker_call_count == 1


def test_run_checks_game_for_game_over_state_each_turn(player_1, player_2):
    game_runner = GameRunner(console=MockConsole())

    game_runner.run(player_1, player_2, Game, MockBoard)

    assert game_runner.get_game().get_board().is_full_call_count == 2


def test_run_sends_a_message_to_user_on_game_over(player_1, player_2):
    console = MockConsole()
    game_runner = GameRunner(console=console)
    game_runner.run(player_1, player_2, Game, MockBoard)

    assert console.show_game_over_message_call_count == 1
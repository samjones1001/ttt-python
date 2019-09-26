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

    def switch_current_player(self):
        self.switch_player_call_count += 1

    def game_over(self):
        self.game_over_call_count += 1


class MockInterface:
    def __init__(self):
        self.render_board_call_count = 0
        self.get_int_call_count = 0

    def render_board(self, _):
        self.render_board_call_count += 1

    def get_int(self):
        self.get_int_call_count += 1


@pytest.fixture
def game_runner():
    return GameRunner(game=MockGame(), output=MockInterface())


def test_returns_a_game():
    game = MockGame()
    runner = GameRunner(game=game, output=MockInterface())
    assert runner.get_game() == game


def test_returns_an_output():
    output = MockInterface()
    runner = GameRunner(game=MockGame(), output=output)
    assert runner.get_output() == output


def test_play_turn_requests_current_board_state(game_runner):
    game_runner.play_turn()
    assert game_runner.get_game().get_board_state_call_count == 1


def test_play_turn_requests_board_to_be_printed(game_runner):
    game_runner.play_turn()
    assert game_runner.get_output().render_board_call_count == 1


def test_play_turn_requests_input(game_runner):
    game_runner.play_turn()
    assert game_runner.get_output().get_int_call_count == 1


def test_play_turn_requests_move_to_be_made(game_runner):
    game_runner.play_turn()
    assert game_runner.get_game().play_turn_call_count == 1


def test_play_turn_requests_current_player_switch(game_runner):
    game_runner.play_turn()
    assert game_runner.get_game().switch_player_call_count == 1


def test_checks_game_for_game_over_state(game_runner):
    game_runner.is_game_over()
    assert game_runner.get_game().game_over_call_count == 1



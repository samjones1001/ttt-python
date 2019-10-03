import pytest
from ttt.game_runner import GameRunner
from ttt.game import Game
from ttt.player import Player
from tests.mocks import MockConsole
from tests.mocks import MockBoard


@pytest.fixture
def game_runner():
    return GameRunner(MockConsole())


@pytest.fixture
def players():
    return [Player('player 1', 'O'), Player('player 2', 'X')]


def test_run_instantiates_a_new_game(players, game_runner):
    game_runner.run(players[0], players[1], Game, MockBoard)

    assert game_runner.get_game() is not None


def test_run_requests_board_to_be_printed_each_turn_and_on_game_over(players):
    times_printed_on_final_turn_and_game_over = 2
    console = MockConsole()
    game_runner = GameRunner(console)
    game_runner.run(players[0], players[1], Game, MockBoard)

    assert console.render_board_call_count == times_printed_on_final_turn_and_game_over


def test_run_requests_a_message_be_displayed_on_each_turn(players):
    console = MockConsole()
    game_runner = GameRunner(console)
    game_runner.run(players[0], players[1], Game, MockBoard)

    assert console.output_message_call_count == 1


def test_run_requests_input_each_turn(players):
    console = MockConsole()
    game_runner = GameRunner(console)
    game_runner.run(players[0], players[1], Game, MockBoard)

    assert console.get_valid_input_call_count == 1


def test_run_requests_move_to_be_made_each_turn(players):
    game_runner = GameRunner(MockConsole())

    game_runner.run(players[0], players[1], Game, MockBoard)

    assert game_runner.get_game().get_board().place_marker_call_count == 1


def test_run_checks_game_for_game_over_state_each_turn(players):
    game_runner = GameRunner(MockConsole())

    game_runner.run(players[0], players[1], Game, MockBoard)

    assert game_runner.get_game().get_board().is_full_call_count == 2


def test_run_sends_a_message_to_user_on_game_over(players):
    console = MockConsole()
    game_runner = GameRunner(console)
    game_runner.run(players[0], players[1], Game, MockBoard)

    assert console.show_game_over_message_call_count == 1
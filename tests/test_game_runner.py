import pytest
from ttt.game_runner import GameRunner
from tests.mocks import MockPlayer, MockConsole, MockGame


@pytest.fixture
def game_runner():
    return GameRunner(MockConsole())


@pytest.fixture
def players():
    return [MockPlayer('player 1', 'O'), MockPlayer('player 2', 'X')]


def test_checks_for_game_over_state_each_turn_and_at_game_over_state(players, game_runner):
    game_runner.run(players[0], players[1], MockGame)

    assert game_runner.get_game().game_over_call_count == 2


def test_plays_a_turn_when_game_is_not_over(players, game_runner):
    game_runner.run(players[0], players[1], MockGame)

    assert game_runner.get_game().play_turn_call_count == 1


def test_instructs_game_to_show_game_over_screen_on_game_over(players, game_runner):
    game_runner.run(players[0], players[1], MockGame)

    assert game_runner.get_game().show_game_over_screen_call_count == 1

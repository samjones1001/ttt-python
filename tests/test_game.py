import pytest
from ttt import game


@pytest.fixture
def standard_game():
    return game.Game()


@pytest.fixture
def custom_names_game():
    return game.Game(player_one='!', player_two='@')


def test_returns_player_one(standard_game):
    assert standard_game.get_player_one() == 'O'


def test_player_one_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_one() == '!'


def test_returns_player_two(standard_game):
    assert standard_game.get_player_two() == 'X'


def test_player_two_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_two() == '@'


def test_returns_current_player(standard_game):
    current_player_at_start = standard_game.get_player_one()
    assert standard_game.get_current_player() == current_player_at_start


def test_can_switch_current_player(standard_game):
    current_player_after_switch = standard_game.get_player_two()
    standard_game.switch_current_player()
    assert standard_game.get_current_player() == current_player_after_switch


def test_can_switch_back_to_player_one(standard_game):
    current_player_on_turn_three = standard_game.get_player_one()
    standard_game.switch_current_player()
    standard_game.switch_current_player()
    assert standard_game.get_current_player() == current_player_on_turn_three




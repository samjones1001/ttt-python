import pytest
from ttt.game.game_rules import GameRules
from ttt.game.board import Board

@pytest.fixture()
def rules():
    return GameRules()


def test_a_line_does_not_win_if_all_spaces_are_empty(rules):
    board = Board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    assert rules.is_won(board, 'X') is False


def test_a_line_does_not_win_if_not_all_spaces_contain_the_same_marker(rules):
    board = Board(['X', 'X', 'O', '4', '5', '6', '7', '8', '9'])

    assert rules.is_won(board, 'X') is False


def test_a_line_wins_if_all_spaces_contain_the_same_marker(rules):
    board = Board(['X', 'X', 'X', '4', '5', '6', '7', '8', '9'])

    assert rules.is_won(board, 'X') is True


def test_game_is_not_over_when_board_is_not_full(rules):
    board = Board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    assert rules.game_over(board, 'X') is False


def test_the_game_is_over_when_board_is_full(rules):
    board = Board(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

    assert rules.game_over(board, 'X') is True


def test_the_game_is_over_if_a_player_has_won(rules):
    board = Board(['X', 'X', 'X', '4', '5', '6', '7', '8', '9'])

    assert rules.game_over(board, 'X') is True
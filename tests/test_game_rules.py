from ttt.game.game_rules import GameRules
from ttt.game.board import Board


def test_a_line_does_not_win_if_all_spaces_are_empty():
    board = Board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    game = GameRules()

    assert game.is_won(board, 'X') is False


def test_a_line_does_not_win_if_not_all_spaces_contain_the_same_marker():
    board = Board(['X', 'X', 'O', ' ', ' ', ' ', ' ', ' ', ' '])
    game = GameRules()

    assert game.is_won(board, 'X') is False


def test_a_line_wins_if_all_spaces_contain_the_same_marker():
    board = Board(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
    game = GameRules()

    assert game.is_won(board, 'X') is True


def test_game_is_not_over_when_board_is_not_full():
    board = Board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    game = GameRules()

    assert game.game_over(board, 'X') is False


def test_the_game_is_over_when_board_is_full():
    board = Board(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
    game = GameRules()

    assert game.game_over(board, 'X') is True


def test_the_game_is_over_if_a_player_has_won():
    board = Board(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
    game = GameRules()

    assert game.game_over(board, 'X') is True
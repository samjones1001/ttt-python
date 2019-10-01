import pytest
from ttt.board import Board


@pytest.fixture
def board():
    return Board()


@pytest.fixture(params=[0, 1, 2, 3, 4, 5, 6, 7, 8])
def space(request):
    yield request.param


def test_board_has_nine_spaces_by_default(board):
    assert len(board.get_spaces()) == 9


def test_can_occupy_a_space(board, space):
    board.place_marker(space, 'x')

    assert board.get_spaces()[space] == 'x'


def test_board_is_not_full_when_no_spaces_are_occupied(board):
    assert board.is_full() is False


def test_board_is_not_full_when_only_some_spaces_are_occupied(board):
    num_of_spaces_minus_one = len(board.get_spaces()) - 1
    for space in range(num_of_spaces_minus_one):
        board.place_marker(space, 'x')

    assert board.is_full() is False


def test_board_is_full_when_all_spaces_are_occupied(board):
    for space in range(len(board.get_spaces())):
        board.place_marker(space, 'x')

    assert board.is_full() is True


def test_a_space_is_available_when_it_exists_and_is_unoccupied(board):
    assert board.is_valid_space(0) is True


def test_a_space_is_unavailable_when_it_exists_but_is_occupied(board):
    board.place_marker(0, 'x')

    assert board.is_valid_space(0) is False


def test_negative_indexed_spaces_are_not_available(board):
    assert board.is_valid_space(-1) is False


def test_out_of_bounds_indexed_spaces_are_not_available(board):
    highest_space_index = len(board.get_spaces()) - 1

    assert board.is_valid_space(highest_space_index + 1) is False


def test_a_line_does_not_win_if_not_all_spaces_contain_the_same_marker(board):
    board.place_marker(0, 'X')
    board.place_marker(1, 'X')
    board.place_marker(2, 'O')

    assert board.is_winning_line((0, 1, 2)) is False


def test_a_line_wins_if_all_spaces_contain_the_same_marker(board):
    board.place_marker(0, 'X')
    board.place_marker(1, 'X')
    board.place_marker(2, 'X')

    assert board.is_winning_line((0, 1, 2)) is True


def test_a_line_does_not_win_if_all_spaces_are_empty(board):
    assert board.is_winning_line((0, 1, 2)) is False

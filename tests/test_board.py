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


def test_returns_false_when_no_spaces_are_occupied(board):
    assert board.is_full() is False


def test_returns_false_when_board_is_not_full(board):
    num_of_spaces_minus_one = len(board.get_spaces()) - 1
    for _ in range(num_of_spaces_minus_one):
        board.place_marker(_, 'x')
    assert board.is_full() is False


def test_returns_true_when_all_spaces_are_occupied(board):
    for _ in range(len(board.get_spaces())):
        board.place_marker(_, 'x')
    assert board.is_full() is True


def test_returns_true_when_a_space_exists_and_is_unoccupied(board):
    assert board.is_available_space(0) is True


def test_returns_false_when_a_space_exists_but_is_occupied(board):
    board.place_marker(0, 'x')
    assert board.is_available_space(0) is False


def test_returns_false_when_passed_a_negative_index(board):
    assert board.is_available_space(-1) is False


def test_returns_false_when_passed_an_out_of_bounds_index(board):
    highest_space_index = len(board.get_spaces()) - 1
    assert board.is_available_space(highest_space_index + 1) is False


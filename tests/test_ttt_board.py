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


def test_knows_when_no_spaces_are_occupied(board):
    assert board.is_full() is False


def test_knows_when_all_spaces_are_not_occupied(board):
    num_of_spaces_minus_one = len(board.get_spaces()) - 1
    for _ in range(num_of_spaces_minus_one):
        board.place_marker(_, 'x')
    assert board.is_full() is False


def test_knows_when_all_spaces_are_occupied(board):
    for _ in range(len(board.get_spaces())):
        board.place_marker(_, 'x')
    assert board.is_full() is True

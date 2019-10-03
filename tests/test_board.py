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
    assert 0 in board.available_spaces()


def test_a_space_is_unavailable_when_it_exists_but_is_occupied(board):
    board.place_marker(0, 'x')

    assert 0 not in board.available_spaces()


def test_returns_all_spaces_when_none_have_been_occupied(board):
    number_of_spaces = len(board.get_spaces())

    assert len(board.available_spaces()) == number_of_spaces


def test_only_returns_unoccupied_spaces_when_some_have_been_occupied(board):
    board.place_marker(0, 'X')

    assert 0 not in board.available_spaces()


def test_returns_no_spaces_when_all_have_been_occupied(board):
    for space in range(0, len(board.get_spaces())):
        board.place_marker(space, 'X')

    assert len(board.available_spaces()) == 0


def test_negative_indexed_spaces_are_not_available(board):
    assert -1 not in board.available_spaces()


def test_out_of_bounds_indexed_spaces_are_not_available(board):
    highest_space_index = len(board.get_spaces())

    assert highest_space_index not in board.available_spaces()


def test_returns_the_contents_of_the_spaces_requested(board):
    board.place_marker(0, 'A')
    board.place_marker(1, 'B')
    board.place_marker(2, 'C')

    assert board.retrieve_line((0,1,2)) == ['A', 'B', 'C']

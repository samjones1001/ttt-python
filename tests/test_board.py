import pytest
from ttt import board

@pytest.fixture
def standard_board():
    return board.Board()


@pytest.fixture(params=[0, 1, 2, 3, 4, 5, 6, 7, 8])
def space(request):
    yield request.param


def test_board_has_nine_spaces_by_default(standard_board):
    assert len(standard_board.get_spaces()) == 9


def test_board_can_have_custom_number_of_spaces():
    assert len(board.Board(16).get_spaces()) == 16


def test_throws_an_error_if_passed_create_with_non_square_number_of_spaces():
    with pytest.raises(Exception) as err:
        board.Board(10)
    assert "Please set the number of spaces to a square number" in str(err.value)


def test_can_occupy_a_space(standard_board, space):
    standard_board.occupy_space(space, 'x')
    assert standard_board.get_spaces()[space] == 'x'

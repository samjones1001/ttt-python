import pytest
from ttt import board


def test_board_has_nine_spaces_by_default():
    assert len(board.Board().get_spaces()) == 9


def test_board_can_have_custom_number_of_spaces():
    assert len(board.Board(16).get_spaces()) == 16


def test_throws_an_error_if_passed_create_with_non_square_number_of_spaces():
    with pytest.raises(Exception) as err:
        board.Board(10)
    assert "Please set the number of spaces to a square number" in str(err.value)
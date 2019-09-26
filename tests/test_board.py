import pytest
from games.board import Board


def test_board_can_have_custom_number_of_spaces():
    assert len(Board(16).get_spaces()) == 16


def test_throws_an_error_if_passed_create_with_non_square_number_of_spaces():
    with pytest.raises(Exception) as err:
        Board(10)
    assert "Please set the number of spaces to a square number" in str(err.value)

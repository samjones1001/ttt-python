import pytest
import ttt.interface as interface


@pytest.fixture
def empty_board_output():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def part_filled_board_output():
    return ' x |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def filled_board_output():
    return ' x | x | x \n-----------\n x | x | x \n-----------\n x | x | x \n'


def test_prints_an_empty_grid_correctly(empty_board_output, capfd):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    interface.render_board(empty_board_state)
    out, err = capfd.readouterr()
    assert out == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, capfd):
    part_filled_board_state = ['x', '-', '-', '-', '-', '-', '-', '-', '-']
    interface.render_board(part_filled_board_state)
    out, err = capfd.readouterr()
    assert out == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, capfd):
    filled_board_state = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    interface.render_board(filled_board_state)
    out, err = capfd.readouterr()
    assert out == filled_board_output






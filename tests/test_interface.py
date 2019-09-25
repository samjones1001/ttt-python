import pytest
import ttt.interface as interface


@pytest.fixture
def empty_board_output():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


def test_prints_an_empty_grid_correctly(empty_board_output, capfd):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    interface.render_board(empty_board_state)
    out, err = capfd.readouterr()
    assert out == empty_board_output





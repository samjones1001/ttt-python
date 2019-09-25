import pytest
import ttt.interface as interface

class Runner():
    def __init__(self, capfd):
        self._capfd = capfd

    def render_board(self, board_state):
        interface.render_board(board_state)
        out, err = self._capfd.readouterr()

        if err:
            print(err)
        else:
            return out


@pytest.fixture
def empty_board_output():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def part_filled_board_output():
    return ' x |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def filled_board_output():
    return ' x | x | x \n-----------\n x | x | x \n-----------\n x | x | x \n'


@pytest.fixture
def runner(capfd):
    return Runner(capfd)


def test_prints_an_empty_grid_correctly(empty_board_output, runner):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(empty_board_state) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', '-', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(part_filled_board_state) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    assert runner.render_board(filled_board_state) == filled_board_output






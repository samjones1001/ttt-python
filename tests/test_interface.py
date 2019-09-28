import pytest
from ttt.console import Console


class MockConsoleIOErrorInput:
    def get_input(self, message=""):
        return "Not a number!"


class MockConsoleIOValidInput:
    def __init__(self):
        self.last_output = None

    def get_input(self, message=""):
        return "1"

    def print_output(self, output):
        self.last_output = output


class TestRunner:
    def render_board(self, board_state):
        console_io = MockConsoleIOValidInput()
        console = Console(console_io)
        console.render_board(board_state)
        return console_io.last_output


@pytest.fixture
def console_with_valid_io_input():
    return Console(MockConsoleIOValidInput())


@pytest.fixture
def console_with_invalid_io_input():
    return Console(MockConsoleIOErrorInput())


@pytest.fixture
def empty_board_output():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   '


@pytest.fixture
def part_filled_board_output():
    return ' x | o |   \n-----------\n   |   |   \n-----------\n   |   |   '


@pytest.fixture
def filled_board_output():
    return ' x | o | x \n-----------\n o | x | o \n-----------\n x | o | x '


@pytest.fixture
def runner():
    return TestRunner()


def test_returns_a_console():
    console_io = MockConsoleIOValidInput()
    interface = Console(console_io)
    assert interface.get_console_io() == console_io


def test_prints_an_empty_grid_correctly(empty_board_output, runner):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(empty_board_state) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', 'o', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(part_filled_board_state) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
    assert runner.render_board(filled_board_state) == filled_board_output


def test_accepts_an_integer_from_the_user(console_with_valid_io_input):
    assert console_with_valid_io_input.get_int() == 1


def test_errors_if_provided_non_numeric_input(console_with_invalid_io_input):
    with pytest.raises(Exception) as err:
        console_with_invalid_io_input.get_int()
    assert "Input was not a number!" in str(err.value)







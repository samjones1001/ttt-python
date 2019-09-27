import pytest
from ttt.cl_interface import CLInterface


class MockConsoleErrorInput:
    def get_input(self, message=""):
        return "Not a number!"


class MockConsoleValidInput:
    def get_input(self, message=""):
        return "1"

    def print_output(self, output):
        print(output)


class Runner:
    def __init__(self, capfd):
        self._capfd = capfd

    def render_board(self, board_state):
        interface = CLInterface(console=MockConsoleValidInput())
        interface.render_board(board_state)
        out, err = self._capfd.readouterr()

        if err:
            print(err)
        else:
            return out


@pytest.fixture
def valid_interface():
    return CLInterface(console=MockConsoleValidInput())


@pytest.fixture
def error_interface():
    return CLInterface(console=MockConsoleErrorInput())


@pytest.fixture
def empty_board_output():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def part_filled_board_output():
    return ' x | o |   \n-----------\n   |   |   \n-----------\n   |   |   \n'


@pytest.fixture
def filled_board_output():
    return ' x | o | x \n-----------\n o | x | o \n-----------\n x | o | x \n'


@pytest.fixture
def runner(capfd):
    return Runner(capfd)


def test_returns_a_console():
    console = MockConsoleValidInput()
    interface = CLInterface(console=console)
    assert interface.get_console() == console


def test_prints_an_empty_grid_correctly(empty_board_output, runner):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(empty_board_state) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', 'o', '-', '-', '-', '-', '-', '-', '-']
    assert runner.render_board(part_filled_board_state) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
    assert runner.render_board(filled_board_state) == filled_board_output


def test_accepts_an_integer_from_the_user(valid_interface):
    assert valid_interface.get_int() == 1


def test_errors_if_provided_non_numeric_input(error_interface):
    with pytest.raises(Exception) as err:
        error_interface.get_int()
    assert "Input was not a number!" in str(err.value)







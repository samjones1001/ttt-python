import pytest
from ttt.console_ui.console import Console
from ttt.game.board import Board
from tests.mocks import MockConsoleIO


class TestRunner:
    def render_board(self, game):
        console_io = MockConsoleIO()
        console = Console(console_io)
        console.render_board(game)
        return console_io.last_output


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


def test_prints_an_empty_grid_correctly(empty_board_output, runner):
    empty_board_state = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    assert runner.render_board(empty_board_state) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', 'o', '-', '-', '-', '-', '-', '-', '-']

    assert runner.render_board(part_filled_board_state) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']

    assert runner.render_board(filled_board_state) == filled_board_output


def test_returns_valid_user_input():
    mock_io = MockConsoleIO(inputs=['valid'])
    console = Console(mock_io)

    output = console.get_valid_input(['valid'], 'error message')
    assert output == 'valid'


def test_continues_to_prompt_for_input_until_valid_input_provided():
    mock_io = MockConsoleIO(inputs=['invalid', 'valid'])
    console = Console(mock_io)

    output = console.get_valid_input(['valid'], 'error message')

    assert mock_io.get_input_call_count == 2
    assert output == 'valid'


def prints_an_error_message_if_provided_invalid_input():
    mock_io = MockConsoleIO(inputs=['invalid', 'valid'])
    console = Console(mock_io)

    console.get_valid_input(['valid'], 'error message')

    assert mock_io.last_output == 'error message'


def test_sends_message_to_console_io():
    console_io = MockConsoleIO()
    console = Console(console_io)

    console.output_message("a message")

    assert console_io.last_output == "a message"

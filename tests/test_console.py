import pytest
from ttt.console_ui.console import Console
from tests.mocks import MockConsoleIO, MockPlayer


class TestRunner:
    def render_board(self, board):
        console_io = MockConsoleIO()
        console = Console(console_io)
        console.render_board(board, 'player_1', 'player_2')
        return console_io.last_output

    def get_validated_input(self, inputs, input_regex, error):
        console_io = MockConsoleIO(inputs = inputs)
        console = Console(console_io)
        return console.get_validated_input(input_regex, error)


@pytest.fixture
def runner():
    return TestRunner()


def test_the_screen_is_cleared_each_time_the_board_is_printed():
    console_io = MockConsoleIO()
    console = Console(console_io)
    console.render_board([], MockPlayer('Player 1', 'O'), MockPlayer('Player 2', 'X'))

    assert console_io.clear_call_count == 1


def test_prints_an_empty_grid_correctly(runner):
    empty_board_output = ' 1  | 2  | 3  \n--------------\n 4  | 5  | 6  \n--------------\n 7  | 8  | 9  '
    empty_board_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    assert runner.render_board(empty_board_state) == empty_board_output


def test_prints_a_part_filled_grid_correctly(runner):
    part_filled_board_output = ' x  | o  | 3  \n--------------\n 4  | 5  | 6  \n--------------\n 7  | 8  | 9  '
    part_filled_board_state = ['x', 'o', '3', '4', '5', '6', '7', '8', '9']

    assert runner.render_board(part_filled_board_state) == part_filled_board_output


def test_prints_a_fully_filled_grid(runner):
    filled_board_output = ' x  | o  | x  \n--------------\n o  | x  | o  \n--------------\n x  | o  | x  '
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']

    assert runner.render_board(filled_board_state) == filled_board_output


def test_prints_a_correctly_aligned_board_with_emoji_markers(runner):
    emoji_board_output = ' 👍 | x  | 3  \n--------------\n x  | 👍 | 6  \n--------------\n x  | 8  | 👍 '
    board_state = ['👍', 'x', '3', 'x', '👍', '6', 'x', '8', '👍']

    assert runner.render_board(board_state) == emoji_board_output


def test_prints_a_correctly_aligned_board_with_emoji_markers_with_a_width_of_two_characters(runner):
    wide_emoji_board_output = ' ❤️  | x  | 3  \n--------------\n x  | ❤️  | 6  \n--------------\n x  | 8  | ❤️  '
    board_state = ['❤️', 'x', '3', 'x', '❤️', '6', 'x', '8', '❤️']

    assert runner.render_board(board_state) == wide_emoji_board_output


def test_returns_valid_user_input(runner):
    assert runner.get_validated_input(['1'], '^[/1]$', 'error message') == '1'


def test_continues_to_prompt_for_input_until_valid_input_provided(runner):
    assert runner.get_validated_input(['-1', '1'], '^[/1]$', 'error message') == '1'


def prints_an_error_message_if_provided_invalid_input():
    mock_io = MockConsoleIO(inputs=['invalid', 'valid'])
    console = Console(mock_io)

    console.get_validated_input(['valid'], 'error message')

    assert mock_io.last_output == 'error message'


def test_sends_message_to_console_io():
    console_io = MockConsoleIO()
    console = Console(console_io)

    console.output_message("a message")

    assert console_io.last_output == "a message"

import pytest
from ttt.console import Console
from ttt.player import Player
from ttt.game import Game


class MockConsoleIO:
    def __init__(self, inputs=None):
        self.get_input_call_count = 0
        self.last_output = None
        self.inputs = inputs

    def get_input(self, message=""):
        self.get_input_call_count += 1
        return self.inputs.pop(0)

    def print_output(self, output):
        self.last_output = output

class MockBoard:
    def __init__(self, is_won=False, is_full=False):
        self.arg = 1
        self._is_won = is_won
        self._is_full = is_full

    def is_winning_line(self, line):
        return self._is_won

    def is_tie(self):
        return self._is_full


class MockGame:
    def __init__(self, board_state):
        self._board_state = board_state

    def get_board_state(self):
        return self._board_state


class TestRunner:
    def render_board(self, game):
        console_io = MockConsoleIO()
        console = Console(console_io)
        console.render_board(game)
        return console_io.last_output


@pytest.fixture
def console_with_valid_io_input():
    return Console(MockConsoleIO('invalid'))


@pytest.fixture
def console_with_invalid_io_input():
    return Console(MockConsoleIO('valid'))


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
    game = MockGame(empty_board_state)

    assert runner.render_board(game) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', 'o', '-', '-', '-', '-', '-', '-', '-']
    game = MockGame(part_filled_board_state)

    assert runner.render_board(game) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
    game = MockGame(filled_board_state
                    )
    assert runner.render_board(game) == filled_board_output


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


def test_sends_message_to_console_io(console_with_valid_io_input):
    console_io = MockConsoleIO()
    console = Console(console_io)

    console.output_message("a message")

    assert console_io.last_output == "a message"


def test_if_a_game_has_been_won_sends_a_message_to_console_io(console_with_valid_io_input):
    console_io = MockConsoleIO()
    console = Console(console_io)
    player_1 = Player('Player 1', 'O')
    player_2 = Player('Player 2', 'O')

    game = Game(player_1, player_2, MockBoard(is_won=True))

    console.show_game_over_message(game)

    assert console_io.last_output == "Player 2 won!"


def test_if_a_game_is_a_tie_sends_a_message_to_console_io(console_with_valid_io_input):
    console_io = MockConsoleIO()
    console = Console(console_io)
    player_1 = Player('Player 1', 'O')
    player_2 = Player('Player 2', 'O')

    game = Game(player_1, player_2, MockBoard(is_full=True))

    console.show_game_over_message(game)

    assert console_io.last_output == "It's a tie!"


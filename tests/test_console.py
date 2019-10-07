import pytest
from ttt.console_ui.console import Console
from ttt.players.human_player import HumanPlayer
from ttt.game.game import Game
from ttt.game.board import Board
from tests.mocks import MockConsoleIO, MockGame, MockBoard


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
    board = Board(empty_board_state)

    assert runner.render_board(board) == empty_board_output


def test_prints_a_part_filled_grid_correctly(part_filled_board_output, runner):
    part_filled_board_state = ['x', 'o', '-', '-', '-', '-', '-', '-', '-']
    board = Board(part_filled_board_state)

    assert runner.render_board(board) == part_filled_board_output


def test_prints_a_fully_filled_grid(filled_board_output, runner):
    filled_board_state = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
    board = Board(filled_board_state)

    assert runner.render_board(board) == filled_board_output


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


def test_if_a_game_has_been_won_sends_a_message_to_console_io():
    console_io = MockConsoleIO()
    console = Console(console_io)
    player_1 = HumanPlayer('Player 1', 'O', console)
    player_2 = HumanPlayer('Player 2', 'X', console)

    game = Game(player_1, player_2, MockBoard(line_to_check=['X', 'X', 'X']))

    console.show_game_over_message(game)

    assert console_io.last_output == "Player 2 won!"


def test_if_a_game_is_a_tie_sends_a_message_to_console_io():
    console_io = MockConsoleIO()
    console = Console(console_io)
    player_1 = HumanPlayer('Player 1', 'O', console)
    player_2 = HumanPlayer('Player 2', 'X', console)

    game = Game(player_1, player_2, MockBoard(spaces_remaining=0, line_to_check=[]))

    console.show_game_over_message(game)

    assert console_io.last_output == "It's a tie!"


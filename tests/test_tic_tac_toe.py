import pytest
import tic_tac_toe as app
from ttt.messages import game_tied_message
from tests.mocks import MockConsoleIO


@pytest.fixture
def filled_board_output():
    return ' O | O | X \n-----------\n X | X | O \n-----------\n O | X | O '


@pytest.fixture
def win_state_board_output():
    return ' O | X | O \n-----------\n X | O | X \n-----------\n O |   |   '


def test_can_play_a_full_game():
    app.consoleio = MockConsoleIO(['1', '', '1', '', '1', '5', '2', '3', '7', '4', '6', '8', '9', 'n'])
    app.main()

    assert app.consoleio.last_output == game_tied_message()


def test_gracefully_handles_invalid_user_input():
    app.consoleio = MockConsoleIO(['1', '', '1', '', '-1', '1', '5', '2', '3', 'not a number', '7', '4', '3000', '6', '8', '9', 'n'])
    app.main()

    assert app.consoleio.last_output == game_tied_message()


def test_game_ends_if_a_player_wins():
    app.consoleio = MockConsoleIO(['1', '', '1', '', '1', '2', '3', '4', '5', '6', '7', 'n'])
    app.main()

    assert "Player 1 won!" in app.consoleio.last_output
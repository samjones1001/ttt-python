import pytest
import tic_tac_toe as app
from ttt.messages import game_tied_message
from tests.mocks import MockConsoleIO


@pytest.fixture
def game_setup_inputs():
    return ['1', '', '1', '', '1']


def test_can_play_a_full_game(game_setup_inputs):
    app.consoleio = MockConsoleIO(game_setup_inputs + ['1', '5', '2', '3', '7', '4', '6', '8', '9', 'n'])
    app.main()

    assert app.consoleio.last_output == game_tied_message()


def test_gracefully_handles_invalid_user_input(game_setup_inputs):
    app.consoleio = MockConsoleIO(game_setup_inputs + ['-1', '1', '5', '2', '3', 'not a number', '7', '4', '3000', '6', '8', '9', 'n'])
    app.main()

    assert app.consoleio.last_output == game_tied_message()


def test_game_ends_if_a_player_wins(game_setup_inputs):
    app.consoleio = MockConsoleIO(game_setup_inputs + ['1', '2', '3', '4', '5', '6', '7', 'n'])
    app.main()

    assert "Player 1 won!" in app.consoleio.last_output

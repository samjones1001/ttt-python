import pytest
import tic_tac_toe as app
from ttt.messages import end_game_message
from tests.mocks import MockConsoleIO


@pytest.fixture
def game_setup_inputs():
    return ['1', '', '1', '', '1']


def _test_can_play_a_full_game(game_setup_inputs):
    app.consoleio = MockConsoleIO(game_setup_inputs + ['1', '5', '2', '3', '7', '4', '6', '8', '9', 'n'])
    app.main()

    assert app.consoleio.last_output == end_game_message()

import pytest
import tic_tac_toe as app
from ttt.console_ui.menu import Interface
from ttt.console_ui.console import Console
from ttt.messages import GAME_TIED_MESSAGE
from tests.mocks import MockConsoleIO


@pytest.fixture
def filled_board_output():
    return ' O | O | X \n-----------\n X | X | O \n-----------\n O | X | O '


@pytest.fixture
def win_state_board_output():
    return ' O | X | O \n-----------\n X | O | X \n-----------\n O |   |   '


def test_can_play_a_full_game():
    io = MockConsoleIO(['1', '0', '4', '1', '2', '6', '3', '5', '7', '8'])
    console = Console(io)
    app.interface = Interface(console)

    app.main()

    assert io.last_output == GAME_TIED_MESSAGE


def test_gracefully_handles_invalid_user_input():
    io = MockConsoleIO(['1', '-1', '0', '4', '1', '2', 'not a number', '6', '3', '3000', '5', '7', '8'])
    console = Console(io)
    app.interface = Interface(console)

    app.main()

    assert io.last_output == GAME_TIED_MESSAGE


def test_game_ends_if_a_player_wins():
    io = MockConsoleIO(['1', '0', '1', '2', '3', '4', '5', '6', '7', '8'])
    console = Console(io)
    app.interface = Interface(console)

    app.main()

    assert io.last_output == "Player 1 won!"
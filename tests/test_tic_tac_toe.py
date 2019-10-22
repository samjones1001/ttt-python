import tic_tac_toe as app
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.messages import end_game_message
from tests.mocks import MockConsoleIO


def test_can_play_a_full_game():
    app.consoleio = MockConsoleIO(['1', '', '', '1', '', '', '1', '1', '5', '2', '3', '7', '4', '6', '8', '9', 'n'])
    app.console = Console(app.consoleio)
    app.menu = Menu(app.console)

    app.main()

    assert app.consoleio.last_output == end_game_message()

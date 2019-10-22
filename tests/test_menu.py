from tests.mocks import MockConsole, MockConsoleIO
from ttt import constants
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.messages import play_again_message, end_game_message
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer


def test_user_can_select_player_types():
    menu = Menu(MockConsole(['1', '', '', '2', '', '', '1']))

    config = menu.configure_game()

    assert isinstance(config.first_player, HumanPlayer)
    assert isinstance(config.second_player, SimpleComputerPlayer)


def test_user_can_select_a_custom_marker():
    menu = Menu(MockConsole(['1', '!', '', '2', '', '', '1']))

    config = menu.configure_game()

    assert config.first_player.get_marker() == '!'


def test_user_can_select_a_colour_for_their_marker():
    menu = Menu(MockConsole(['1', '!', '1', '2', '', '', '1']))

    config = menu.configure_game()

    assert config.first_player.get_marker_colour() == constants.COLOURS['1']


def test_user_can_select_a_custom_emoji_marker():
    menu = Menu(MockConsole(['1', '👍', '', '1', '', '', '1']))

    config = menu.configure_game()

    assert config.first_player.get_marker() == '👍'


def test_a_user_will_continue_to_be_prompted_if_they_provide_an_integer_as_a_marker():
    menu = Menu(Console(MockConsoleIO(['1', '1', '5', '2', '7', '!', '', '1', '', '', '1'])))

    config = menu.configure_game()

    assert config.first_player.get_marker() == '!'


def test_a_player_will_continue_to_be_prompted_if_they_provide_whitespace_as_a_marker():
    menu = Menu(Console(MockConsoleIO(['1', ' ', ' ', '   ', '!', '', '1', '', '', '1'])))

    config = menu.configure_game()

    assert config.first_player.get_marker() == '!'


def test_a_player_will_retain_their_default_marker_if_they_provide_an_empty_string():
    menu = Menu(Console(MockConsoleIO(['1', '', '', '1', '', '', '1'])))

    config = menu.configure_game()

    assert config.first_player.get_marker() == 'O'


def test_if_player_one_selects_x_as_marker_player_two_default_marker_changes_to_o():
    menu = Menu(Console(MockConsoleIO(['1', 'X', '', '1', '', '', '1', 'n'])))

    config = menu.configure_game()

    assert config.second_player.get_marker() == 'O'


def test_user_cannot_select_the_same_marker_as_their_opponent():
    menu = Menu(Console(MockConsoleIO(['1', 'X', '', '2', 'X', 'O', '', '1'])))

    config = menu.configure_game()

    assert config.second_player.get_marker() == 'O'


def test_user_can_reverse_the_order_of_turns():
    menu = Menu(Console(MockConsoleIO(['1', 'X', '', '2', 'O', '', '2'])))

    config = menu.configure_game()

    assert config.first_player.get_name() == 'Player 2'


def test_console_is_cleared_after_each_message_is_printed():
    inputs = ['1', 'X', '', '2', 'O', '', '2', 'n']
    console = MockConsole(inputs)
    menu = Menu(console)

    menu.configure_game()

    assert console.clear_output_call_count == len(inputs) - 1


def test_user_has_the_option_to_play_again():
    io = MockConsoleIO(['y'])
    console = Console(io)
    menu = Menu(console)

    play_again = menu.play_again()

    assert io.last_output == play_again_message()
    assert play_again


def test_user_has_the_option_not_to_play_again():
    io = MockConsoleIO(['n'])
    console = Console(io)
    menu = Menu(console)

    play_again = menu.play_again()

    assert io.last_output == end_game_message()
    assert not play_again


def test_exits_the_game():
    io = MockConsoleIO([])
    console = Console(io)
    menu = Menu(console)

    menu.exit()

    assert io.last_output == end_game_message()

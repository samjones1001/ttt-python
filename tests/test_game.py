import pytest
from ttt.game.game import Game
from ttt.game.board import Board
from ttt.console_ui.console import Console
from tests.mocks import MockConsoleIO, MockConsole, MockPlayer


@pytest.fixture
def players():
    return [MockPlayer('player 1', 'O', 0), MockPlayer('player 2', 'X', 1)]


@pytest.fixture
def game(players):
    return Game(first_player=players[0], second_player=players[1])


def test_current_player_switches_to_player_two_after_player_one_turn(game, players):
    current_player_after_switch = players[1].get_name()
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert game.get_current_player_name() == current_player_after_switch


def test_current_player_reverts_to_player_one_after_player_two_turn(game, players):
    current_player_on_turn_three = players[0].get_name()
    console = Console(MockConsoleIO(['1', '0']))
    game.play_turn(console)
    game.play_turn(console)

    assert game.get_current_player_name() == current_player_on_turn_three


def test_play_turn_occupies_a_space_on_the_board(game):
    available_space_count = len(game.available_spaces())
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert len(game.available_spaces()) == available_space_count - 1


def test_playing_a_turn_outputs_the_current_state_of_the_board(game):
    console = MockConsole()
    game.play_turn(console)

    assert console.render_board_call_count == 1


def test_on_first_turn_outputs_a_message_with_no_previous_move(game):
    console_io = MockConsoleIO()
    console = Console(console_io)

    game.play_turn(console)

    assert console_io.last_output == "\nplayer 1's turn."


def test_on_subsequent_turns_outputs_a_message_with_previous_move(game):
    console_io = MockConsoleIO()
    console = Console(console_io)

    game.play_turn(console)
    game.play_turn(console)

    assert console_io.last_output == "\nplayer 2's turn. player 1 chose space 1"


def test_playing_a_turn_prompts_player_for_a_move(game, players):
    game.play_turn(Console(MockConsoleIO()))

    assert players[0].get_move_call_count == 1


def test_displays_the_board_and_a_message_on_game_over(players):
    game_over_board = Board(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '])
    game = Game(players[0], players[1], game_over_board)
    console_io = MockConsoleIO()
    console = Console(console_io)
    game.game_over(console)

    assert console_io.print_output_call_count == 2

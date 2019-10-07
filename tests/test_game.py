import pytest
from ttt.game.game import Game
from ttt.console_ui.console import Console
from tests.mocks import MockConsoleIO, MockConsole, MockPlayer, MockBoard


@pytest.fixture
def players():
    return [MockPlayer('player 1', 'O'), MockPlayer('player 2', 'X')]


@pytest.fixture
def game(players):
    return Game(player_one=players[0], player_two=players[1])


def test_get_board_state_sends_a_message_to_board(players):
    board = MockBoard()
    game = Game(players[0], players[1], game_board=board)
    game.get_board_state()

    assert board.get_spaces_call_count == 1


def test_available_spaces_sends_a_message_to_board(players):
    board = MockBoard()
    game = Game(players[0], players[1], game_board=board)
    game.available_spaces()

    assert board.available_spaces_call_count == 1


def test_current_player_switches_to_player_two_after_player_one_turn(game, players):
    current_player_after_switch = players[1].get_name()
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert game.get_current_player_name() == current_player_after_switch


def test_current_player_reverts_to_player_one_after_player_two_turn(game, players):
    current_player_on_turn_three = players[0].get_name()
    console = Console(MockConsoleIO(['1']))
    game.play_turn(console)
    game.play_turn(console)

    assert game.get_current_player_name() == current_player_on_turn_three


def test_play_turn_instructs_board_to_occupy_space(players):
    board = MockBoard()
    game = Game(game_board=board, player_one=players[0], player_two=players[1])
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert board.place_marker_call_count == 1


def test_playing_a_turn_outputs_the_current_state_of_the_board(game):
    console = MockConsole()
    game.play_turn(console)

    assert console.render_board_call_count == 1


def test_playing_a_turn_outputs_a_message(game):
    console = MockConsole()
    game.play_turn(console)

    assert console.output_message_call_count == 1


def test_playing_a_turn_prompts_player_for_a_move(game, players):
    console = MockConsole()
    game.play_turn(console)

    assert players[0].get_move_call_count == 1


def test_playing_a_turn_places_a_marker_on_the_board(game):
    space_to_fill = 1
    console = MockConsole()
    game.play_turn(console)

    assert space_to_fill not in game.get_board().available_spaces()


def test_game_is_not_over_when_board_is_not_full(game):
    assert game.game_over() is False


def test_the_game_is_over_when_board_is_full(players):
    end_state_game = Game(players[0], players[1], game_board=MockBoard(spaces_remaining=0))

    assert end_state_game.game_over() is True


def test_the_game_is_over_if_a_player_has_won(players):
    board = MockBoard(line_to_check=['X', 'X', 'X'])
    won_game = Game(players[0], players[1], game_board=board)

    assert won_game.game_over() is True


def test_a_line_does_not_win_if_not_all_spaces_contain_the_same_marker(players):
    board = MockBoard(line_to_check=['X', 'X', 'O'])
    game = Game(players[0], players[1], game_board=board)

    assert game.is_won(board, 'X') is False


def test_a_line_wins_if_all_spaces_contain_the_same_marker(players):
    board = MockBoard(line_to_check=['X', 'X', 'X'])
    game = Game(players[0], players[1], game_board=board)

    assert game.is_won(board, 'X') is True


def test_a_line_does_not_win_if_all_spaces_are_empty(players):
    board = MockBoard(line_to_check=['-', '-', '-'])
    game = Game(players[0], players[1], game_board=board)

    assert game.is_won(board, 'X') is False


def test_displays_the_board_and_a_message_on_game_over(game):
    console = MockConsole()
    game.show_game_over_screen(console)

    assert console.render_board_call_count == 1
    assert console.show_game_over_message_call_count == 1

import pytest
from ttt.game import Game
from ttt.console import Console
from tests.mocks import MockConsoleIO, MockPlayer, MockBoard


@pytest.fixture
def players():
    return [MockPlayer('player 1', 'O'), MockPlayer('player 2', 'X')]


@pytest.fixture
def game(players):
    return Game(game_board=MockBoard(), player_one=players[0], player_two=players[1])


def test_get_board_state_sends_a_message_to_board():
    board = MockBoard()
    game = Game(game_board=board)
    game.get_board_state()

    assert board.get_spaces_call_count == 1


def test_available_spaces_sends_a_message_to_board():
    board = MockBoard()
    game = Game(game_board=board)
    game.available_spaces()

    assert board.available_spaces_call_count == 1


def test_current_player_switches_to_player_two_after_player_one_turn(game, players):
    current_player_after_switch = players[1]
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert game.get_current_player() == current_player_after_switch


def test_current_player_reverts_to_player_one_after_player_two_turn(game, players):
    current_player_on_turn_three = players[0]
    console = Console(MockConsoleIO(['1']))
    game.play_turn(console)
    game.play_turn(console)

    assert game.get_current_player() == current_player_on_turn_three


def test_game_is_not_over_when_board_is_not_full(game):
    assert game.game_over() is False


def test_the_game_is_over_when_board_is_full():
    end_state_game = Game(game_board=MockBoard(spaces_remaining=0))

    assert end_state_game.game_over() is True


def test_the_game_is_over_if_a_player_has_won():
    board = MockBoard(line_to_check=['X', 'X', 'X'])
    won_game = Game(game_board=board)

    assert won_game.game_over() is True


def test_a_line_does_not_win_if_not_all_spaces_contain_the_same_marker():
    board = MockBoard(line_to_check=['X', 'X', 'O'])
    game = Game(game_board=board)

    assert game.is_won() is False


def test_a_line_wins_if_all_spaces_contain_the_same_marker():
    board = MockBoard(line_to_check=['X', 'X', 'X'])
    game = Game(game_board=board)

    assert game.is_won() is True


def test_a_line_does_not_win_if_all_spaces_are_empty():
    board = MockBoard(line_to_check=['-', '-', '-'])
    game = Game(game_board=board)

    assert game.is_won() is False


def test_play_turn_instructs_board_to_occupy_space(players):
    board = MockBoard()
    game = Game(game_board=board, player_one=players[0], player_two=players[1])
    game.play_turn(Console(MockConsoleIO(['1'])))

    assert board.place_marker_call_count == 1

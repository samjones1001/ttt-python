import pytest
from ttt.game import Game


class MockBoard:
    def __init__(self):
        self.occupy_space_call_count = 0
        self.get_spaces_call_count = 0

    def is_full(self):
        return False

    def place_marker(self, space, marker):
        self.occupy_space_call_count += 1

    def get_spaces(self):
        self.get_spaces_call_count += 1


class MockEndStateBoard:
    def is_full(self):
        return True


@pytest.fixture
def game():
    return Game(game_board=MockBoard())


@pytest.fixture
def custom_names_game():
    return Game(game_board=MockBoard(), player_one='!', player_two='@')


def test_returns_player_one(game):
    assert game.get_player_one() == 'O'


def test_player_one_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_one() == '!'


def test_returns_player_two(game):
    assert game.get_player_two() == 'X'


def test_player_two_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_two() == '@'


def test_get_board_state_sends_a_message_to_board():
    board = MockBoard()
    game = Game(board)
    game.get_board_state()
    assert board.get_spaces_call_count == 1


def test_returns_current_player(game):
    current_player_at_start = game.get_player_one()
    assert game.get_current_player() == current_player_at_start


def test_current_player_switches_to_player_two_after_player_one_turn(game):
    current_player_after_switch = game.get_player_two()
    game.play_turn(0)
    assert game.get_current_player() == current_player_after_switch


def test_current_player_reverts_to_player_one_after_player_two_turn(game):
    current_player_on_turn_three = game.get_player_one()
    game.play_turn(0)
    game.play_turn(1)
    assert game.get_current_player() == current_player_on_turn_three


def test_the_game_is_not_over_when_board_is_not_full(game):
    assert game.game_over() is False


def test_the_game_is_over_when_board_is_full():
    end_state_game = Game(game_board=MockEndStateBoard())
    assert end_state_game.game_over() is True


def test_play_turn_instructs_board_to_occupy_space():
    board = MockBoard()
    game = Game(board)
    game.play_turn(space='1')
    assert board.occupy_space_call_count == 1


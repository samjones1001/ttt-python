import pytest
from ttt.game import Game


class MockBoard:
    def __init__(self):
        self.occupy_space_call_count = 0
        self.get_spaces_call_count = 0

    def is_full(self):
        return False

    def place_marker(self, space_index, symbol):
        self.occupy_space_call_count += 1

    def get_spaces(self):
        self.get_spaces_call_count += 1


class MockEndStateBoard:
    def is_full(self):
        return True


@pytest.fixture
def standard_game():
    return Game(game_board=MockBoard())


@pytest.fixture
def custom_names_game():
    return Game(game_board=MockBoard(), player_one='!', player_two='@')


def test_returns_player_one(standard_game):
    assert standard_game.get_player_one() == 'O'


def test_player_one_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_one() == '!'


def test_returns_player_two(standard_game):
    assert standard_game.get_player_two() == 'X'


def test_player_two_can_have_custom_symbol(custom_names_game):
    assert custom_names_game.get_player_two() == '@'


def test_requests_the_boards_current_state():
    board = MockBoard()
    game = Game(board)
    game.get_board_state()
    assert board.get_spaces_call_count == 1


def test_returns_current_player(standard_game):
    current_player_at_start = standard_game.get_player_one()
    assert standard_game.get_current_player() == current_player_at_start


def test_play_turn_switches_the_current_player(standard_game):
    current_player_after_switch = standard_game.get_player_two()
    standard_game.play_turn(0)
    assert standard_game.get_current_player() == current_player_after_switch


def test_play_turn_can_switch_back_to_player_one(standard_game):
    current_player_on_turn_three = standard_game.get_player_one()
    standard_game.play_turn(0)
    standard_game.play_turn(1)
    assert standard_game.get_current_player() == current_player_on_turn_three


def test_the_game_is_not_over_when_board_is_not_full(standard_game):
    assert standard_game.game_over() is False


def test_the_game_is_over_when_board_is_full():
    end_state_game = Game(game_board=MockEndStateBoard())
    assert end_state_game.game_over() is True


def test_play_turn_instructs_board_to_occupy_space(standard_game):
    board = MockBoard()
    game = Game(board)
    game.play_turn(space_index='1')
    assert board.occupy_space_call_count == 1


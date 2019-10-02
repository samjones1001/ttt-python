import pytest
from ttt.game import Game
from ttt.player import Player
from ttt.console import Console


class MockBoard:
    def __init__(self):
        self.place_marker_call_count = 0
        self.get_spaces_call_count = 0
        self.available_spaces_call_count = 0

    def is_full(self):
        return False

    def place_marker(self, space, marker):
        self.place_marker_call_count += 1

    def get_spaces(self):
        self.get_spaces_call_count += 1

    def is_available_space(self, space):
        lowest_indexed_space = 0
        highest_indexed_space = 8
        occupied_space = 3
        if space < lowest_indexed_space or space > highest_indexed_space or space == occupied_space:
            return False
        else:
            return True

    def is_winning_line(self, line):
        return False

    def available_spaces(self):
        self.available_spaces_call_count += 1


class MockFullBoard:
    def is_full(self):
        return True

    def is_winning_line(self, line):
        return False


class MockBoardWithWinConditionMet:
    def is_full(self):
        return False

    def is_winning_line(self, line):
        return True


class MockConsoleIOInvalidInput:
    def get_input(self):
        return '-1'


class MockConsoleIOOccupiedInput:
    def get_input(self):
        return '3'


class MockConsoleIOValidInput:
    def get_input(self):
        return '1'


@pytest.fixture
def players():
    return [Player('player 1', 'O'), Player('player 2', 'X')]


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
    game.play_turn(Console(MockConsoleIOValidInput()))

    assert game.get_current_player() == current_player_after_switch


def test_current_player_reverts_to_player_one_after_player_two_turn(game, players):
    current_player_on_turn_three = players[0]
    game.play_turn(Console(MockConsoleIOValidInput()))
    game.play_turn(Console(MockConsoleIOValidInput()))

    assert game.get_current_player() == current_player_on_turn_three


def test_game_is_not_over_when_board_is_not_full(game):
    assert game.game_over() is False


def test_the_game_is_over_when_board_is_full():
    end_state_game = Game(game_board=MockFullBoard())

    assert end_state_game.game_over() is True


def test_the_game_is_over_if_a_player_has_won():
    won_game = Game(game_board=MockBoardWithWinConditionMet())

    assert won_game.game_over() is True


def test_play_turn_instructs_board_to_occupy_space():
    board = MockBoard()
    game = Game(game_board=board)
    game.play_turn(Console(MockConsoleIOValidInput()))

    assert board.place_marker_call_count == 1


def test_play_turn_raises_an_error_for_if_passed_an_occupied_space(game):
    with pytest.raises(Exception) as err:
        game.play_turn(Console(MockConsoleIOOccupiedInput()))

    assert "Invalid Move!" in str(err.value)


def test_play_turn_raises_an_error_for_if_passed_an_invalid_space(game):
    with pytest.raises(Exception) as err:
        game.play_turn(Console(MockConsoleIOInvalidInput()))

    assert "Invalid Move!" in str(err.value)

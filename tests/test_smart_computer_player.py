import pytest
from ttt.players.smart_computer_player import SmartComputerPlayer
from ttt.game.game import Game
from ttt.game.board import Board


class TestRunner:
    def setup_game(self, board_state):
        board = Board(board_state)
        player_1 = SmartComputerPlayer('Player 1', 'X')
        player_2 = SmartComputerPlayer('Player 2', 'O')

        return Game(player_1, player_2, board)


@pytest.fixture
def runner():
    return TestRunner()


def test_will_always_pick_the_center_space_if_available(runner):
    game = runner.setup_game(['O','2','3','4','5','6','7','8','9'])
    player = SmartComputerPlayer('Player 1', 'X')
    center_space_index = 4

    assert player.get_move(game) == center_space_index


def test_will_always_pick_a_winning_space_if_available(runner):
    game = runner.setup_game(['X','X','3','4','5','6','7','8','9'])
    player = SmartComputerPlayer('Player 1', 'X')
    game_winning_space_index = 2

    assert player.get_move(game) == game_winning_space_index


def test_will_always_prevent_opponent_from_winning_where_possible(runner):
    game = runner.setup_game(['O','O','3','4','5','6','7','8','9'])
    player = SmartComputerPlayer('Player 1', 'X')
    game_losing_space_index = 2

    assert player.get_move(game) == game_losing_space_index


def test_will_choose_to_win_a_game_over_preventing_an_opponent_from_winning(runner):
    game = runner.setup_game(['X','X','3','O','O','6','7','8','9'])
    player = SmartComputerPlayer('Player 1', 'X')
    game_winning_space_index = 2

    assert player.get_move(game) == game_winning_space_index
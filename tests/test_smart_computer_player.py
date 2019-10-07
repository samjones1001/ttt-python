from ttt.players.smart_computer_player import SmartComputerPlayer
from ttt.game.game import Game
from ttt.game.board import Board

def test_will_always_pick_the_center_space_if_available():
    board = Board(['O','-','-','-','-','-','-','-','-'])
    player_1 = SmartComputerPlayer('Player 1', 'X')
    player_2 = SmartComputerPlayer('Player 2', 'O')
    game = Game(player_1, player_2, board)
    center_space_index = 4

    assert player_1.get_move(game) == center_space_index


def test_will_always_pick_a_winning_space_if_available():
    board = Board(['X','X','-','-','-','-','-','-','-'])
    player_1 = SmartComputerPlayer('Player 1', 'X')
    player_2 = SmartComputerPlayer('Player 2', 'O')
    game = Game(player_1, player_2, board)
    game_winning_space_index = 2

    assert player_1.get_move(game) == game_winning_space_index


def test_will_always_prevent_opponent_from_winning_where_possible():
    board = Board(['O','O','-','-','-','-','-','-','-'])
    player_1 = SmartComputerPlayer('Player 1', 'X')
    player_2 = SmartComputerPlayer('Player 2', 'O')
    game = Game(player_1, player_2, board)
    game_losing_space_index = 2

    assert player_1.get_move(game) == game_losing_space_index


def test_will_choose_to_win_a_game_over_preventing_an_opponent_from_winning():
    board = Board(['X','X','-','O','O','-','-','-','-'])
    player_1 = SmartComputerPlayer('Player 1', 'X')
    player_2 = SmartComputerPlayer('Player 2', 'O')
    game = Game(player_1, player_2, board)
    game_winning_space_index = 2

    assert player_1.get_move(game) == game_winning_space_index
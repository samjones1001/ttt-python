from ttt.computer_player import ComputerPlayer


def test_computer_player_move_returns_the_index_of_an_available_space():
    spaces = ['-', 'X', 'X', 'O', 'O', 'X', 'X', 'O', 'O']
    computer_player = ComputerPlayer('player 2', 'X')

    assert computer_player.get_move(spaces) == 0



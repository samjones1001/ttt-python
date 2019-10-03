from ttt.computer_player import ComputerPlayer


def test_computer_player_move_returns_the_index_of_an_available_space():
    spaces = [1,5,7]
    computer_player = ComputerPlayer('player 2', 'X')

    assert computer_player.get_move(spaces) in spaces



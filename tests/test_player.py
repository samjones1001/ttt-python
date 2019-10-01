from ttt.player import Player

class MockConsole:
    def __init__(self):
        self.get_int_call_counter = 0

    def get_int(self):
        self.get_int_call_counter += 1


def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    player = Player('player 1', 'X')

    player.get_move(console)

    assert console.get_int_call_counter == 1

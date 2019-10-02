from ttt.player import Player


class MockConsole:
    def __init__(self):
        self.get_valid_input_call_counter = 0

    def get_valid_input(self, valid_inputs, error_message):
        self.get_valid_input_call_counter += 1
        return '0'


def test_human_player_moves_get_an_integer_from_the_console():
    console = MockConsole()
    player = Player('player 1', 'X')

    player.get_move([], console)

    assert console.get_valid_input_call_counter == 1

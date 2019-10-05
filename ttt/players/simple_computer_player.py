import random
from ttt.players.human_player import HumanPlayer


class SimpleComputerPlayer(HumanPlayer):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, board, console=None):
        spaces = board.available_spaces()
        return spaces[random.randint(0, len(spaces) - 1)]

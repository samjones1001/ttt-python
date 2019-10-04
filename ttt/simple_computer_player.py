import random
from ttt.player import Player


class SimpleComputerPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, game, console=None):
        spaces = game.available_spaces()
        return spaces[random.randint(0, len(spaces) - 1)]

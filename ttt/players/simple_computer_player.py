import random
from ttt.players.player import Player


class SimpleComputerPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, game):
        spaces = game.available_spaces()
        return spaces[random.randint(0, len(spaces) - 1)]


import random
from ttt.player import Player


class ComputerPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, spaces, console=None):
        available_spaces = [index for index, space in enumerate(spaces) if space == "-"]
        return available_spaces[random.randint(0, len(available_spaces) - 1)]
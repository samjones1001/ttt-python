from ttt.player import Player


class SmartComputerPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)
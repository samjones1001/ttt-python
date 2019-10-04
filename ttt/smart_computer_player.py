from ttt.player import Player


class SmartComputerPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, game, console=None):
        return self._find_best_move(game)

    def _find_best_move(self, game):
        return 1

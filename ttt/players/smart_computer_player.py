from ttt.players.human_player import HumanPlayer


class SmartComputerPlayer(HumanPlayer):
    def __init__(self, name, marker):
        super().__init__(name, marker)

    def get_move(self, game, console=None):
        return self._find_best_move(game)

    def _find_best_move(self, board):
        best_move = -1
        best_score = -100


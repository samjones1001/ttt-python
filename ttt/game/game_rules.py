class GameRules:
    def __init__(self):
        self._win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def game_over(self, board, opponent_marker):
        if self.is_tie(board) or self.is_won(board, opponent_marker):
            return True
        return False

    def is_tie(self, board):
        return board.is_full()

    def is_won(self, board, marker):
        for condition in self._win_conditions:
            line = board.retrieve_line(condition)
            if len(set(line)) == 1 and line[0] == marker:
                return True
        return False

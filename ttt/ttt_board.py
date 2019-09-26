from games.board import Board


class TTTBoard(Board):
    def __init__(self, spaces=9):
        super().__init__(spaces)

    def occupy_space(self, space_index, symbol):
        self.get_spaces()[space_index] = symbol

    def is_full(self):
        return self.get_spaces().count("-") == 0

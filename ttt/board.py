import math


class Board:
    def __init__(self, spaces=9):
        self._spaces = [space for space in self._generate_spaces(spaces)]

    def get_spaces(self):
        return self._spaces

    def occupy_space(self, space_index, symbol):
        self.get_spaces()[space_index] = symbol

    def is_full(self):
        return self.get_spaces().count("-") == 0

    def _generate_spaces(self, space_count):
        self._is_square_board(space_count)
        for _ in range(space_count):
            yield "-"

    def _is_square_board(self, space_count):
        if not self._is_square_number(space_count):
            raise Exception("Please set the number of spaces to a square number")

    def _is_square_number(self, num):
        return int(math.sqrt(num) + 0.5) ** 2 == num

class Board:
    def __init__(self):
        self._spaces = ['-'] * 9

    def get_spaces(self):
        return self._spaces

    def place_marker(self, space, marker):
        self._spaces[space] = marker

    def is_full(self):
        return '-' not in self._spaces

    def is_occupied_space(self, space):
        return self._spaces[space] is not '-'


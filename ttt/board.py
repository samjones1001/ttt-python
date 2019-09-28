class Board:
    def __init__(self):
        self._spaces = ['-'] * 9

    def get_spaces(self):
        return self._spaces

    def place_marker(self, space_index, marker):
        self._spaces[space_index] = marker

    def is_full(self):
        return '-' not in self._spaces


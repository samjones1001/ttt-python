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

    def is_existing_space(self, space):
        return False if self._is_out_of_bounds_space(space) else True

    def _is_out_of_bounds_space(self, space):
        return space > len(self.get_spaces()) - 1 or space < 0


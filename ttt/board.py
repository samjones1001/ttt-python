class Board:
    def __init__(self):
        self._spaces = ['-'] * 9

    def get_spaces(self):
        return self._spaces

    def place_marker(self, space, marker):
        self._spaces[space] = marker

    def is_full(self):
        return '-' not in self._spaces

    def is_available_space(self, space):
        return False if self._is_out_of_bounds_space(space) or \
                        self._is_occupied_space(space) else True

    def available_spaces(self):
        return [index for index, space in enumerate(self._spaces) if space == "-"]

    def is_winning_line(self, line):
        markers = [space for space in self._get_markers_for_line(line)]
        return len(set(markers)) == 1 and markers[0] != '-'

    def _is_occupied_space(self, space):
        return self._spaces[space] is not '-'

    def _is_out_of_bounds_space(self, space):
        return space > len(self.get_spaces()) - 1 or space < 0

    def _get_markers_for_line(self, spaces):
        for index in spaces:
            yield self._spaces[index]
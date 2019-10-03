class Board:
    def __init__(self):
        self._spaces = ['-'] * 9

    def get_spaces(self):
        return self._spaces

    def is_full(self):
        return len(self.available_spaces()) == 0

    def available_spaces(self):
        return [index for index, space in enumerate(self._spaces) if space == "-"]

    def place_marker(self, space, marker):
        self._spaces[space] = marker

    def retrieve_line(self, line):
        return [space for space in self._get_markers_for_line(line)]

    def _get_markers_for_line(self, spaces):
        for index in spaces:
            yield self._spaces[index]
import copy


class Board:
    def __init__(self, state=None):
        self._spaces = self._set_spaces(state)

    def get_spaces(self):
        return self._spaces

    def is_full(self):
        return len(self.available_spaces()) == 0

    def available_spaces(self):
        return [index for index, space in enumerate(self._spaces) if space == " "]

    def place_marker(self, space, marker):
        state = copy.deepcopy(self._spaces)
        state[space] = marker
        return Board(state)

    def retrieve_line(self, line):
        return [self._spaces[index] for index in line]

    def _set_spaces(self, state):
        spaces = [' ']*9 if state is None else state
        return spaces

    def _get_markers_for_line(self, spaces):
        for index in spaces:
            yield self._spaces[index]



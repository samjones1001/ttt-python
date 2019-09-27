import math
from ttt.console import Console


class Interface:
    def __init__(self, console=Console()):
        self._console = console

    def get_console(self):
        return self._console

    def render_board(self, board_state):
        self.get_console().print_output(self._build_board_output(board_state))

    def get_int(self):
        try:
            return int(self.get_console().get_input(self))
        except ValueError:
            raise Exception("Input was not a number!")

    def _build_board_output(self, board_state):
        spaces_per_line = self._find_board_size(board_state)
        lines = self._build_lines(board_state, spaces_per_line)
        dividers = self._build_dividers(spaces_per_line)
        return dividers.join(lines)

    def _build_lines(self, board_state, spaces_per_line):
        line_arrays = self._split_board_to_lines(board_state, spaces_per_line)
        return [self._build_line_string(line) for line in line_arrays]

    def _find_board_size(self, board_state):
        return int(math.sqrt(len(board_state)))

    def _split_board_to_lines(self, board_state, spaces_per_line):
        for i in range(0, len(board_state), spaces_per_line):
            yield board_state[i:i + spaces_per_line]

    def _build_line_string(self, line_array):
        line = ' | '.join(line_array).replace('-', ' ')
        return self._pad_string(line)

    def _pad_string(self, string):
        return f" {string} "

    def _build_dividers(self, grid_width):
        divider = '-' * self._divider_length(grid_width)
        return f"\n{divider}\n"

    def _divider_length(self, grid_width):
        return (grid_width * 3) + (grid_width - 1)

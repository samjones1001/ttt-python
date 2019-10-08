import re
from ttt.console_ui.consoleio import ConsoleIO


class Console:
    def __init__(self, io=ConsoleIO()):
        self._io = io

    def render_board(self, board_state):
        board_string = self._build_board_output(board_state)
        self._io.print_output(board_string)

    def get_valid_input(self, valid_inputs, error):
        user_input = self._io.get_input()
        while not re.search(valid_inputs, user_input):
            self._io.print_output(error)
            user_input = self._io.get_input()
        return user_input

    def output_message(self, message):
        self._io.print_output(message)

    def _build_board_output(self, board_state):
        lines = self._build_lines(board_state)
        dividers = self._build_dividers()
        return dividers.join(lines)

    def _build_lines(self, board_state):
        line_arrays = self._split_board_to_lines(board_state)
        return [self._build_line_string(line) for line in line_arrays]

    def _split_board_to_lines(self, board_state):
        spaces_per_line = 3
        for i in range(0, len(board_state), spaces_per_line):
            yield board_state[i:i + spaces_per_line]

    def _build_line_string(self, line_array):
        line = ' | '.join(line_array)
        return self._pad_string(line)

    def _pad_string(self, string):
        return f" {string} "

    def _build_dividers(self):
        divider_length = 11
        divider = '-' * divider_length
        return f"\n{divider}\n"


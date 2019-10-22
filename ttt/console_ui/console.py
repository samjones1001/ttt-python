import re
from ttt.console_ui.consoleio import ConsoleIO
import ttt.constants as constants


class Console:
    def __init__(self, io=ConsoleIO()):
        self._io = io

    def render_board(self, board_state, player_1, player_2):
        self._io.clear()
        board_string = self._build_board_output(board_state, player_1, player_2)
        self._io.print_output(board_string)

    def get_validated_input(self, valid_inputs, error):
        user_input = self._io.get_input()
        while not re.search(valid_inputs, user_input):
            self._io.print_output(error)
            user_input = self._io.get_input()
        return user_input

    def output_message(self, message):
        self._io.print_output(message)

    def clear_output(self):
        self._io.clear()

    def _build_board_output(self, board_state, player_1, player_2):
        lines = self._build_lines(board_state, player_1, player_2)
        dividers = self._build_dividers()
        return dividers.join(lines)

    def _build_lines(self, board_state, player_1, player_2):
        line_arrays = self._split_board_to_lines(board_state)
        return [self._build_line_string(line, player_1, player_2) for line in line_arrays]

    def _split_board_to_lines(self, board_state):
        spaces_per_line = 3
        for i in range(0, len(board_state), spaces_per_line):
            yield board_state[i:i + spaces_per_line]

    def _build_line_string(self, line_array, player_1, player_2):
        line = ' | '.join(self._format_cells(line_array, player_1, player_2))
        return self._pad_string(line)

    def _format_cells(self, line, player_1, player_2):
        return [self._format_cell(cell, player_1, player_2) for cell in line]

    def _format_cell(self, cell, player_1, player_2):
        if cell == player_1.get_marker():
            color = player_1.get_marker_colour()
        elif cell == player_2.get_marker():
            color =player_2.get_marker_colour()
        else:
            color = ''

        cell = f"{color}{cell}{constants.END_COLOUR}"

        if not re.search(constants.EMOJI_REGEX, cell) or len(cell) == 2:
            return f'{cell} '
        return cell

    def _pad_string(self, string):
        return f" {string} "

    def _build_dividers(self):
        divider_length = 14
        divider = '-' * divider_length
        return f"\n{divider}\n"


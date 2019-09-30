from ttt.consoleio import ConsoleIO


class Console:
    def __init__(self, io=ConsoleIO()):
        self._io = io

    def get_console_io(self):
        return self._io

    def render_board(self, board_state):
        self._io.print_output(self._build_board_output(board_state))

    def output_message(self, message):
        self._io.print_output(message)

    def get_int(self):
        try:
            return int(self.get_console_io().get_input())
        except ValueError:
            raise Exception("Input was not a number!")

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
        line = ' | '.join(line_array).replace('-', ' ')
        return self._pad_string(line)

    def _pad_string(self, string):
        return f" {string} "

    def _build_dividers(self):
        divider_length = 11
        divider = '-' * divider_length
        return f"\n{divider}\n"


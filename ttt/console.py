from ttt.consoleio import ConsoleIO
from ttt.messages import GAME_WON_MESSAGE
from ttt.messages import GAME_TIED_MESSAGE


class Console:
    def __init__(self, io=ConsoleIO()):
        self._io = io

    def render_board(self, game):
        board_string = self._build_board_output(game.get_board_state())
        self._io.print_output(board_string)

    def get_valid_input(self, valid_inputs, error):
        user_input = self._io.get_input()
        while user_input not in valid_inputs:
            self._io.print_output(error)
            user_input = self._io.get_input()
        return user_input

    def output_message(self, message):
        self._io.print_output(message)

    def show_game_over_message(self,game):
        if game.is_won():
            message = f"{game.get_opponent_name()}{GAME_WON_MESSAGE}"
        else:
            message = f"{GAME_TIED_MESSAGE}"
        self.output_message(message)

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


class MockConsoleIO:
    def __init__(self, inputs=None):
        self.inputs = inputs
        self.get_input_call_count = 0
        self.last_output = None

    def get_input(self, message=""):
        self.get_input_call_count += 1
        return self.inputs.pop(0)

    def print_output(self, output):
        self.last_output = output


class MockConsole:
    def __init__(self, input_return='1'):
        self.input_return = input_return
        self.get_valid_input_call_count = 0
        self.output_message_call_count = 0
        self.render_board_call_count = 0
        self.show_game_over_message_call_count = 0

    def get_valid_input(self, valid_inputs, error_message):
        self.get_valid_input_call_count += 1
        return self.input_return

    def output_message(self, message):
        self.output_message_call_count += 1

    def render_board(self, _):
        self.render_board_call_count += 1

    def show_game_over_message(self, game):
        self.show_game_over_message_call_count += 1


class MockGameRunner():
    def __init__(self, console):
        self.run_call_count = 0
        self.player_2 = None

    def run(self, player_1, player_2):
        self.run_call_count += 1
        self.player_2 = player_2


class MockPlayer:
    def __init__(self, name, marker):
        self._name = name
        self._marker = marker
        self.get_move_call_count = 0

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def get_move(self, spaces, console):
        self.get_move_call_count += 1
        return 1


class MockGame:
    def __init__(self, board_state):
        self._board_state = board_state

    def get_board_state(self):
        return self._board_state


class MockBoard:
    def __init__(self, spaces_remaining=1, line_to_check=[]):
        self._spaces_remaining = spaces_remaining
        self._line_to_check = line_to_check
        self.place_marker_call_count = 0
        self.get_spaces_call_count = 0
        self.available_spaces_call_count = 0
        self.is_full_call_count = 0
        self.is_winning_line_call_count = 0

    def get_spaces(self):
        self.get_spaces_call_count += 1
        return []

    def is_full(self):
        self.is_full_call_count += 1
        return True if self._spaces_remaining == 0 else False

    def place_marker(self, space, marker):
        self.place_marker_call_count += 1
        self._spaces_remaining -= 1

    def is_available_space(self, space):
        lowest_indexed_space = 0
        highest_indexed_space = 8
        occupied_space = 3
        if space < lowest_indexed_space or space > highest_indexed_space or space == occupied_space:
            return False
        else:
            return True

    def retrieve_line(self, line):
        self.is_winning_line_call_count += 1
        return self._line_to_check

    def available_spaces(self):
        self.available_spaces_call_count += 1
        return None

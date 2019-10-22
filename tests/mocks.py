class MockConsoleIO:
    def __init__(self, inputs=None):
        self.inputs = inputs
        self.get_input_call_count = 0
        self.print_output_call_count = 0
        self.last_output = None
        self.clear_call_count = 0

    def get_input(self, message=""):
        self.get_input_call_count += 1
        return self.inputs.pop(0)

    def print_output(self, output):
        self.print_output_call_count += 1
        self.last_output = output

    def clear(self):
        self.clear_call_count += 1


class MockConsole:
    def __init__(self, inputs=['1']):
        self.inputs = inputs.copy()
        self.get_valid_input_call_count = 0
        self.output_message_call_count = 0
        self.render_board_call_count = 0
        self.clear_output_call_count = 0

    def get_validated_input(self, valid_inputs, error_message):
        self.get_valid_input_call_count += 1
        return self.inputs.pop(0)

    def output_message(self, message):
        self.output_message_call_count += 1

    def render_board(self, board, player_1, player_2):
        self.render_board_call_count += 1

    def clear_output(self):
        self.clear_output_call_count += 1

class MockPlayer:
    def __init__(self, name, marker, inputs=[1]):
        self._name = name
        self._marker = marker
        self._marker_colour = None
        self.get_move_call_count = 0
        self._inputs = inputs

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def get_marker_colour(self):
        return self._marker_colour

    def get_move(self, game):
        self.get_move_call_count += 1
        return self._inputs.pop(0)

    def set_marker(self, marker):
        self._marker = marker

    def set_marker_colour(self, colour):
        self._marker_colour = colour


class MockGame():
    def __init__(self,
                 board_state=None,
                 available_spaces=None,
                 turns_remaining=1):
        self._available_spaces = available_spaces
        self._turns_remaining = turns_remaining
        self.game_over_call_count = 0
        self.play_turn_call_count = 0

    def available_spaces(self):
        return self._available_spaces

    def game_over(self, console):
        result = self.game_over_call_count >= self._turns_remaining
        self.game_over_call_count += 1
        return result

    def play_turn(self, console):
        self.play_turn_call_count += 1

class MockConsoleIO:
    def __init__(self, inputs=None):
        self.inputs = inputs
        self.get_input_call_count = 0
        self.last_output = None
        self.clear_call_count = 0

    def get_input(self, message=""):
        self.get_input_call_count += 1
        return self.inputs.pop(0)

    def print_output(self, output):
        self.last_output = output

    def clear(self):
        self.clear_call_count += 1


class MockConsole:
    def __init__(self, inputs=['1']):
        self.inputs = inputs
        self.get_valid_input_call_count = 0
        self.output_message_call_count = 0
        self.render_board_call_count = 0

    def get_validated_input(self, valid_inputs, error_message):
        self.get_valid_input_call_count += 1
        return self.inputs.pop(0)

    def output_message(self, message):
        self.output_message_call_count += 1

    def render_board(self, _):
        self.render_board_call_count += 1


class MockGameRunner():
    def __init__(self, console):
        self.run_call_count = 0
        self.player_1 = None
        self.player_2 = None

    def run(self, player_1, player_2):
        self.run_call_count += 1
        self.player_1 = player_1
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

    def get_move(self, game):
        self.get_move_call_count += 1
        return 1


class MockGame:
    def __init__(self,
                 board_state=None,
                 available_spaces=None,
                 turns_remaining=1):
        self._board_state = self._set_board_state(board_state)
        self._available_spaces = available_spaces
        self._turns_remaining = turns_remaining
        self.game_over_call_count = 0
        self.play_turn_call_count = 0
        self.show_game_over_screen_call_count = 0

    def get_board_state(self):
        return self._board_state

    def available_spaces(self):
        return self._available_spaces

    def game_over(self, console):
        result = self.game_over_call_count >= self._turns_remaining
        self.game_over_call_count += 1
        return result

    def play_turn(self, console):
        self.play_turn_call_count += 1

    def _set_board_state(self, board_state):
        if board_state is None:
            return []
        return board_state


class MockBoard:
    def __init__(self):
        self.place_marker_call_count = 0
        self.get_spaces_call_count = 0
        self.available_spaces_call_count = 0

    def get_spaces(self):
        self.get_spaces_call_count += 1
        return []

    def place_marker(self, space, marker):
        self.place_marker_call_count += 1

    def available_spaces(self):
        self.available_spaces_call_count += 1

from ttt import constants
from ttt.console_ui.console import Console
from ttt.networking.socket import Socket


class TTTClient:
    def __init__(self, console=Console()):
        self._socket = None
        self._console = console
        self._turns = 0
        self._last_board_state = None

    def send_data(self, data):
        encoded_data = data.encode(constants.ENCODING_STRING)
        self._socket.send_data(encoded_data)

    def start(self, host=constants.LOCAL_HOST_STRING, socket_type=Socket):
        self._set_socket(host, socket_type)
        self._connect()
        self._console.clear_output()

    def play(self):
        while self._game_in_progress():
            self._display_game_state()
            if self._turns % 2 != 0:
                move = self._console.get_validated_input(constants.DIGIT_REGEX, constants.NUMBER_ERROR)
                self.send_data(move)
            self._turns += 1

    def _set_socket(self, host, socket_type):
        self._socket = socket_type(host)

    def _connect(self):
        self._socket.connect()

    def _game_in_progress(self):
        return not self._last_board_state or any(char.isdigit() for char in self._last_board_state)

    def _display_game_state(self):
        data = self._socket.receive_data().decode(constants.ENCODING_STRING)
        self._console.output_message(data)
        self._last_board_state = data.split('\n\n')[0]




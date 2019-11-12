from ttt import constants
from ttt.console_ui.console import Console
from ttt.networking.socket import Socket


class TTTClient:
    def __init__(self, console=Console()):
        self._socket = None
        self._console = console
        self._turns = 0
        self._last_board_state = '0'

    def send_data(self, data):
        encoded_data = data.encode('utf-8')
        self._socket.send_data(encoded_data)

    def start(self, host='127.0.0.1', socket_type=Socket):
        self._set_socket(host, socket_type)
        self._connect()
        self._console.clear_output()

    def play(self):
        print(111111)
        while self._game_in_progress():
            print(2222222)
            self._display_game_state()
            if self._turns % 2 != 0:
                print(33333)
                move = self._console.get_validated_input(constants.DIGIT_REGEX, 'Please input a digit')
                self.send_data(move)
            self._turns += 1

    def _set_socket(self, host, socket_type):
        self._socket = socket_type(host)

    def _connect(self):
        self._socket.connect()

    def _game_in_progress(self):
        return any(char.isdigit() for char in self._last_board_state)

    def _display_game_state(self):
        data = self._socket.receive_data().decode('utf-8')
        self._console.output_message(data)
        self._last_board_state = data.split('\n\n')[0]




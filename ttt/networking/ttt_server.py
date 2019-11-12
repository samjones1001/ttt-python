from ttt import constants
from ttt.networking.socket import Socket


class TTTServer:
    def __init__(self, host=constants.LOCAL_HOST_STRING, socket=Socket):
        self._socket = socket(host)
        self._connection = None
        self._client_address = None

    def get_socket(self):
        return self._socket

    def start(self):
        self._connection, self._client_address = self._socket.setup()

    def accept_input(self):
        return self._connection.recv(1024).decode(constants.ENCODING_STRING)

    def send_data(self, data):
        encoded_data = data.encode(constants.ENCODING_STRING)
        self._connection.send(encoded_data)

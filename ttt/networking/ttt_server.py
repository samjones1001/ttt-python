from ttt.networking.socket import Socket


class TTTServer:
    def __init__(self, host='127.0.0.1', socket=Socket):
        self._socket = socket(host)
        self._connection = None
        self._client_address = None

    def get_socket(self):
        return self._socket

    def start(self):
        self._connection, self._client_address = self._socket.setup()

    def accept_input(self):
        return self._connection.recv(1024).decode('utf-8')

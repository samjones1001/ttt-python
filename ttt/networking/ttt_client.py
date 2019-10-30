from ttt.networking.socket import Socket


class TTTClient:
    def __init__(self):
        self._socket = None

    def set_socket(self, host, socket_type=Socket):
        self._socket = socket_type(host)

    def connect(self):
        self._socket.connect()

    def send_data(self, data):
        encoded_data = data.encode('utf-8')
        self._socket.send_data(encoded_data)

    def receive_data(self):
        return self._socket.receive_data().decode('utf-8')

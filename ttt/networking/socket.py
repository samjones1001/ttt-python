import socket

class Socket:
    def __init__(self, host):
        self._host = host
        self._port = 65432
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setup(self):
        self._socket.bind((self._host, self._port))
        self._socket.listen()
        return self._socket.accept()

    def connect(self):
        self._socket.connect((self._host, self._port))

    def send_data(self, data):
        self._socket.send(data)

    def receive_data(self):
        return self._socket.recv(1024)
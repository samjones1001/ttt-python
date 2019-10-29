import socket

class Socket:
    def __init__(self):
        self._host = '127.0.0.1'
        self._port = 65432
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._socket.connect((self._host, self._port))

    def send_data(self, data):
        encoded_data = data.encode('utf-8')
        self._socket.send(encoded_data)

    def receive_data(self):
        return self._socket.recv(1024)
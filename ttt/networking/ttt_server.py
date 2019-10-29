from ttt.networking.socket import Socket


class TTTServer:
    def __init__(self):
        self._socket = None

    def set_socket(self, host, socket_type=Socket):
        self._socket = socket_type(host)

    def start(self):
        conn, addr = self._socket.setup()

        with conn:
            print("Connected by", addr)
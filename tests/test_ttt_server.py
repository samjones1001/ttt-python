from tests.mocks import MockSocket
from ttt.networking.ttt_server import TTTServer


def test_sets_up_a_socket_bound_to_the_passed_ip():
    server = TTTServer()
    server.set_socket('127.0.0.1', MockSocket)

    assert server._socket.host == '127.0.0.1'
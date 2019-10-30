from tests.mocks import MockSocket
from ttt.networking.ttt_server import TTTServer


def test_sets_up_a_socket_bound_to_the_passed_ip():
    server = TTTServer('127.0.0.1', socket=MockSocket)

    assert server.get_socket().host == '127.0.0.1'
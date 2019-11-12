from tests.mocks import MockSocket
from ttt.networking.ttt_server import TTTServer


def test_sets_up_a_socket_bound_to_the_passed_ip():
    server = TTTServer('127.0.0.1', socket=MockSocket)

    assert server.get_socket().host == '127.0.0.1'


def test_sets_a_connection_and_stores_the_connection_address():
    server = TTTServer('127.0.0.1', socket=MockSocket)

    server.start()

    assert server._connection is not None
    assert server._client_address is not None


def tests_gets_a_byte_like_object_from_the_connection_and_decodes_it_to_a_string():
    server = TTTServer('127.0.0.1', socket=MockSocket)
    server.get_socket().input = b'Some input'

    server.start()

    assert server.accept_input() == "Some input"


def test_encodes_a_string_to_a_bytes_like_object_and_sends_it_to_the_connection():
    server = TTTServer('127.0.0.1', socket=MockSocket)

    server.start()
    server.send_data('Some input')

    assert server.get_socket().last_sent_data() == b'Some input'

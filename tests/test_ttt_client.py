from tests.mocks import MockSocket
from ttt.networking.ttt_client import TTTClient


def test_sets_up_a_socket_bound_to_the_passed_ip():
    client = TTTClient()
    client.set_socket('127.0.0.1', MockSocket)

    assert client._socket.host == '127.0.0.1'


def test_connects_the_socket():
    client = TTTClient()
    client.set_socket('127.0.0.1', MockSocket)
    client.connect()

    assert client._socket.connect_call_count == 1

def test_encodes_a_string_to_bytes_like_object_and_sends_it_to_socket():
    client = TTTClient()
    client.set_socket('127.0.0.1', MockSocket)

    client.send_data("Data to send")

    assert client._socket.sent_data == b'Data to send'


def test_receives_a_bytes_like_object_from_socket_and_decodes_to_string():
    client = TTTClient()
    client.set_socket('127.0.0.1', MockSocket)

    client._socket.received_data = b'Received data'

    assert client.receive_data() == "Received data"

from tests.mocks import MockSocket, MockConsoleIO
from ttt.console_ui.console import Console
from ttt.networking.ttt_client import TTTClient


def test_sets_up_a_socket_bound_to_the_passed_ip():
    client = TTTClient()
    client.start('127.0.0.1', MockSocket)

    assert client._socket.host == '127.0.0.1'


def test_connects_the_socket():
    client = TTTClient()
    client.start('127.0.0.1', MockSocket)

    assert client._socket.connect_call_count == 1


def test_encodes_a_string_to_bytes_like_object_and_sends_it_to_socket():
    client = TTTClient()
    client.start('127.0.0.1', MockSocket)

    client.send_data("Data to send")

    assert client._socket.sent_data == b'Data to send'


def test_prints_received_data_while_game_is_in_progress():
    console_io = MockConsoleIO(['1'])
    console = Console(console_io)
    client = TTTClient(console)

    client.start('127.0.0.1', MockSocket)
    client._socket.received_data = [b'Board\n\nMessage']

    client.play()

    assert console_io.last_output == "Board\n\nMessage"


def test_send_an_encoded_string_to_the_socket():
    console_io = MockConsoleIO(['1'])
    console = Console(console_io)
    client = TTTClient(console)

    client.start('127.0.0.1', MockSocket)
    client._socket.received_data = [b'1\n\nMessage', b'Board\n\nMessage']

    client.play()

    assert client._socket.sent_data == b'1'


def test_will_continue_to_prompt_if_provided_non_integer_input():
    console_io = MockConsoleIO(['not an integer', '!', '1'])
    console = Console(console_io)
    client = TTTClient(console)

    client.start('127.0.0.1', MockSocket)
    client._socket.received_data = [b'1\n\nMessage', b'Board\n\nMessage']

    client.play()

    assert client._socket.sent_data == b'1'
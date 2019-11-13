from tests.mocks import MockPlayer, MockServer, MockConsoleIO
from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game_config import Config
from ttt.game.networked_game_runner import NetworkedGameRunner


def test_creates_a_game_object_with_the_passed_config_parameters():
    runner = NetworkedGameRunner()
    player_1 = MockPlayer('Player 1', 'X')
    player_2 = MockPlayer('Player 2', 'O')
    board = Board(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])

    config = Config(
        first_player=player_1,
        second_player=player_2,
        board=board,
        server=MockServer()
    )

    runner.run(config)

    game = runner.get_game()

    assert game.get_board() == board
    assert game.get_current_player_name() == 'Player 1'
    assert game.get_opponent_name() == 'Player 2'


def test_creates_and_sends_a_string_representing_current_game_state_on_each_turn():
    expected_data_string = " X\x1b[0m  | X\x1b[0m  | 3\x1b[0m  \n--------------\n 4\x1b[0m  | 5\x1b[0m  | 6\x1b[0m  \n--------------\n 7\x1b[0m  | 8\x1b[0m  | 9\x1b[0m  \n\n\nPlayer 1's turn."
    console_io = MockConsoleIO()
    console = Console(console_io)
    runner = NetworkedGameRunner(console)

    player_1 = MockPlayer('Player 1', 'X', inputs=[2])
    player_2 = MockPlayer('Player 2', 'O')
    board = Board(['X', 'X', '3', '4', '5', '6', '7', '8', '9'])
    server = MockServer()

    config = Config(
        first_player=player_1,
        second_player=player_2,
        board=board,
        server=server
    )

    runner.run(config)

    assert server.sent_data == expected_data_string
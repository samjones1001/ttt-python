import pytest

from tests.mocks import MockPlayer, MockConsole, MockConsoleIO, MockPersisterIO, MockGame
from ttt.console_ui.console import Console
from ttt.game.board import Board
from ttt.game.game import Game
from ttt.game.game_runner import GameRunner, Config
from ttt.messages import game_tied_message
from ttt.persister.persister import Persister


@pytest.fixture
def players():
    return [MockPlayer('player 1', 'O'), MockPlayer('player 2', 'X')]


def test_checks_for_game_over_state_each_turn_and_at_game_over_state(players):
    game_runner = GameRunner(MockConsole(), game_class=MockGame)
    game_runner.run(Config(players[0], players[1], Board()))

    assert game_runner.get_game().game_over_call_count == 2


def test_plays_a_turn_when_game_is_not_over(players):
    game_runner = GameRunner(MockConsole(), game_class=MockGame)
    game_runner.run(Config(players[0], players[1], Board()))

    assert game_runner.get_game().play_turn_call_count == 1


def test_can_play_a_full_game():
    io = MockConsoleIO([])
    game_runner = GameRunner(Console(io))
    player_1 = MockPlayer('player 1', 'O', [0, 1, 6, 5, 8])
    player_2 = MockPlayer('player 2', 'X', [4, 2, 3, 7])
    config = Config(player_1, player_2, Board())

    game_runner.run(config)

    assert io.last_output == game_tied_message()


def test_game_ends_if_a_player_wins():
    io = MockConsoleIO([])
    game_runner = GameRunner(Console(io))
    player_1 = MockPlayer('player 1', 'O', [0, 2, 4, 6])
    player_2 = MockPlayer('player 2', 'X', [1, 3, 5])
    config = Config(player_1, player_2, Board())

    game_runner.run(config)

    assert "player 1 won!" in io.last_output


def test_a_game_which_is_stopped_but_not_in_progress_does_not_get_saved():
    player_1 = MockPlayer('player 1', 'O', [0, 1, 2])
    player_2 = MockPlayer('player 2', 'X', [3, 4])
    io = MockConsoleIO([])
    persister_io = MockPersisterIO()
    persister = Persister(persister_io)
    game_runner = GameRunner(Console(io), persister)

    config = Config(player_1, player_2, Board())

    game_runner.run(config)
    game_runner.stop()

    assert persister_io.saved_data is None


def test_a_game_which_is_stopped_while_in_progress_gets_saved():
    player_1 = MockPlayer('player 1', 'O', [])
    player_2 = MockPlayer('player 2', 'X', [])
    io = MockConsoleIO([])
    persister_io = MockPersisterIO()
    persister = Persister(persister_io)
    game_runner = GameRunner(Console(io), persister)
    game_runner._game = Game(player_1, player_2)


    game_runner.stop()

    assert persister_io.saved_data is not None

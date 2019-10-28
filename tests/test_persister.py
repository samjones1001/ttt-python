import json

import pytest

from tests.mocks import MockPersisterIO
from ttt.game.board import Board
from ttt.game.game import Game
from ttt.persister.persister import Persister
from ttt.players.simple_computer_player import SimpleComputerPlayer


@pytest.fixture()
def save_game_json_data():
    board_state = ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9']
    current_player = SimpleComputerPlayer('Player 1', 'O')
    opponent = SimpleComputerPlayer('Player 2', 'X')
    save_id = '1'

    return create_json_object_for_save_data(board_state, current_player, opponent, save_id)


def create_json_object_for_save_data(board_state, current_player, opponent, save_id):
    save_data = { save_id: {
                'board': board_state,
                'current_player': {
                    'name': current_player.get_name(),
                    'type': type(current_player).__name__,
                    'marker': current_player.get_marker(),
                    'colour': current_player.get_marker_colour()
                },
                'opponent': {
                    'name': opponent.get_name(),
                    'type': type(opponent).__name__,
                    'marker': opponent.get_marker(),
                    'colour': opponent.get_marker_colour()
                }}}

    return json.dumps(save_data)


def test_sends_a_json_representation_of_the_game_to_be_saved(save_game_json_data):
    persister_io = MockPersisterIO()
    persister = Persister(persister_io)
    board = Board(['X', 'O', 'X', 'O', '5', '6', '7', '8', '9'])
    player_1 = SimpleComputerPlayer('Player 1', 'O')
    player_2 = SimpleComputerPlayer('Player 2', 'X')
    game = Game(player_1, player_2, board)

    persister.save('myfile.txt', game)

    assert persister_io.saved_data == save_game_json_data


def test_if_save_data_exists_new_save_is_added_with_an_incremented_save_id(save_game_json_data):
    persister_io = MockPersisterIO(save_game_json_data)
    persister = Persister(persister_io)
    board = Board(['X', 'O', 'X', 'O', '5', '6', '7', '8', '9'])
    player_1 = SimpleComputerPlayer('Player 1', 'O')
    player_2 = SimpleComputerPlayer('Player 2', 'X')
    game = Game(player_1, player_2, board)

    persister.save('myfile.txt', game)

    updated_data = json.loads(persister_io.saved_data)

    assert len(updated_data) == 2
    assert '2' in list(updated_data.keys())


def test_converts_a_json_representation_of_the_game_with_the_passed_id_into_a_config_object():
    board_state = ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9']
    current_player = SimpleComputerPlayer('Player 1', 'O')
    opponent = SimpleComputerPlayer('Player 2', 'X')
    save_id = '1'

    saved_game_json_data = create_json_object_for_save_data(board_state, current_player, opponent, save_id)
    persister_io = MockPersisterIO(saved_game_json_data)
    persister = Persister(persister_io)

    config = persister.load('myfile.txt', save_id)

    assert config.board.get_spaces() == ['X', 'O', 'X', 'O', '5', '6', '7', '8', '9']
    assert config.first_player.get_name() == "Player 1"
    assert config.second_player.get_name() == "Player 2"

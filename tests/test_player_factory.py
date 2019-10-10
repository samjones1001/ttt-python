import pytest
from ttt.players.player_factory import PlayerFactory
from ttt.console_ui.console import Console
from tests.mocks import MockConsoleIO


def test_creates_a_player_when_provided_a_valid_type():
    console = Console(MockConsoleIO())
    factory = PlayerFactory()

    player = factory.create('human', 'Player 1', 'X', console)

    assert player is not None


def test_throws_an_error_if_provided_a_non_valid_type():
    with pytest.raises(ValueError) as err:
        console = Console(MockConsoleIO())
        factory = PlayerFactory()

        factory.create('invalidType', 'Player 1', 'X', console)

    assert "invalidType is not a valid player type" in str(err.value)

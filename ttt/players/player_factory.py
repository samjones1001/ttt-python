import ttt.constants as constants
from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer


class PlayerFactory:

    def __init__(self):
        self._types = {
            constants.HUMAN_PLAYER_STRING: HumanPlayer,
            constants.SIMPLE_COMPUTER_STRING: SimpleComputerPlayer,
            constants.SMART_COMPUTER_STRING: SmartComputerPlayer
        }

    def create(self, player_type, name, marker, console):
        selected_type = self._types.get(player_type)
        if not selected_type:
            raise ValueError(f"{player_type} is not a valid player type")
        return selected_type(name, marker, console)




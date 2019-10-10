from ttt.players.human_player import HumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer


class PlayerFactory:

    def __init__(self):
        self._types = {
            'human': HumanPlayer,
            'simpleComputer': SimpleComputerPlayer,
            'smartComputer': SmartComputerPlayer
        }

    def create(self, player_type, name, marker, console):
        selected_type = self._types.get(player_type)
        if not selected_type:
            raise ValueError(f"{player_type} is not a valid player type")
        return selected_type(name, marker, console)




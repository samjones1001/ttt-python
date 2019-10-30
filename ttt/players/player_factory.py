import ttt.constants as constants
from ttt.players.human_player import HumanPlayer
from ttt.players.networked_human_player import NetworkedHumanPlayer
from ttt.players.simple_computer_player import SimpleComputerPlayer
from ttt.players.smart_computer_player import SmartComputerPlayer


class PlayerFactory:
    def create(self, player_type, name, marker, console, server=None):
        if player_type == constants.HUMAN_PLAYER_STRING:
            return HumanPlayer(name, marker, console)
        elif player_type == constants.NETWORKED_PLAYER_STRING:
            return NetworkedHumanPlayer(name, marker, server)
        elif player_type == constants.SIMPLE_COMPUTER_STRING:
            return SimpleComputerPlayer(name, marker)
        elif player_type == constants.SMART_COMPUTER_STRING:
            return SmartComputerPlayer(name, marker)
        else:
            raise ValueError(f"{player_type} is not a valid player type")




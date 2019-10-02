from ttt.player import Player
from ttt.computer_player import ComputerPlayer
from ttt.game_runner import GameRunner


class Interface:
    def __init__(self, console):
        self._console = console
        self._runner = None

    def start(self, game_runner=GameRunner):
        player_1 = Player('Player 1', 'O')
        player_2 = self._select_player_type('Player 2', 'X')
        self._runner = game_runner(self._console)
        self._runner.run(player_1, player_2)

    def _select_player_type(self, name, marker):
        input = self._console.get_int()
        if input == 1:
            return Player(name, marker)
        else:
            return ComputerPlayer(name, marker)


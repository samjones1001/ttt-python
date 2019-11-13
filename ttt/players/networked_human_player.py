from ttt.players.player import Player


class NetworkedHumanPlayer(Player):
    def __init__(self, name, marker, server):
        super().__init__(name, marker)
        self._server = server

    def get_move(self, game):
        return int(self._server.accept_input()) - 1

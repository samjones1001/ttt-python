from ttt.players.player import Player


class HumanPlayer(Player):
    def __init__(self, name, marker, console):
        super().__init__(name, marker, console)

    def get_move(self, game):
        space_strings = list(map(str, game.available_spaces()))
        return int(self._console.get_valid_input(space_strings, "Please select from available spaces"))

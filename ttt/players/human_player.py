from ttt.players.player import Player


class HumanPlayer(Player):
    def __init__(self, name, marker, console):
        super().__init__(name, marker, console)

    def get_move(self, game):
        spaces_regex = self._build_space_regex(game.available_spaces())
        return int(self._console.get_validated_input(spaces_regex, "Please select from available spaces"))

    def _build_space_regex(self, spaces):
        regex = '^['
        for space in spaces:
            regex += f'/{space}'
        return regex + ']$'


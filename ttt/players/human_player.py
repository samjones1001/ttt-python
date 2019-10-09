from ttt.players.player import Player


class HumanPlayer(Player):
    def __init__(self, name, marker, console):
        super().__init__(name, marker, console)

    def get_move(self, game):
        one_indexed_spaces = [index + 1 for index in game.available_spaces()]
        spaces_regex = self._build_space_regex(one_indexed_spaces)
        return int(self._console.get_validated_input(spaces_regex, "Please select from available spaces")) - 1

    def _build_space_regex(self, spaces):
        regex = '^['
        for space in spaces:
            regex += f'/{space}'
        return regex + ']$'


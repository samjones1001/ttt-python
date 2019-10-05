class HumanPlayer:
    def __init__(self, name, marker):
        self._name = name
        self._marker = marker

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def get_move(self, board, console):
        space_strings = list(map(str, board.available_spaces()))
        return int(console.get_valid_input(space_strings, "Please select from available spaces"))

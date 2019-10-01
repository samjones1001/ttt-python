class Player:
    def __init__(self, name, marker):
        self._name = name
        self._marker = marker

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def get_move(self, console, spaces=None):
        return console.get_int()

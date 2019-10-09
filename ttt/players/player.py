from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, marker, console=None):
        self._name = name
        self._marker = marker
        self._console = console

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def set_marker(self):
        marker_choice = self._console.get_validated_input('^$|[^\d\t/ */]', "Please choose a valid marker")
        if marker_choice != '':
            self._marker = marker_choice

    @abstractmethod
    def get_move(self, game):
        pass
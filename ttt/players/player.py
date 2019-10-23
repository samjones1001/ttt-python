from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, marker):
        self._name = name
        self._marker = marker
        self._marker_colour = None

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def get_marker_colour(self):
        return self._marker_colour

    def set_marker(self, marker=None):
        self._marker = marker

    def set_marker_colour(self, colour_code):
        self._marker_colour = colour_code

    @abstractmethod
    def get_move(self, game):
        pass
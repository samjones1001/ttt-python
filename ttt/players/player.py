from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, marker):
        self._name = name
        self._marker = marker

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def set_marker(self, marker=None):
        self._marker = marker

    @abstractmethod
    def get_move(self, game):
        pass
import tic_tac_toe as app
from ttt.cl_interface import CLInterface


class Runner:
    def __init__(self):
        self._current_index = 0

    def fake_input(self):
        values = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        current_value = values[self._current_index]
        self._current_index += 1
        return current_value


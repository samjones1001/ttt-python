import math


def render_board(board_state):
    print(_build_board_output(board_state))


def _build_board_output(board_state):
    spaces_per_line = _find_board_size(board_state)
    lines = _build_lines(board_state, spaces_per_line)
    dividers = _build_dividers(spaces_per_line)
    return dividers.join(lines)


def _build_lines(board_state, spaces_per_line):
    line_arrays = _split_board_to_lines(board_state, spaces_per_line)
    return [_build_line_string(line) for line in line_arrays]


def _find_board_size(board_state):
    return int(math.sqrt(len(board_state)))


def _split_board_to_lines(board_state, spaces_per_line):
    for i in range(0, len(board_state), spaces_per_line):
        yield board_state[i:i + spaces_per_line]


def _build_line_string(line_array):
    line = ' | '.join(line_array).replace('-', ' ')
    return _pad_string(line)


def _pad_string(string):
    return f" {string} "


def _build_dividers(grid_width):
    divider = '-' * _divider_length(grid_width)
    return f"\n{divider}\n"


def _divider_length(grid_width):
    return (grid_width * 3) + (grid_width - 1)

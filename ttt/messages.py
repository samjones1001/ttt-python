def welcome_message():
    return "Welcome to Tic-Tac-Toe!\n"


def player_type_message(name):
    return f"Select a player type for {name}\n\n" \
           f"(1) Human\n\n" \
           f"(2) Simple Computer\n\n" \
           f"(3) Tough Computer\n"


def marker_message(name, default_marker):
    return f"Select a marker for {name}. " \
           f"To use the default {default_marker}, just hit enter\n"


def turn_start_message(player, available_spaces):
    return f"{player}'s turn. Available Spaces: {available_spaces}"


def game_won_message(player):
    return f"{player} won!"


def game_tied_message():
    return "It's a tie!"

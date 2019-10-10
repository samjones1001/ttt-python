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


def invalid_marker_message():
    return "Please select a different marker from your opponent."


def turn_start_message(player, opponent, previous_move):
    message = f"\n{player}'s turn."
    if previous_move is not None:
        message += f" {opponent} chose space {previous_move}"
    return message


def game_won_message(player):
    return f"{player} won!"


def game_tied_message():
    return "It's a tie!"

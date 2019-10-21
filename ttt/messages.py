def welcome_message():
    return "Welcome to Tic-Tac-Toe!\nQuit the game at any time using ctrl+c.\n"


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


def player_choice_message():
    return "Which player should go first??\n\nPlayer (1) / Player (2)"


def turn_start_message(player, opponent, previous_move):
    message = f"\n{player}'s turn."
    if previous_move is not None:
        message += f" {opponent} chose space {previous_move}"
    return message


def game_won_message(player):
    return f"\n{player} won!\n\n"


def game_tied_message():
    return f"\nIt's a tie!\n\n"


def play_again_message():
    return "Play again?\n\n(y)es / (n)o"


def end_game_message():
    return "Thanks for playing!"

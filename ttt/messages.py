def welcome_message():
    return "Welcome to Tic-Tac-Toe!\nQuit the game at any time using ctrl+c.\n\n" \
           "What would you like to do?\n\n" \
           "(1) Play a local game\n(2) Play a networked game\n"


def new_or_load_message():
    return "Welcome to Tic-Tac-Toe!\nQuit the game at any time using ctrl+c.\n\n" \
           "What would you like to do?\n\n" \
           "(1) Play a new game\n(2) Load a game\n"


def load_game_message():
    return "Please enter the id of the game you wish to load\n"


def load_game_error_message(id):
    return f"No save game with id {id} exists"


def player_type_message(name):
    return f"Select a player type for {name}\n\n" \
           f"(1) Human\n\n" \
           f"(2) Simple Computer\n\n" \
           f"(3) Tough Computer\n"


def marker_message(name, default_marker):
    return f"Select a marker for {name}. " \
           f"To use the default {default_marker}, just hit enter\n"


def colour_message(name):
    return f"Select a colour for {name}'s marker\n(1) Red\n(2) Yellow\n(3) Blue\n(4) Green\n(5) Pink\n\n " \
           f"Press enter to use the default colour for your terminal."


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


def game_saved_message(save_id):
    return f"Your game has been saved with an id of {save_id}"


def end_game_message():
    return "Thanks for playing!"

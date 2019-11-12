PLAYER_1_NAME = 'Player 1'
PLAYER_1_MARKER = 'O'
PLAYER_2_NAME = 'Player 2'
PLAYER_2_MARKER = 'X'

HUMAN_PLAYER_STRING = 'HumanPlayer'
NETWORKED_PLAYER_STRING = 'NetworkedHumanPlayer'
SIMPLE_COMPUTER_STRING = 'SimpleComputerPlayer'
SMART_COMPUTER_STRING = 'SmartComputerPlayer'

PLAYER_CHOICES = {'1': HUMAN_PLAYER_STRING,
                  '2': SIMPLE_COMPUTER_STRING,
                  '3': SMART_COMPUTER_STRING}

DIGIT_REGEX = '^$|^[/1/2/3/4/5/6/7/8/9]{1}$'
TWO_OPTION_MENU_REGEX = '^[1/2]{1}$'
THREE_OPTION_MENU_REGEX = '^[/1/2/3]{1}$'
LOAD_GAME_ID_REGEX = '^\\d+$'
NORMAL_MARKER_REGEX = '^$|^[^\\d\t ]{1}$'
COLOUR_REGEX = '^$|^[/1/2/3/4/5/]{1}$'
EMOJI_REGEX = '^[\U0001F601-\U0001F64F]$|^[\U00002702-\U000027B0]$|^[\U0001F680-\U0001F6C0]$|^[\U000024C2-\U0001F251]$|^[\U000000A9-\U0001F5FF]$|^[\U0001F600-\U0001F636]$|^[\U0001F681-\U0001F6C5]$|^[\U0001F30D-\U0001F567]$'
MARKER_REGEX = f'{NORMAL_MARKER_REGEX}|^{EMOJI_REGEX}$'
PLAY_AGAIN_REGEX = '^[/y/n/Y/N]{1}$'

MENU_ERROR = "Please select an option from the menu"
MARKER_ERROR = "Please choose a valid marker. This can be an emoji or any character except for numbers and white space"
EMOJI_ERROR = "Please enter a valid emoji name"
SPACES_ERROR = "Please select from available spaces"
NUMBER_ERROR = "Please enter a number"

ONE_CHAR = '1'
TWO_CHAR = '2'
CONFIRMATION_CHAR = 'y'

NO_COLOUR = ''
COLOURS = {
    '1': '\033[91m',
    '2': '\033[93m',
    '3': '\033[94m',
    '4': '\033[92m',
    '5': '\033[95m',
    '': NO_COLOUR,
}
END_COLOUR = '\033[0m'

SAVE_GAME_REPO_PATH = './ttt/persister/data.txt'

BOARD_KEY = 'board'
CURRENT_PLAYER_KEY = 'current_player'
OPPONENT_KEY = 'opponent'
NAME_KEY = 'name'
TYPE_KEY = 'type'
MARKER_KEY = 'marker'
COLOUR_KEY = 'colour'

LOCAL_HOST_STRING = '127.0.0.1'
PORT_STRING = '65432'
ENCODING_STRING = 'utf-8'



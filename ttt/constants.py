PLAYER_1_NAME = 'Player 1'
PLAYER_1_MARKER = 'O'
PLAYER_2_NAME = 'Player 2'
PLAYER_2_MARKER = 'X'

HUMAN_PLAYER_STRING = 'human'
SIMPLE_COMPUTER_STRING = 'simpleComputer'
SMART_COMPUTER_STRING = 'smartComputer'

PLAYER_SELECTION_REGEX = '^[/1/2/3]{1}$'
DEFAULT_ORDER_REGEX = '^[1/2]{1}$'
NORMAL_MARKER_REGEX = '^$|^[^\\d\t ]{1}$'
COLOUR_REGEX = '^$|^[/1/2/3/4/5/]{1}$'
EMOJI_REGEX = '^[\U0001F601-\U0001F64F]$|^[\U00002702-\U000027B0]$|^[\U0001F680-\U0001F6C0]$|^[\U000024C2-\U0001F251]$|^[\U000000A9-\U0001F5FF]$|^[\U0001F600-\U0001F636]$|^[\U0001F681-\U0001F6C5]$|^[\U0001F30D-\U0001F567]$'
MARKER_REGEX = f'{NORMAL_MARKER_REGEX}|^{EMOJI_REGEX}$'
PLAY_AGAIN_REGEX = '^[/y/n/Y/N]{1}$'

MENU_ERROR = "Please select an option from the menu"
MARKER_ERROR = "Please choose a valid marker"
EMOJI_ERROR = "Please enter a valid emoji name"
SPACES_ERROR = "Please select from available spaces"

CONFIRMATION_CHAR = 'y'

COLOURS = {
    '1': '\033[91m',
    '2': '\033[93m',
    '3': '\033[94m',
    '4': '\033[92m',
    '5': '\033[95m',
    '': '',
}
END_COLOUR = '\033[0m'



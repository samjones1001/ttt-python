from ttt.console_ui.emoji import emoji_regex

PLAYER_1_NAME = 'Player 1'
PLAYER_1_MARKER = 'O'
PLAYER_2_NAME = 'Player 2'
PLAYER_2_MARKER = 'X'

HUMAN_PLAYER_STRING = 'human'
SIMPLE_COMPUTER_STRING = 'simpleConputer'
SMART_COMPUTER_STRING = 'smartComputer'

PLAYER_SELECTION_REGEX = '^[/1/2/3]{1}$'
MARKER_TYPE_SELECTION_REGEX = '^[/1/2/]{1}$'
NORMAL_MARKER_REGEX = '^$|^[^\\d\t/ */]{1}$'
EMOJI_REGEX = emoji_regex()
MARKER_REGEX = f'{NORMAL_MARKER_REGEX}|^{EMOJI_REGEX}$'
PLAY_AGAIN_REGEX = '^[/y/n/Y/N]{1}$'

MENU_ERROR = "Please select an option from the menu"
MARKER_ERROR = "Please choose a valid marker"
EMOJI_ERROR = "Please enter a valid emoji name"
SPACES_ERROR = "Please select from available spaces"


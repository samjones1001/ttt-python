import emojis
from emojis.emojis import RE_EMOJI_TO_TEXT_GROUP

def is_string_with_emojis(string):
    return emojis.count(string) > 0

def emoji_regex():
    return RE_EMOJI_TO_TEXT_GROUP[1:-1]


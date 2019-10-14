import emojis


def is_emoji(emoji_name):
    return emojis.db.get_emoji_by_alias(emoji_name) is not None


def get_emoji(emoji_name):
    return emojis.encode(f":{emoji_name}:")


def is_string_with_emojis(string):
    return emojis.count(string) > 0
from prompt_toolkit.completion import NestedCompleter


def get_nested_completer() -> NestedCompleter:
    """
    Method that creates the dictionary with the instructions how to prompt commands
    in console for the bot.
    :return: NestedCompleter instance
    """
    return NestedCompleter.from_nested_dict(
        {
            "help": None,
            "hello": None,
            "delete": {
                "contact": None,
            },
            "change": {
                "contact": None,
                "phone": None,
                "email": None,
                "address": None,
                "name": None,
                "birthday": None,
                "note's": {
                    "title": None,
                    "content": None,
                },
            },
            "phone": None,
            "show": {
                "all": {
                    "contacts": None,
                },
                "days to birthday": None,
            },
            "good bye": None,
            "close": None,
            "exit": None,
            "add": {
                "contact": None,
                "phone": None,
                "email": None,
                "address": None,
            },
            "search": {
                "contact": None,
            },
            "upcoming birthdays": None,
        }
    )

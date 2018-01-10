import re

regex_has_some_number = re.compile(r"(\d)")

def has_some_number(text):
    return bool(regex_has_some_number.search(text))


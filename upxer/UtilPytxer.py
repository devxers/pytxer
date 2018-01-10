import re

regex_has_some_number = re.compile(r"(\d)")
regex_has_some_letter = re.compile(r"([A-z])")


def has_some_number(text):
    return bool(regex_has_some_number.search(text))


def has_some_letter(text):
    return bool(regex_has_some_letter.search(text))

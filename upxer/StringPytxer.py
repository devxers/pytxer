import re

regex_first_letter_lowercase = re.compile(r"(^[^A-Z])")


def capitalize(text):
    if bool(regex_first_letter_lowercase.search(text)):
        return text[:1].upper() + text[1:]
    else:
        return text

import re

regex_first_letter_lowercase = re.compile(r"(^[^A-Z])")


def capitalize(text):
    if bool(regex_first_letter_lowercase.search(text)):
        return text[:1].upper() + text[1:].lower()
    else:
        return text

def list_to_string(list):
    return " ".join(str(x) for x in list)


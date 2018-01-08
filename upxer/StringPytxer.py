import re

regex_first_letter_lowercase = re.compile(r"(^[^A-Z])")
regex_capitalize_name = re.compile(r"\b[^\s^A-Z]")


def capitalize(text):
    if bool(regex_first_letter_lowercase.search(text)):
        return text[:1].upper() + text[1:].lower()
    else:
        return text

def list_to_string(list):
    return " ".join(str(x) for x in list)


def capitalize_name(name):
    if bool(regex_capitalize_name.search(name)):
        list_of_substrings = name.split()

        list_of_substrings_capitalize = [capitalize(word) for word in list_of_substrings]

        return list_to_string(list_of_substrings_capitalize)
    else:
        return name



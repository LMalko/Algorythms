import re


def spelling_correction(string):

    regex = re.compile(r" {2,}")
    string = regex.sub(" ", string)

    regex = re.compile(r"(\.)([A-Za-z])")
    string = regex.sub(r"\1 \2", string)
    return string
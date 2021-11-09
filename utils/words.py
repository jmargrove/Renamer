import re


def words(string: str):
    return re.findall(r'\w+', string)

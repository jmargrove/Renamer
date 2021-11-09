"""
Converts 'string' to kebab case
https://en.wikipedia.org/wiki/Letter_case#Special_case_styles
"""

from utils.words import words


def kebab_case(string: str):
    trim_ws = string.strip()
    rm_2027 = trim_ws.replace(u'\u0027', "")
    lower = rm_2027.lower()
    return '-'.join(words(lower))

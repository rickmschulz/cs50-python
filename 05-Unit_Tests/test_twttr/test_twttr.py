"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

from twttr import shorten


def test_words():
    assert shorten("twitter") == "twttr"
    assert shorten("google") == "ggl"
    assert shorten("gOogle") == "ggl"
    assert shorten("google1") == "ggl1"
    assert shorten("twitter.") == "twttr."

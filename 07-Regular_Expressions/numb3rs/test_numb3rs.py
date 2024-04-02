import pytest
from numb3rs import validate


def test_range():
    assert validate("155.0.1.255") == True
    assert validate("0.0.0.0") == True
    assert validate("255.0.100.280") == False
    assert validate("10.10.10.10.10") == False


def test_char():
    assert validate("cat.0.0.1") == False
    assert validate("1.150.1.dog") == False

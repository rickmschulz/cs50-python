import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/5") == 60
    assert convert("1/2") == 50
    assert convert("7/10") == 70
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    # Test non-integer fraction
    with pytest.raises(ValueError):
        convert("3.5/5")
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_gauge():
    # empty tank
    assert gauge(1) == "E"
    assert gauge(0) == "E"

    # full tank
    assert gauge(99) == "F"
    assert gauge(100) == "F"

    # normal percentage
    assert gauge(60) == "60%"
    assert gauge(75) == "75%"

    # out of range percentages
    assert gauge(-5) == "E"
    assert gauge(105) == "F"

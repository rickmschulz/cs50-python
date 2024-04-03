import pytest
from jar import Jar


def test_init():
    # default values
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # testing setters
    with pytest.raises(ValueError):
        jar.capacity = -1
    with pytest.raises(ValueError):
        jar.size = -1

    # value greater than capacity
    with pytest.raises(ValueError):
        jar.size = 15

    # invalid capacity
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # deposit greater than capacity
    with pytest.raises(ValueError):
        jar.deposit(20)

    # negative deposit
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-10)


def test_withdraw():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"

    # withdraw greater than cookies in the jar
    with pytest.raises(ValueError):
        jar.withdraw(10)

    # negative withdraw
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-10)

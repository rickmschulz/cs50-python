from bank import value


def test_conditions():
    assert value("hello") == 0
    assert value("h") == 20
    assert value("") == 100


def test_general_cases():
    assert value("What's up?") == 100
    assert value("How are you?") == 20


def test_capitalization():
    assert value(" Hello ") == 0
    assert value(" HeLLo ") == 0
    assert value(" HELLO ") == 0

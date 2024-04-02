from plates import is_valid


def test_general():
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA2AA") == False
    assert is_valid("AABBCC") == True
    assert is_valid("AA22AA") == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False


def test_start_letters():
    assert is_valid("CS") == True
    assert is_valid("50CS") == False


def test_first_number():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


def test_typographical_symbols():
    assert is_valid(".CS50") == False
    assert is_valid(",CS05") == False
    assert is_valid(" 50") == False
    assert is_valid("HELLO, WORLD") == False


def test_alphanumeric_characters():
    assert is_valid("HELLO!") == False
    assert is_valid("HELLO@WORLD") == False

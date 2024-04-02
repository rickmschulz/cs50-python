from um import count


def test_words():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um, um") == 2
    assert count("Um, um, UM!") == 3


def test_words_phrases():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_words_with_um():
    assert count("instrumentation") == 0
    assert count("umbellifer") == 0
    assert count("jump") == 0
    assert count("arum") == 0

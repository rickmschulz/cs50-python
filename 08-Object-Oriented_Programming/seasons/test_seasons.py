import pytest
from seasons import convert


def test_convert():
    # 2024 year is a leap year
    assert convert("2023-04-02") == "Five hundred twenty-seven thousand forty minutes"

    with pytest.raises(SystemExit):
        convert("202-04-10")
    with pytest.raises(SystemExit):
        convert("1990-02-1")
    with pytest.raises(SystemExit):
        convert("January 1, 1999")

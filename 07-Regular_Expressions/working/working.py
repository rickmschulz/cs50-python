"""
In a file called working.py, implement a function called convert that expects a
str in either of the 12-hour formats below and returns the corresponding str in
24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized
(with no periods therein) and that there will be a space before each. Assume
that these times are representative of actual times, not necessarily 9:00 AM and
5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those
formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do
not assume that someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or
implement other functions as you see fit, but you may not import any other
libraries. You’re welcome, but not required, to use re and/or sys.

Either before or after you implement convert in working.py, additionally
implement, in a file called test_working.py, three or more functions that
collectively test your implementation of convert thoroughly, each of whose names
should begin with test_ so that you can execute your tests with:
"""

import re
import sys


def get_clean_time(time: str) -> tuple:
    pattern = r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)"
    if cleaned_time := re.search(pattern, time):
        return cleaned_time.groups()
    raise ValueError


def convert(s: str) -> str:
    # first reference -> ('5', None, 'AM', '12', None, 'PM')
    # second reference -> ('5', "00", 'AM', '12', "00", 'PM')
    h1, m1, p1, h2, m2, p2 = get_clean_time(s)

    # check if m1 and m2 exists
    m1 = 0 if not m1 else m1
    m2 = 0 if not m2 else m2

    # convert to int
    h1, m1, h2, m2 = map(int, [h1, m1, h2, m2])

    # convert hours to 24h format
    if h1 == 12 and p1 == "AM":
        h1 = 0
    elif h1 != 12 and p1 == "PM":
        h1 += 12

    if h2 == 12 and p2 == "AM":
        h2 = 0
    elif h2 != 12 and p2 == "PM":
        h2 += 12

    # validate hours and minutes
    if not 0 <= h1 <= 23 or not 0 <= m1 <= 59 or not 0 <= h2 <= 23 or not 0 <= m2 <= 59:
        raise ValueError("Invalid arguments")

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()

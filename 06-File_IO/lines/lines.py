"""
Even so, in a file called lines.py, implement a program that
expects exactly one command-line argument, the name (or
path) of a Python file, and outputs the number of lines of
code in that file, excluding comments and blank lines. If
the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py, or if
the specified file does not exist, the program should
instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded
by whitespace, is a comment. (A docstring should not be
considered a comment.) Assume that any line that only
contains whitespace is blank.
"""

import sys


def is_code(line):
    line = line.strip()
    if line.startswith("#") or line == "":
        return False
    return True


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        try:
            count = 0
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if is_code(line):
                        count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            print(count)
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()

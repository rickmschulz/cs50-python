"""
In a file called pizza.py, implement a program that expects
exactly one command-line argument, the name (or path) of a
CSV file in Pinocchio’s format, and outputs a table
formatted as ASCII art using tabulate, a package on PyPI at
pypi.org/project/tabulate. Format the table using the
library’s grid format. If the user does not specify exactly
one command-line argument, or if the specified file’s name
does not end in .csv, or if the specified file does not
exist, the program should instead exit via sys.exit.
"""

import sys
import csv
from tabulate import tabulate


def check_arguments() -> bool:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("Too many command-line arguments")


def main():
    if check_arguments():
        try:
            with open(sys.argv[1], "r") as file:
                reader = [row for row in csv.reader(file)]
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            pass


if __name__ == "__main__":
    main()

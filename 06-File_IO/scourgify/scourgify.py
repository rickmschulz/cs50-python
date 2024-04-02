"""
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose
columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns
should be, in order, first, last, and house.
Converts that input to that output, splitting each name into
a first name and last name. Assume that each student will
have both a first name and last name.
If the user does not provide exactly two command-line
arguments, or if the first cannot be read, the program
should exit via sys.exit with an error message.
"""

import sys
import csv


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3:
        input_csv_file, output_csv_file = sys.argv[1:]
        if input_csv_file.endswith(".csv") and output_csv_file.endswith(".csv"):
            return input_csv_file, output_csv_file
        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("Too many command-line arguments")


def main():
    input_csv_file, output_csv_file = check_arguments()
    if input_csv_file and output_csv_file:
        try:
            cleaned_csv = []
            # open input csv file
            with open(input_csv_file, "r") as read_file:
                read_file = csv.DictReader(read_file)
                for row in read_file:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    cleaned_csv.append({"first": first, "last": last, "house": house})

            # open output csv file
            with open(output_csv_file, "w") as write_file:
                writer = csv.DictWriter(
                    write_file, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()
                writer.writerows(cleaned_csv)

        except FileNotFoundError:
            sys.exit(f"Could not read {input_csv_file}")


if __name__ == "__main__":
    main()

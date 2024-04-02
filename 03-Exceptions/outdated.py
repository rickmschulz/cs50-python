"""
Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def date_format_first(date):
    date_format = date.split("/")
    if len(date_format) == 3:
        for _ in date_format:
            if not _.isdigit():
                return False
        return True


def date_format_second(date):
    date_format = date.split(",")
    if len(date_format) == 2:
        return True
    return False


def validate_date(date):
    while True:
        date = str(input(date)).strip()

        # First Case - month-day-year - e.g.: 9/8/1636
        if date_format_first(date):
            date_format = date.split("/")
            yyyy = int(date_format[2])
            mm = int(date_format[0])
            dd = int(date_format[1])
            if 0 < dd <= 31 and 0 < mm <= 12:
                return print(f"{yyyy:04}-{mm:02}-{dd:02}")

        # Second Case - e.g.: September 8, 1636
        if date_format_second(date):
            date_format = date.split(",")
            mm = date_format[0].split()[0]
            try:
                mm = months.index(mm) + 1
            except ValueError:
                continue
            else:
                dd = int(date_format[0].split()[1])
                yyyy = int(date_format[1])
                if 0 < dd <= 31 and 0 < mm <= 12:
                    return print(f"{yyyy:04}-{mm:02}-{dd:02}")


def main():
    date = validate_date("Date: ")


if __name__ == "__main__":
    main()

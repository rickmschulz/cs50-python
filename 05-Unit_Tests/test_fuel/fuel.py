"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""


def convert(fraction: str) -> int:
    while True:
        try:
            x, y = str(fraction).split("/")
            x, y = int(x), int(y)
            if y == 0:
                raise ZeroDivisionError("Y cannot be zero")
            if x > y:
                raise ValueError("X cannot be greater than Y")
            fuel = x / y
            if 0 < fuel > 1:
                raise ValueError
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            return round(fuel * 100)


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    convert("5/0")
    gauge(60)


if __name__ == "__main__":
    main()

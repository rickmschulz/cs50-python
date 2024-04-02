"""
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            random_number = random.randint(1, level)
        except ValueError:
            pass
            # print("Value is not an integer!")
        else:
            return level, random_number


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
            # print("Value is not an integer!")
        else:
            return guess


def main():

    level, random_number = get_level()
    guess = get_guess()

    while True:
        # if guess > level:
        #     # print("Out-of-range level.")
        #     guess = get_guess()
        if guess == random_number:
            print("Just right!")
            break
        elif guess > random_number:
            print("Too large!")
            guess = get_guess()
        else:
            print("Too small!")
            guess = get_guess()


if __name__ == "__main__":
    main()

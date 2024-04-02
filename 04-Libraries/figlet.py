"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
from random import choice
from pyfiglet import Figlet


def random_font(figlet, font_list):
    prompt = str(input("Input: "))
    font = choice(font_list)
    figlet.setFont(font=font)
    print(figlet.renderText(prompt))


def specific_font(figlet):
    prompt = str(input("Input: "))
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(prompt))


def main():

    figlet = Figlet()
    font_list = figlet.getFonts()

    if len(sys.argv) < 2:
        random_font(figlet, font_list)

    elif (
        len(sys.argv) == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and sys.argv[2] in font_list
    ):
        specific_font(figlet)

    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()

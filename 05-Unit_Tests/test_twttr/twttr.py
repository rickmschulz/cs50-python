"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""


def main():
    new_word = shorten("twitter")
    print(new_word)


def shorten(word):
    vowels = ("a", "e", "i", "o", "u")

    new_word = []
    for char in word:
        if char.lower() not in vowels:
            new_word.append(char.lower())
    new_word = "".join(new_word)
    return new_word


if __name__ == "__main__":
    main()

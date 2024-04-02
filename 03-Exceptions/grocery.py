"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""


def get_items(prompt):
    items = dict()
    while True:
        try:
            item = str(input(prompt)).upper()
        except EOFError:
            print()
            return items
        else:
            if items.get(item):
                items[item] += 1
            else:
                items[item] = 1


def main():
    items = get_items("")

    # Sorting keys and Show results
    for item in sorted(items.keys()):
        print(items[item], item)


if __name__ == "__main__":
    main()

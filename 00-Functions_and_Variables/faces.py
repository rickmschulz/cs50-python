def convert(msg):
    chars_to_replace = {':)': '🙂',
                        ':(': '🙁'}

    for char in chars_to_replace:
        if char in msg:
            msg = msg.replace(char, chars_to_replace[char])
    return msg


def main():
    msg = str(input('Write the message: '))
    msg = convert(msg)
    print(msg)

main()

"""
In a file called shirt.py, implement a program that expects
exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read
(i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write
(i.e., save) as output
The program should then overlay shirt.png (which has a
transparent background) on the input after resizing and
cropping the input to be the same size, saving the result as
its output.

Open the input with Image.open, per
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per
pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering,
overlay the shirt with Image.paste, per
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
and save the result with Image.save, per
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line
arguments,
if the input’s and output’s names do not end in .jpg, .jpeg,
or .png, case-insensitively,
if the input’s name does not have the same extension as the
output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in
just the right way, like these demos, so that, when they’re
resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself,
first drag the photo over to VS Code’s file explorer, into
the same folder as shirt.py. No need to submit any photos
with your code. But, if you would like, you’re welcome (but
not expected) to share a photo of yourself wearing your
virtual shirt in any of CS50’s communities!
"""

import sys
from PIL import Image, ImageOps


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3:
        input_img_file, output_img_file = sys.argv[1:]
        extensions = [".jpg", ".jpeg", ".png"]
        extension_input = "." + input_img_file.lower().rsplit(".", 1)[1]
        extension_output = "." + output_img_file.lower().rsplit(".", 1)[1]
        if extension_input not in extensions:
            sys.exit("Invalid input")
        elif extension_input not in extensions or extension_output not in extensions:
            sys.exit("Invalid output")
        if extension_input == extension_output:
            return input_img_file, output_img_file
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Too many command-line arguments")


def main():
    input_img_file, output_img_file = check_arguments()
    if input_img_file and output_img_file:
        try:
            # shirt image
            shirt_file = "shirt.png"
            with Image.open(shirt_file) as shirt:
                # pasting
                with Image.open(input_img_file) as input_img_file:
                    input_img_file_resized = ImageOps.fit(input_img_file, shirt.size)
                    input_img_file_resized.paste(shirt, shirt)
                    input_img_file_resized.save(output_img_file)

        except FileNotFoundError:
            sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

"""
Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image
of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for
their name and outputs, using fpdf2, a CS50 shirtificate in a file called
shirtificate.pdf similar to this one for John Harvard, with these
specifications:

The orientation of the PDF should be Portrait.

The format of the PDF should be A4, which is 210mm wide by 297mm tall.

The top of the PDF should say “CS50 Shirtificate” as text, centered
horizontally.

The shirt’s image should be centered horizontally.

The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders, colors,
and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need
to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use
it. Then skim fpdf2’s API (application programming interface) to see all of its
functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re
welcome (but not expected) to share a shirtificate with your name on it in any
of CS50’s communities!
"""

from fpdf import FPDF, enums


class PDF(FPDF):
    def header(self):
        # performing a line break:
        self.ln(20)
        # setting font: helvetica bold 50
        self.set_font("helvetica", "", 50)
        # printing title:
        self.cell(
            w=0,
            h=10,
            text=self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        # performing a line break:
        self.ln(30)


def main():
    name = str(input("Name: ")).strip().title()
    shirtificate = "CS50 Shirtificate"
    name = f"{name} took CS50"

    # initial steps
    pdf = PDF()
    pdf.set_auto_page_break(False)
    pdf.set_title(shirtificate)
    pdf.add_page()

    # add shirt image
    pdf.image(
        name="shirtificate.png",
        x=enums.Align.C,
        w=pdf.epw,
    )

    # setting font and font color
    pdf.set_font("helvetica", "", 20)
    pdf.set_text_color(255, 255, 255)

    # place text in shirt image
    text_width = pdf.get_string_width(name) + 6
    pdf.text(x=(210 - text_width) / 2, y=140, text=name)

    # output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

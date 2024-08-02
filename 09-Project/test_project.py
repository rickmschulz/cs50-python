import pytest
import argparse
import io
import sys
from unittest.mock import patch
from pyfiglet import Figlet
from tabulate import tabulate
import textwrap
from project import (
    get_cli_arguments,
    get_asc_art,
    display_movie_info,
)


def test_get_cli_arguments():
    # Mock command-line arguments
    test_args = ["test_project.py", "Inception"]
    with patch.object(sys, "argv", test_args):
        args = get_cli_arguments()

    assert args.movie == "Inception"


def test_get_asc_art():
    # Capture the output of get_asc_art
    movie_title = "Inception"
    figlet = Figlet(font="small")
    expected_art = figlet.renderText(movie_title).strip()

    # Capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    get_asc_art(movie_title)

    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_art


def test_display_movie_info():
    # Sample movie info data
    movie_info = {
        "Title": "Inception",
        "Year": "2010",
        "Plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
        "Ratings": [
            {"Source": "Internet Movie Database", "Value": "8.8/10"},
            {"Source": "Rotten Tomatoes", "Value": "87%"},
        ],
        "Response": "True",
    }

    # Expected output format
    expected_table = [
        ("Title", "Inception"),
        ("Year", "2010"),
        ("Plot", "\n".join(textwrap.wrap(movie_info["Plot"], width=60))),
        ("Rating (Internet Movie Database)", "8.8/10"),
        ("Rating (Rotten Tomatoes)", "87%"),
    ]
    expected_output = tabulate(
        expected_table, tablefmt="grid", colalign=("left", "left")
    )

    # Capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    display_movie_info(movie_info)

    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

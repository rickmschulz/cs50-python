import sys
import os
import argparse
import requests
from dotenv import load_dotenv
from tabulate import tabulate
from pyfiglet import Figlet
import textwrap


class OmdbAPI:
    def __init__(self, api_key) -> None:
        if not api_key:
            sys.exit("API key missing. Set the API key in the .env file.")
        self.api_key = api_key
        self.url = f"http://www.omdbapi.com/?apikey={self.api_key}"
        self.headers = {"Content-Type": "application/json"}

    def get_response(self, params):
        try:
            response = requests.get(self.url, headers=self.headers, params=params)
            response.raise_for_status()  # raise an error for bad response status
            return response
        except requests.exceptions.RequestException as e:
            sys.exit(f"An error occurred while fetching data: {e}")


def get_cli_arguments():
    parser = argparse.ArgumentParser(description="Fetch movie details from OMDb API")
    parser.add_argument("movie", help="The title of the movie to search for")
    args = parser.parse_args()
    return args


def get_asc_art(s):
    figlet = Figlet(font="small")
    print(figlet.renderText("-" * (len(s) + 2)))
    print(figlet.renderText(s))
    print(figlet.renderText("-" * (len(s) + 2)))


def display_movie_info(movie_info):
    table_data = []

    # Add simple key-value pairs to table data
    for key, value in movie_info.items():
        # Skip the Ratings key and Response key initially
        if key not in ["Ratings", "Response"]:
            # Wrap text for readability instead of truncating
            if isinstance(value, str):
                value = "\n".join(textwrap.wrap(value, width=60))
            table_data.append((key, value))

    # Handle the nested Ratings list
    ratings = movie_info.get("Ratings", [])
    for rating in ratings:
        source = rating.get("Source", "Unknown Source")
        value = rating.get("Value", "N/A")
        table_data.append((f"Rating ({source})", value))

    # Print the table with aligned text
    print(tabulate(table_data, tablefmt="grid", colalign=("left", "left")))


def main():
    # Load environment variables from .env.
    load_dotenv()

    # API instance
    api = OmdbAPI(os.getenv("API_KEY"))

    # Get CLI arguments
    args = get_cli_arguments()

    # Parameters for the API request
    params = {
        "t": args.movie,
    }

    # Fetch and display movie information
    try:
        response = api.get_response(params=params)
        movie_info = response.json()
        if movie_info.get("Response", "False") == "True":
            get_asc_art(movie_info["Title"])
            display_movie_info(movie_info)
        else:
            sys.exit(f"Movie not found: {movie_info.get('Error')}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

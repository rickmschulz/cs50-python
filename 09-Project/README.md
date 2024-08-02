# Movie Info CLI

#### Video Demo: <https://youtu.be/WFzdmcG2D3E>

#### Description:

Movie Info CLI is a simple command-line interface (CLI) tool that allows users to fetch detailed information about movies using the OMDb API. The application retrieves data such as title, release year, plot, director, cast, and ratings from various sources. It presents this information in a well-organized table format in the terminal. Additionally, the movie title is displayed in ASCII art to enhance the user experience.

## Features

- Fetch movie details from the OMDb API.
- Display information in a neatly formatted table.
- Show movie titles in ASCII art.
- Support for multiple rating sources.
- Command-line interface for easy use.

## Requirements

- Python 3.x
- [OMDb API Key](http://www.omdbapi.com/apikey.aspx)
- Required Python packages: `requests`, `pyfiglet`, `python-dotenv`, `tabulate`

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/movie-info-cli.git
```

```bash
cd movie-info-cli
```
Install the required packages:

```bash
pip install -r requirements.txt
```

Create a .env file in the root directory and add your OMDb API key:

```bash
API_KEY=your_api_key_here
```

## Usage

Run the script with the movie title as an argument:

```bash
python movie_info.py "Inception"
```

The application will display the movie details in the terminal, including the title in ASCII art and ratings from different sources.

## Examples

```bash
python movie_info.py "The Matrix"
```

This command fetches and displays details about the movie "The Matrix."

## Troubleshooting

- API Key Missing: Ensure your .env file contains a valid API_KEY.
- Network Issues: Check your internet connection if the application fails to fetch data.

## Acknowledgements

OMDb API for providing movie data.

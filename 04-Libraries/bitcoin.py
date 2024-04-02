"""
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of
 Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import requests
import sys


def get_bitcoin_quantity():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Too many arguments")
    return n


def get_bitcoin_value():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        sys.exit(e)
    json = response.json()
    return float(json["bpi"]["USD"]["rate_float"])


def main():
    n = get_bitcoin_quantity()
    value = get_bitcoin_value()
    total = n * value
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()

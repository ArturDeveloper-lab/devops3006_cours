import random

import requests


def ger_the_rate():
    url = "https://v6.exchangerate-api.com/v6/1d4d2fe5e7d4bceed6c590e4/latest/USD"
    response = requests.request("GET", url)
    response.raise_for_status()
    jsonResponse = response.json()
    ils_rate = jsonResponse["conversion_rates"]["ILS"]
    return ils_rate


def difficult():
    random_number = random.randint(1, 5)
    return random_number


def lower_value(t: int, d: int):
    return round((t - (5 - d)))


def high_value(t: int, d: int):
    return round((t + (5 - d)))


def number_from_user():
    return int(input("Enter a number between 1 - 100: \n"))


if __name__ == '__main__':
    if lower_value(ger_the_rate(), difficult()) <= number_from_user() <= high_value(ger_the_rate(), difficult()):
        print("true")
    else:
        print("false")

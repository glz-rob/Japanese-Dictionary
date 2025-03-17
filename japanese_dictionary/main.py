#!/usr/bin/env python3
import requests

from utils import clear
from word import Word

DICT_URL = 'https://jisho.org/api/v1/search/words?keyword='

MENU = """1. Search a word
2. Exit"""
TITLE = 'Japanese Dictionary'


def search(text):
    res = requests.get(DICT_URL + text).json()

    if res['meta']['status'] == 200:
        return res['data']
    else:
        return None


def main():
    while True:
        clear()
        print(TITLE)
        print(MENU)

        choice = input('Enter an option: ')

        clear()
        if choice == '1':
            print(TITLE)
            data = search(input('Enter a word to search for: '))
            clear()

            print("Results:")
            if data:
                for entry in data:
                    print('-------------------')
                    print(Word(entry))
            else:
                print('No results found')

            input()

        if choice == '2':
            print(TITLE)
            exit()


if __name__ == "__main__":
    main()

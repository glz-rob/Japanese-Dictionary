#!/usr/bin/env python3
import requests

from word import Word

DICT_URL = 'https://jisho.org/api/v1/search/words?keyword='


def search(text):
    res = requests.get(DICT_URL + text).json()

    if res['meta']['status'] == 200:
        return res['data']
    else:
        return None

def main():
    word_info = search(input('Enter a word: '))

    if word_info:
        for entry in word_info:
            print(Word(entry))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os

from japanese_dictionary.main import search

prg = 'japanese_dictionary/main.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_01():
    """test search function"""

    for val in ['', 'dog', '犬', "犬は大きです"]:
        search_res = search(val)
        assert search_res is not None

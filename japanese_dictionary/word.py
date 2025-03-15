#!/usr/bin/env python3

TEST_1 = {'slug': '赤', 'is_common': True, 'tags': ['wanikani4'], 'jlpt': ['jlpt-n5'], 'japanese': [{'word': '赤', 'reading': 'あか'}, {'word': '紅', 'reading': 'あか'}, {'word': '朱', 'reading': 'あか'}, {'word': '緋', 'reading': 'あか'}], 'senses': [{'english_definitions': ['red', 'crimson', 'scarlet'], 'parts_of_speech': ['Noun', "Noun which may take the genitive case particle 'no'"], 'links': [], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['red-containing colour (e.g. brown, pink, orange)'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['Red (i.e. communist)'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Colloquial'], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': ['often written as アカ']}, {'english_definitions': ['red light (traffic)'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Abbreviation'], 'restrictions': [], 'see_also': ['赤信号'], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['red ink (i.e. in finance or proof-reading)', '(in) the red'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Abbreviation'], 'restrictions': [], 'see_also': ['赤字', '赤字'], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['complete', 'total', 'perfect', 'obvious'], 'parts_of_speech': ["Noun which may take the genitive case particle 'no'"], 'links': [], 'tags': [], 'restrictions': [], 'see_also': ['赤の他人'], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['copper'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Abbreviation'], 'restrictions': ['赤'], 'see_also': ['銅 あかがね'], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['red 5-point card'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Hanafuda', 'Abbreviation'], 'restrictions': [], 'see_also': ['あかたん'], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['Aka'], 'parts_of_speech': ['Place'], 'links': [], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['Red'], 'parts_of_speech': ['Wikipedia definition'], 'links': [{'text': 'Read “Red” on English Wikipedia', 'url': 'http://en.wikipedia.org/wiki/Red?oldid=495022741'}, {'text': 'Read “赤” on Japanese Wikipedia', 'url': 'http://ja.wikipedia.org/wiki/赤?oldid=42762386'}], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': [], 'sentences': []}], 'attribution': {'jmdict': True, 'jmnedict': True, 'dbpedia': 'http://dbpedia.org/resource/Red'}}
# TEST_2 = {'slug': 'レモン', 'is_common': True, 'tags': [], 'jlpt': [], 'japanese': [{'word': '檸檬', 'reading': 'レモン'}], 'senses': [{'english_definitions': ['lemon'], 'parts_of_speech': ['Noun'], 'links': [], 'tags': ['Usually written using kana alone'], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': []}, {'english_definitions': ['Lemon'], 'parts_of_speech': ['Wikipedia definition'], 'links': [{'text': 'Read “Lemon” on English Wikipedia', 'url': 'http://en.wikipedia.org/wiki/Lemon?oldid=495387540'}, {'text': 'Read “レモン” on Japanese Wikipedia', 'url': 'http://ja.wikipedia.org/wiki/レモン?oldid=42743366'}], 'tags': [], 'restrictions': [], 'see_also': [], 'antonyms': [], 'source': [], 'info': [], 'sentences': []}], 'attribution': {'jmdict': True, 'jmnedict': False, 'dbpedia': 'http://dbpedia.org/resource/Lemon'}}

class Word:
    """Model for a word entry from the Jisho API"""

    def __init__(self, entry: dict) -> None:
        self.word = entry['slug']
        self.japanese = entry['japanese']
        self.senses = entry['senses']

    def __str__(self) -> str:
        return_string = f'{self.word}\n'

        return_string += 'Meanings:\n'
        for id, entry in enumerate(self.senses):
            return_string += ', '.join(entry['parts_of_speech'])
            return_string += '\n'

            return_string += f'{id + 1}. '
            return_string += ', '.join(entry['english_definitions'])
            return_string += '\n'

        return_string += 'Other Forms:\n'
        for entry in self.japanese:
            return_string += '- '
            if entry.get('word'):
                return_string += f'{entry['word']}'
            if entry.get('reading'):
                return_string += f' ({entry['reading']})'
            return_string += '\n'

        return return_string


def main():
    myWord = Word(TEST_1)
    print(myWord)


if __name__ == "__main__":
    main()

import re
from collections import Counter

WORD_REGEX = r"[a-zA-Z\d]+(?:\'t)?"


def count_words(sentence):
    words = re.findall(WORD_REGEX, sentence)
    return Counter(map(str.lower, words))

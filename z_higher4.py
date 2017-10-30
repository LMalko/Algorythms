"""Alghorithmic warm-ups: zadanie 4 form Higher order functions and list comprehensions 20."""


def filter_long_words(words, length):
    return list(filter(lambda word: len(word) > length, words))

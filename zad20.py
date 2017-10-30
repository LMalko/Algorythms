"""Alghorithmic warm-ups: zadanie20."""


def translate(english_wishes):
    _my_lexicon = {
                        "merry": "god",
                        "christmas": "jul",
                        "and": "och",
                        "happy": "gott",
                        "new": "nytt",
                        "year": "år"
                    }

    _swedish_wishes = []
    for word in english_wishes:
        if word in _my_lexicon:
            _translated_word = _my_lexicon[word]
            _swedish_wishes.append(_translated_word)
    return _swedish_wishes

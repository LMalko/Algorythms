"""Alghorithmic warm-ups: zadanie 1 from Somewhat harder exercises."""


def splitter(text):
    _sentences = []
    _sentence = ''
    for index, char in enumerate(text):
        _should_skip = False
        _sentence += char
        if char in ('!', '?'):
            _sentences.append(_sentence)
            _sentence = ''
        elif char == '.':
            # check skip conditions (period is not end of sentence):
            if index < len(text) - 1 and index not in (0, 1, 2, 3):
                # set next/previous word:
                # _prevoius_char = text[index-1]
                _next_char = text[index+1]

                if _next_char != ' ':
                    _should_skip = True
                else:
                    _slice_to_check = text[index-3:index]
                    for letter in _slice_to_check:
                        if letter.isupper():
                            _should_skip = True
                            break
                if _should_skip is False:
                    _sentences.append(_sentence)
                    _sentence = ''
    _sentences.append(_sentence)
    return _sentences

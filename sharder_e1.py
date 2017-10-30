import time

# A sentence splitter is a program capable of splitting a text into sentences.
# The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
# Sentence boundaries occur at one of "." (periods), "?" or "!", except that
#
# Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
#
# Periods followed by a digit with no intervening whitespace are not sentence boundaries.
#
# Periods followed by whitespace and then an upper case letter,
# but preceded by any of a short list of titles are not sentence boundaries.
# Sample titles include Mr., Mrs., Dr., and so on.
#
# Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
# (for example, www.aptex.com (Łącza do strony zewnętrznej.)Łącza do strony zewnętrznej., or e.g).
#
# Periods followed by certain kinds of punctuation (notably comma and more periods)
# are probably not sentence boundaries.


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

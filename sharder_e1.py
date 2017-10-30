"""Alghorithmic warm-ups: zadanie 1 from Somewhat harder exercises."""


def splitter(text, display_sentences=False):
    """
    Return list (_sentences) of sentences.

    If to_display_sentences is True, function displays sentences in terminal.
    """
    _sentences = []
    _sentence = ''
    for index, char in enumerate(text):
        _should_skip = False
        _sentence += char
        if char in ('!', '?'):
            _sentences.append(_sentence)
            _sentence = ''
        elif char == '.':
            # check skip conditions (if period is not end of sentence):
            if index < len(text) - 1 and index not in (0, 1, 2, 3):  # to avoid index error
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

    # remove unnecessary whitespaces, capitalize first letter of sentences
    _output_sentences = []
    for sentence in _sentences:
        _stripped_sentence = sentence.lstrip(' ')
        _capitalize_sentence = _stripped_sentence.capitalize()
        _output_sentences.append(_capitalize_sentence)

    if display_sentences:
        for sentence in _output_sentences:
            print(sentence)

    return _output_sentences

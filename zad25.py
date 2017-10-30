"""Alghorithmic warm-ups: zadanie25."""


def make_3sg_form(verb):
    _founded_suffix = False
    irregulars_suffixes = ['ss', 'x', 'ch', 'sh',  'o', 'y']
    for suffix in irregulars_suffixes:
        if verb.endswith(suffix):
            _founded_suffix = suffix
            break
    if _founded_suffix:
        if suffix in ['ss', 'x', 'ch', 'sh',  'o']:
            return verb + 'es'
        elif suffix == 'y':
            _output_verb = verb[0:-1] + 'ies'
            return _output_verb
    else:
        return verb + 's'

"""Alghorithmic warm-ups: zadanie25."""


# Your task in this exercise is to define a function make_3sg_form()
# which given a verb in infinitive form returns its third person singular form.
# Test your function with words like try, brush, run and fix.
# Note however that the rules must be regarded as heuristic, in the sense that you must
# not expect them to work for all cases.
# Tip: Check out the string method endswith().

def make_3sg_form(verb):
    irregulars_suffixes = ['SS', 'X', 'CH', 'SH' or 'O']

    _verb_suffix = ''
    _verb_3sg_form = ''
    # SS, X, CH, SH or the letter O
    else:
        return verb + 's'


print(make_3sg_form('make'))

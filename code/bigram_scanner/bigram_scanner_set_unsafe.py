#!/usr/bin/env python
# encoding: utf-8

bigram_grammar = set(['La', 'ab', 'ba', 'bR'])


def augment_string(w):
    """Add edge markers to string."""
    return 'L' + w + 'R'


def string_to_bigrams(w):
    """Convert string into non-repeating list of bigrams."""
    bigram_list = []
    for i in range(len(w)-1):
        current_bigram = w[i] + w[i+1]
        if current_bigram not in bigram_list:
            bigram_list.append(current_bigram)
    return bigram_list


def bigram_comparison(grammar, bigram_list):
    """Check whether a bigram grammar subsumes a list of bigrams."""
    return set(bigram_list).issubset(grammar)


def bigram_scanner(grammar, w):
    """Recognizer for bigram grammar given string w."""
    if bigram_comparison(grammar, string_to_bigrams(augment_string(w))):
        print("well-formed: " + w[1:-1])
    else:
        print("ill-formed: " + w[1:-1])

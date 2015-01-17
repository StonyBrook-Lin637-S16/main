#!/usr/bin/env python

bigram_grammar = set(['La', 'ab', 'bR'])

def augment_string(w):
    """add edge markers to string"""
    try:
        return 'L' + w + 'R'
    except TypeError:
        print("argument type of augment_string cannot be concatenated")

def string_to_bigrams(w):
    """convert string into non-repeating list of bigrams"""
    
    bigram_list = []

    for i in range(len(w)-1):
        current_bigram = w[i] + w[i+1]
        if current_bigram not in bigram_list:
            bigram_list.append(current_bigram)
    return bigram_list
        
def bigram_comparison(grammar,bigram_list):
    """Check whether a bigram grammar subsumes a list of bigrams"""

    if set(bigram_list).issubset(grammar):
        return True

def bigram_scanner(grammar,w):
    """Recognizer for bigram grammar given string w"""

    if bigram_comparison(grammar,string_to_bigrams(augment_string(w))):
        print("well-formed: " + w)
    else:
        print("ill-formed: " + w)

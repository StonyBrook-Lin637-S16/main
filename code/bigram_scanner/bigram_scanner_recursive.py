#!/usr/bin/env python
# encoding: utf-8

bigram_grammar = set(['La', 'ab', 'ba', 'bR'])


def augment_string(w):
    """add edge markers to string"""
    return 'L' + w + 'R'


def bigram_check(grammar, w, i):
    """check if specific bigram is in grammar"""
    bigram = w[i] + w[i+1]
    return bigram in grammar


def bigram_scan(grammar, w, i):
    """recursively scan through string starting at position i"""
    if bigram_check(grammar, w, i):
        if i < len(w)-2:  # we haven't seen the last bigram yet, keep going!
            bigram_scan(grammar, w, i+1)
        else:  # we made it through the entire string without error
            print("well-formed: " + w[1:-1])
    else:
        print("ill-formed: " + w[1:-1])


def bigram_scanner(grammar, w):
    """recognizer for bigram grammar given string w"""
    if type(grammar) is not list and type(grammar) is not set:
        print("wrong argument type: first argument must be list or set")
    elif type(w) is not str:
        print("wrong argument type: second argument must be string")
    else:
        bigram_scan(set(grammar), augment_string(w), 0)

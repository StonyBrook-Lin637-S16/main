#!/usr/bin/env python
# encoding: utf-8

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


def bigram_learner(language):
    """Induce a strictly 2-local grammar from a finite sample of strings"""
    grammar = set([])
    for w in language:
        grammar = grammar.union(set(string_to_bigrams(augment_string(w))))
    return grammar

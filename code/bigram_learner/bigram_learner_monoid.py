#!/usr/bin/env python
# encoding: utf-8


def bigram_learner(language):
    """Induce a strictly 2-local grammar from a finite sample of strings"""
    grammar = set([])
    for w in language:
        grammar = grammar.union(
            monoid_scanner(
                set_base,
                set_compose,
                grammar,
                augment_string(w)))
    return grammar

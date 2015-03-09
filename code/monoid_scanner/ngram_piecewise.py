#!/usr/bin/env python
# encoding: utf-8


def piecewise_base(w, grammar):
    """
    Check that input bigram is in the grammar and return:

    1) set of seen bigrams (= just the input),
    2) boolean indicating well-formedness, and
    3) the grammar so that it can be referenced by the compose function
    """
    return set([w]), w in grammar, grammar


def piecewise_compose(s, t):
    """
    Each argument is a triple of values:

    first component  -- set of 2-subsequences
    second component -- boolean indicating well-formedness
    third component  -- 2-gram grammar for which well-formedness is tested

    Based on this argument, the function computes:

    1) the set of all 2-subsequences that have been seen so far,
    2) the compound boolean.
    """

    # check that nothing went wrong with the grammar and give it a name
    if s[2] == t[2]:
        grammar = s[2]
    else:
        raise Exception("grammars of arguments differ")

    # retrieve values
    set_s = s[0]
    set_t = t[0]
    boolean_s = s[1]
    boolean_t = t[1]

    # don't do anything if we already have an ill-formed subsequence
    if (boolean_s is False) or (boolean_t is False):
        return s[0], False, s[2]
    # otherwise proceed with subsequence construction
    else:
        checked_bigrams = set_s.union(set_t)
        new_bigrams = set([])

        for i in checked_bigrams:
            for j in checked_bigrams:
                subsequence = i[0] + j[1]
                if subsequence not in checked_bigrams:
                    if subsequence in grammar:
                        # found a new licit subsequence
                        new_bigrams.add(subsequence)
                    else:
                        # found a new illicit subsequence
                        return s[0], False, s[2]
        return checked_bigrams.union(new_bigrams), True, grammar

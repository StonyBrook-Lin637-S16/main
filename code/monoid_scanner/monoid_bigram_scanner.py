#!/usr/bin/env python
# encoding: utf-8


def monoid_scanner(base_value, compose, w):
    """
    Generalized bigram scanner that assigns strings
    a value over a given monoid.

    Arguments:
    base_value -- maps a bigram to an element of the monoid
    compose    -- implements the monoid operation
    w          -- the input string
    """
    # [Base Case]
    # value of a single bigram
    if len(w) == 2:
        return base_value(w)
    # [Recursion]
    # scan string from left to right and compose values
    else:
        return compose(
            base_value(w[0:2]),
            monoid_scanner(base_value, compose, w[1:len(w)]))
